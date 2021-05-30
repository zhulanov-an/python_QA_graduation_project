from pages.BasePage import BasePage
from pages.locators.RegisterPageLocators import RegisterPageLocators as locator


class ProductPage(BasePage):
    def __init__(self, driver, url):
        super(ProductPage, self).__init__(driver, url)

    @property
    def text_header(self):
        return self._get_element_text(locator.HEADER)

    @property
    def field_first_name(self):
        return self._get_elements(locator.FIRST_NAME_FIELD)

    @property
    def field_last_name(self):
        return self._get_elements(locator.LAST_NAME_FIELD)

    @property
    def field_email(self):
        return self._get_elements(locator.EMAIL_FIELD)

    @property
    def field_password(self):
        return self._get_elements(locator.PASSWORD_FIELD)

    @property
    def field_confirm_password(self):
        return self._get_elements(locator.CONFIRM_PASSWORD_FIELD)

    @property
    def radio_yes(self):
        return self._get_elements(locator.SUBSCRIBE_YES_RADIO)

    @property
    def radio_no(self):
        return self._get_elements(locator.SUBSCRIBE_NO_RADIO)

    @property
    def checkbox_privacy_policy(self):
        return self._get_elements(locator.PRIVACY_POLICY_CHECKBOX)

    @property
    def button_continue(self):
        return self._get_elements(locator.CONTINUE_BUTTON)
