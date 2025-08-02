import os
import shutil
import allure
from typing import Generator
from playwright.sync_api import Playwright, Page


def initialize_playwright_page(
        playwright: Playwright,
        test_name: str,
        storage_state: str | None = None
) -> Generator[Page, None, None]:
    headless = os.getenv('CI', 'false').lower() == 'true'
    browser = playwright.chromium.launch(headless=headless)
    context = browser.new_context(
        storage_state=storage_state, 
        record_video_dir='./videos'
    )
    context.tracing.start(screenshots=True, snapshots=True, sources=True)
    page = context.new_page()

    yield page

    context.tracing.stop(path=f'./tracing/{test_name}.zip')

    browser.close()

    video_path = page.video.path()
    if video_path and os.path.exists(video_path):
        new_video_path = f'./videos/{test_name}.webm'
        try:
            shutil.copy2(video_path, new_video_path)
            os.remove(video_path)
            video_path = new_video_path
        except Exception:
            # If it was not possible to rename, use the original path.
            pass

    allure.attach.file(f'./tracing/{test_name}.zip', name='trace', extension='zip')
    if video_path and os.path.exists(video_path):
        allure.attach.file(video_path, name='video', attachment_type=allure.attachment_type.WEBM)