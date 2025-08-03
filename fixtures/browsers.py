import os
import pytest
from _pytest.fixtures import SubRequest
from playwright.sync_api import Page, Playwright
from typing import Generator

from pages.authentication.registration_page import RegistrationPage
from tools.playwright.pages import initialize_playwright_page
from config import settings
from tools.routes import AppRoute


@pytest.fixture(params=settings.browsers)
def browser_page(request: SubRequest, playwright: Playwright) -> Generator[Page, None, None]:
    yield from initialize_playwright_page(playwright,
                                          test_name=request.node.name,
                                          browser_type=request.param)

@pytest.fixture(scope='session', params=settings.browsers)
def initialize_browser_state(playwright: Playwright):
    headless = os.getenv('CI', 'false').lower() == 'true'
    browser = playwright.chromium.launch(headless=headless)
    context = browser.new_context(base_url=settings.get_base_url())
    page = context.new_page()

    registration_page = RegistrationPage(page=page)
    registration_page.visit(AppRoute.REGISTRATION)
    registration_page.registration_form.fill(
        email=settings.test_user.email,
        username=settings.test_user.username,
        password=settings.test_user.password
    )
    registration_page.click_registration_button()

    context.storage_state(path=settings.browser_state_file)
    browser.close()

@pytest.fixture(scope='function', params=settings.browsers)
def browser_page_with_state(initialize_browser_state, 
                           request: SubRequest, 
                           playwright: Playwright) -> Generator[Page, None, None]:
    yield from initialize_playwright_page(
        playwright,
        test_name=request.node.name,
        browser_type=request.param,
        storage_state=settings.browser_state_file
    )