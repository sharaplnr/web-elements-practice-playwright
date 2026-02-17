from playwright.sync_api import Page

class SimpleFormElements:
    def __init__(self, page: Page):
        self.page = page

    @property
    def username(self):
        return self.page.locator("#username")

    @property
    def email(self):
        return self.page.locator("#email")

    @property
    def password(self):
        return self.page.locator("#password")

    @property
    def country(self):
        return self.page.locator("#country")

    @property
    def terms_checkbox(self):
        return self.page.locator("#terms")

    @property
    def register_button(self):
        return self.page.locator("#submitBtn")

    @property
    def result_message(self):
        return self.page.locator("#formResult")
