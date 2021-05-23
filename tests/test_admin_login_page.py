import pytest
from pages.LoginPage import LoginPage


@pytest.fixture
def user_pass():
    return "user", "bitnami"


@pytest.fixture
def login_page(browser, base_url):
    url = base_url + "/admin/index.php?route=common/login"
    page = LoginPage(browser, url)
    page.open()
    return page


def test_browser_title_is_administration(login_page):
    """проверка заголовка страницы Administration в браузере"""
    assert "Administration" in login_page.title


def test_text_of_forms_header(login_page):
    """проверка отображения заголовка с текстом о вводе логина и пароля"""
    header = login_page.header
    assert header.is_displayed()
    assert header.text == "Please enter your login details."


def test_field_username(login_page):
    """проверка отображения поля ввода имени, пароля пользователя и кнопки авторизации"""
    field_username = login_page.input_username
    assert field_username.is_displayed()
    assert field_username.get_attribute("placeholder") == "Username"


def test_field_password(login_page):
    """проверка отображения поля ввода пароля пользователя"""
    field_password = login_page.input_password
    assert field_password.is_displayed()
    assert field_password.get_attribute("placeholder") == "Password"


def test_button_login(login_page):
    """проверка отображения кнопки авторизации пользователя"""
    button_login = login_page.button_login
    assert button_login.is_displayed()
    assert button_login.text == "Login"


def test_forgotten_password_link(login_page):
    """проверка отображения ссылки восстановления пароля"""
    forgotten_password_link = login_page.forgotten_password_link
    assert forgotten_password_link.is_displayed()
    assert forgotten_password_link.text == "Forgotten Password"

