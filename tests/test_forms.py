import pytest

from playwright.sync_api import Page, Playwright, Browser, BrowserContext


class TestForm1:

    def test_valid_values(self, playwright: Playwright):
        browser: Browser = playwright.chromium.launch(headless=False)
        context: BrowserContext = browser.new_context()
        page: Page = context.new_page()

        page.goto("https://aqa-proka4.org/sandbox/web#forms")

        username_field = page.locator("#username")
        email_field = page.locator("#email")
        password_field = page.locator("#password")
        country_field = page.locator("#country")
        terms_checkbox = page.locator("#terms")
        register_button = page.locator("#submitBtn")
        result_message = page.locator("#formResult")

        username_field.fill("autotest")
        email_field.fill("autotest@test.ru")
        password_field.fill("qwerty")
        country_field.select_option("ru")
        terms_checkbox.click()
        register_button.click()

        assert 'успешно' in result_message.inner_text()





