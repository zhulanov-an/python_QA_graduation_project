import pytest
from pages.LoginPage import LoginPage


@pytest.fixture
def login_page(browser, base_url):
    url = f"{base_url}/admin/"
    page = LoginPage(browser, url)
    page.open()
    return page


@pytest.fixture
def right_user():
    return "user", "bitnami"


@pytest.fixture
def wrong_user():
    return "wrong", "wrong"


def test_correct_login(login_page, right_user):
    """проверка корректного логина"""
    user, password = right_user
    admin_page = login_page.login(user, password)
    assert "common/logout" in admin_page.logout_link.get_attribute("href")
    assert admin_page.profile.text == "John Doe"


def test_incorrect_login(login_page, wrong_user):
    """проверка некорректного логина"""
    user, password = wrong_user
    login_page.login(user, password)
    assert "No match for Username and/or Password." in login_page.notification.text
    assert login_page.input_username.is_displayed()
    assert login_page.input_password.is_displayed()
    assert login_page.button_login.is_displayed()
