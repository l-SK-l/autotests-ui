import os
import shutil
from typing import Generator
import allure

from config import Browser, settings
from playwright.sync_api import Playwright, Page

from tools.playwright.mocks import mock_static_resources


def initialize_playwright_page(
        playwright: Playwright,
        test_name: str,
        browser_type: Browser,
        storage_state: str | None = None
) -> Generator[Page, None, None]:
    headless = os.getenv('CI', 'false').lower() == 'true'
    browser = playwright[browser_type].launch(headless=headless)
    context = browser.new_context(
        base_url=settings.get_base_url(),
        storage_state=storage_state, 
        record_video_dir=settings.videos_dir
    )
    context.tracing.start(screenshots=True, snapshots=True, sources=True)
    page = context.new_page()
    mock_static_resources(page)

    yield page

    context.tracing.stop(path=settings.tracing_dir.joinpath(f'{test_name}.zip'))
    browser.close()

    video_path = page.video.path()
    if video_path and os.path.exists(video_path):
        new_video_path = settings.videos_dir.joinpath(f'{test_name}.webm')
        shutil.copy2(video_path, new_video_path)
        os.remove(video_path)
        video_path = new_video_path

    allure.attach.file(settings.tracing_dir.joinpath(f'{test_name}.zip'), name='trace', extension='zip')
    if video_path and os.path.exists(video_path):
        allure.attach.file(video_path, name='video', attachment_type=allure.attachment_type.WEBM)