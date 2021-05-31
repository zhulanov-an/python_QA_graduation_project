import pytest
from pages.RegisterPage import RegisterPage
import allure


@pytest.fixture
def register_page(browser, base_url):
    with allure.step('получение страницы регистрации клиента'):
        url = base_url + "/index.php?route=account/register"
        page = RegisterPage(browser, url)
        page.open()
    return page


@allure.title("Тест проверки регистрации клиента")
def test_register(register_page, browser):
    login, password = register_page.succesful_random_data_register()
    assert register_page.text_header == 'Our Account Has Been Created!'
    # assert register_page.text_header == 'Your Account Has Been Created!'
