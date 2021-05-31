import allure
import pytest
from pages.LoginPage import LoginPage


@allure.step('получение страницы авторизации')
@pytest.fixture
def login_page(browser, base_url):
    url = f"{base_url}/admin/"
    page = LoginPage(browser, url)
    page.open()
    return page


@allure.title('тест проверки логина')
def test_correct_login(login_page, admin):
    """проверка корректного логина"""
    user, password = admin
    admin_page = login_page.login(user, password)
    assert "common/logout" in admin_page.logout_link.get_attribute("href")
    assert admin_page.profile.text == "John Doe"


@allure.title('тест проверки некорректного логина')
def test_incorrect_login(login_page, wrong_user):
    """проверка некорректного логина"""
    user, password = wrong_user
    login_page.login(user, password)
    assert "No match for Username and/or Password." in login_page.notification.text
    assert login_page.input_username.is_displayed()
    assert login_page.input_password.is_displayed()
    assert login_page.button_login.is_displayed()
