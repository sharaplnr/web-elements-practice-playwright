import pytest
from playwright.sync_api import Page, Playwright, BrowserContext, Browser


@pytest.fixture()
def page_init(playwright: Playwright):
    browser: Browser = playwright.chromium.launch(headless=False)
    context: BrowserContext = browser.new_context()
    page: Page = context.new_page()
    page.goto("https://aqa-proka4.org/sandbox/web#forms")

    yield page

    page.close()
    context.browser.close()

