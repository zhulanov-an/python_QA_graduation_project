import pytest

from pages.AdminPage import AdminPage
from pages.LoginPage import LoginPage


@pytest.fixture
def right_user():
    return "user", "bitnami"


@pytest.fixture
def product_page(base_url, admin, browser):
    url = f"{base_url}/admin/"
    login_page = LoginPage(browser, url)
    login_page.open()
    login_page.login(*admin)
    admin_page = AdminPage(browser, None)
    admin_page.move_to_item_in_left_menu_by_name('Catalog > Products')
    return admin_page


def test_title_of_product(product_page):
    """проверка заголовка страницы"""
    assert product_page.title == 'Products'


def test_count_of_column(product_page):
    """проверка количества колонок в таблице товаров"""
    assert len(product_page.product_table_headers) == 8


def test_name_column_of_products_table(product_page):
    """проверка наименования колонок в таблице"""
    names = ["Image", "Product Name", "Model", "Price", "Quantity", "Status", "Action"]
    for idx, col in enumerate(product_page.product_table_headers[1:]):
        assert names[idx] in col.text
