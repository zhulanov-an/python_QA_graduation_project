from pages.BasePage import BasePage
from pages.locators.AccountLoginPageLocators import AccountLoginPageLocators as locator


class AccountLoginPage(BasePage):
    def __init__(self, driver, base_url):
        self.driver = driver
        self.url = base_url
        super(AccountLoginPage, self).__init__(self.driver,
                                               self.url)

    @property
    def button_continue(self):
        return self._get_element(locator.BUTTON_NEW_CUSTOMER_CONTINUE)

    @property
    def field_username_of_returned_customer(self):
        return self._get_element(locator.INPUT_EMAIL)

    @property
    def field_password_of_returned_customer(self):
        return self._get_element(locator.INPUT_PASSWORD)

    @property
    def button_login_of_returned_customer(self):
        return self._get_element(locator.BUTTON_LOGIN)

    @property
    def text_header_of_block_new_customer(self):
        return self._get_element_text(locator.HEADER_NEW_CUSTOMER)

    @property
    def text_header_of_block_returned_customer(self):
        return self._get_element_text(locator.HEADER_RETURNING_CUSTOMER)

    def login_returned_customer(self, name, password):
        self.field_username_of_returned_customer.send_keys(name)
        self.field_password_of_returned_customer.send_keys(password)
        self.button_login_of_returned_customer.click()
