from playwright.async_api import Page

from constants.country import Country
from pages.blocks.simple_form.simple_form_elements import SimpleFormElements


class SimpleForm:
    def __init__(self, page: Page):
        self.elements = SimpleFormElements(page)

    def fill_data_into_form_fields_and_registry(self, username: str = None, password: str = None, email: str = None, country: Country = None) -> None:
        self.elements.username.fill(username)
        self.elements.password.fill(password)
        self.elements.email.fill(email)
        self.elements.country.select_option(country.value)

        self.elements.terms_checkbox.click()
        self.elements.register_button.click()

    def result_message(self):
        return self.elements.result_message.inner_text()