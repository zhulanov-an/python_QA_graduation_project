import pytest
from pages.RegisterPage import RegisterPage


@pytest.fixture
def register_page(browser, base_url):
    url = base_url + "/index.php?route=account/register"
    page = RegisterPage(browser, url)
    page.open()
    return page


def test_register(register_page, browser):
    login, password = register_page.succesful_random_data_register()
    assert register_page.text_header == 'Your Account Has Been Created!'
