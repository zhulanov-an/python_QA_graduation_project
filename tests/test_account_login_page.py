import allure
import pytest
from pages.AccountLoginPage import AccountLoginPage


@pytest.fixture
def account_login_page(browser, base_url):
    url = base_url + '/index.php?route=account/login'
    page = AccountLoginPage(browser, url)
    page.open()
    return page


@allure.title('Тест проверки заголовка браузера')
def test_browser_title_is_account_login(account_login_page):
    """проверка заголовка страницы Account Login в браузере"""
    assert "Account Login" in account_login_page.title


@allure.title('Тест проверки заголовка блока регистрации нового клиента')
def test_header_of_block_new_customer(account_login_page):
    """проверка наличия заголовка в блоке new customer"""
    assert account_login_page.text_header_of_block_new_customer == "New Customer"


@allure.title('Тест проверки заголовка блока регистрации зарегестрированного клиента')
def test_header_of_block_returning_customer(account_login_page):
    """проверка наличия заголовка в блоке Returning Customer"""
    assert account_login_page.text_header_of_block_returned_customer == "Returning Customer"


@allure.title('Тест проверки наличия кнопки в блоке регистрации нового клиента')
def test_button_continue_in_block_new_customer(account_login_page):
    assert account_login_page.button_continue.text == "Continue"
    assert account_login_page.button_continue.get_attribute("href").endswith("register")


@allure.title('Тест полей имени и пароля клиента и кнопки авторизации')
def test_inputs_in_block_returning_customer(account_login_page):
    """проверка полей имени и пароля клиента и кнопки авторизации"""
    input_email = account_login_page.field_username_of_returned_customer
    input_password = account_login_page.field_password_of_returned_customer
    button_login = account_login_page.button_login_of_returned_customer

    assert input_email.get_attribute("placeholder") == "E-Mail Address"
    assert input_password.get_attribute("placeholder") == "Password"
    assert button_login.get_attribute("value") == "Login"
    assert button_login.get_attribute("type") == "submit"
