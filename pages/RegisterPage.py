from selenium.webdriver.remote.webelement import WebElement
from faker import Faker
from pages.BasePage import BasePage
from pages.locators.RegisterPageLocators import RegisterPageLocators as locator


class RegisterPage(BasePage):
    def __init__(self, driver, url):
        super(RegisterPage, self).__init__(driver, url)

    @property
    def text_header(self) -> str:
        return self._get_element_text(locator.HEADER)

    @property
    def field_first_name(self) -> WebElement:
        return self._get_element(locator.FIRST_NAME_FIELD)

    @property
    def field_last_name(self) -> WebElement:
        return self._get_element(locator.LAST_NAME_FIELD)

    @property
    def field_email(self) -> WebElement:
        return self._get_element(locator.EMAIL_FIELD)

    @property
    def field_phone(self) -> WebElement:
        return self._get_element(locator.TELEPHONE_FIELD)

    @property
    def field_password(self) -> WebElement:
        return self._get_element(locator.PASSWORD_FIELD)

    @property
    def field_confirm_password(self) -> WebElement:
        return self._get_element(locator.CONFIRM_PASSWORD_FIELD)

    @property
    def radio_yes(self) -> WebElement:
        return self._get_element(locator.SUBSCRIBE_YES_RADIO)

    @property
    def radio_no(self) -> WebElement:
        return self._get_element(locator.SUBSCRIBE_NO_RADIO)

    @property
    def checkbox_privacy_policy(self) -> WebElement:
        return self._get_element(locator.PRIVACY_POLICY_CHECKBOX)

    @property
    def button_continue(self) -> WebElement:
        return self._get_element(locator.CONTINUE_BUTTON)

    @property
    def button_continue_after_register(self) -> WebElement:
        return self._get_element(locator.CONTINUE_AFTER_REGISTER_BUTTON)

    def _register(self,
                  first_name,
                  lastname,
                  email,
                  phone,
                  password,
                  confirm_password,
                  subsribe=False,
                  accept_policy=True):
        self.field_first_name.send_keys(first_name)
        self.field_last_name.send_keys(lastname)
        self.field_email.send_keys(email)
        self.field_phone.send_keys(phone)
        self.field_password.send_keys(password)
        self.field_confirm_password.send_keys(confirm_password)
        if subsribe:
            self.radio_yes.click()
        if accept_policy:
            self.checkbox_privacy_policy.click()
        self.button_continue.click()

    def successful_register(self,
                            first_name,
                            lastname,
                            email,
                            phone,
                            password):
        self._register(first_name, lastname, email, phone, password, password)

    def succesful_random_data_register(self):
        fake = Faker()
        first_name = fake.first_name()
        last_name = fake.last_name()
        email = fake.email()
        phone = fake.phone_number()
        password = fake.password()
        self.successful_register(first_name, last_name, email, phone, password)
        return email, password