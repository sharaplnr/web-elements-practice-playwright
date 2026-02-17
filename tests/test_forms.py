import pytest

from playwright.sync_api import Page, Playwright, Browser, BrowserContext

from constants.country import Country
from pages.blocks.simple_form.simple_form import SimpleForm


class TestForm1:

    @pytest.mark.parametrize("username, email, password", [
        ("autotest", "test@test.ru", "qwerty"),
        (" ", " ", " "),
    ])
    def test_registry_form_with_valid_values(self, page_init, username, email, password):
        form1 = SimpleForm(page_init)

        form1.fill_data_into_form_fields_and_registry(username=username,
                                                      email=email,
                                                      password=password,
                                                      country=Country.RUSSIA)

        assert 'успешно' in form1.result_message()

    @pytest.mark.parametrize("username", ["", " ", f"{"t"*100}"])
    def test_invalid_username(self, username: str, playwright: Playwright):
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

        username_field.fill(username)
        email_field.fill("autotest@test.ru")
        password_field.fill("qwerty")
        country_field.select_option("ru")
        terms_checkbox.click()
        register_button.click()

        assert result_message.is_visible() is False

    def test_registry_without_checkbox(self, playwright: Playwright):
        browser: Browser = playwright.chromium.launch(headless=False)
        context: BrowserContext = browser.new_context()
        page: Page = context.new_page()
        page.goto("https://aqa-proka4.org/sandbox/web#forms")

        username_field = page.locator("#username")
        email_field = page.locator("#email")
        password_field = page.locator("#password")
        country_field = page.locator("#country")
        register_button = page.locator("#submitBtn")
        result_message = page.locator("#formResult")

        username_field.fill("autotest")
        email_field.fill("autotest@test.ru")
        password_field.fill("qwerty")
        country_field.select_option("ru")
        register_button.click()

        assert result_message.is_visible() is False


class TestForm2:

    @pytest.mark.parametrize("username, email, password", [
        ('admin', 'test@test.ru	', 'password123'),
        ('юзернейм', 'cp@ladogaspb.ru', 'Autotest2026!'),
        ('VeryLongUserName', 'user.name+alias@domain.co', '12345678aB'),
        ('12345', '1@2.ru', 'p4ssword'),
        ('USER_NAME', 'EMAIL@DOMAIN.COM', '9876543210zZ'),
    ])
    def test_registration_with_valid_values(self, playwright: Playwright, username: str, email: str, password: str):
        browser: Browser = playwright.chromium.launch(headless=True)
        context: BrowserContext = browser.new_context()
        page: Page = context.new_page()
        page.goto("https://aqa-proka4.org/sandbox/web#forms")

        username_field = page.locator("#val-username")
        email_field = page.locator("#val-email")
        password_field = page.locator("#val-password")
        confirm_password_field = page.locator("#val-confirm-password")
        submit_button = page.locator("#valSubmitBtn")

        username_field.fill(username)
        email_field.fill(email)
        password_field.fill(password)
        confirm_password_field.fill(password)
        submit_button.click()

        result_form = page.locator("#valFormResult")

        expected_text_in_form = 'проверки пройдены'

        assert expected_text_in_form in result_form.inner_text()

    @pytest.mark.parametrize("username, email, password", [
        ('shar', 'test.ru', 'pas1237'),
        ('', 'test', 'pass'),
        (' ', '', '1'),
    ])
    def test_registration_with_invalid_values(self, playwright: Playwright, username: str, email: str, password: str):
        browser: Browser = playwright.chromium.launch(headless=True)
        context: BrowserContext = browser.new_context()
        page: Page = context.new_page()
        page.goto("https://aqa-proka4.org/sandbox/web#forms")

        username_field = page.locator("#val-username")
        username_error_field = page.locator("#username-error")

        email_field = page.locator("#val-email")
        email_error_field = page.locator("#email-error")

        password_field = page.locator("#val-password")
        password_error_field = page.locator("#password-error")

        confirm_password_field = page.locator("#val-confirm-password")
        submit_button = page.locator("#valSubmitBtn")

        username_field.fill(username)
        email_field.fill(email)
        password_field.fill(password)
        confirm_password_field.fill(password)

        submit_button.click()

        assert username_error_field.is_visible()
        assert email_error_field.is_visible()
        assert password_error_field.is_visible()

        result_form = page.locator("#valFormResult")

        expected_text_in_form = 'содержит ошибки'

        assert expected_text_in_form in result_form.inner_text()



class TestForm3:

    def test_send_form_with_one_email_and_phone_number(self, playwright: Playwright):
        browser: Browser = playwright.chromium.launch(headless=False)
        context: BrowserContext = browser.new_context()
        page: Page = context.new_page()

        page.goto("https://aqa-proka4.org/sandbox/web#forms")
        username_field = page.locator("#dyn-name")
        email_blocks_first_input = page.locator("#emailFields").nth(0)
        phone_number_blocks_first_input = page.locator("#phoneFields").nth(0)
        submit_button = page.locator("#dynSubmitBtn")
        success_text = page.locator("#dynFormResult i")

        username_field.fill("Ilnur")
        email_blocks_first_input.fill("test@test.ru")
        phone_number_blocks_first_input.fill("+79991234567")
        submit_button.click()



        assert "успешно" in success_text.inner_text()

