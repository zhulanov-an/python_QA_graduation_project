import allure

from pages.AdminPage import AdminPage
from pages.BasePage import BasePage
from pages.locators import LoginPageLocators as locator


class LoginPage(BasePage):
    def __init__(self, driver, url):
        super(LoginPage, self).__init__(driver,
                                        url)

    @property
    def header(self):
        return self._get_element(locator.HEADER)

    @property
    def input_username(self):
        return self._get_element(locator.FIELD_USERNAME)

    @property
    def input_password(self):
        return self._get_element(locator.FIELD_PASSWORD)

    @property
    def button_login(self):
        return self._get_element(locator.BUTTON_LOGIN)

    @property
    def forgotten_password_link(self):
        return self._get_element(locator.LINK_FORGOTTEN_PASSWORD)

    @property
    def notification(self):
        return self._get_element(locator.NOTIFICATION)

    @allure.step("авторизация администратора")
    def login(self, username, password):
        self.input_username.send_keys(username)
        self.input_password.send_keys(password)
        self.button_login.click()
        return AdminPage(self.driver, None)