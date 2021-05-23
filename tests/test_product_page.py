import pytest
from pages.ProductPage import ProductPage


@pytest.fixture
def product_page(browser, base_url):
    url = f"{base_url}/index.php?route=product/product&path=57&product_id=49"
    page = ProductPage(browser, url)
    page.open()
    return page


def test_browser_title_of_product(product_page):
    """проверка заголовка браузера на странице продукта"""
    assert product_page.title == "Samsung Galaxy Tab 10.1"


def test_header_of_page(product_page):
    """проверка отображения заголовка товара в странице продукта"""
    assert product_page.text_header_product == "Samsung Galaxy Tab 10.1"


@pytest.mark.parametrize("name, idx", [("Product Code:", 0), ("Reward Points:", 1), ("Availability:", 2)])
def test_features_of_product(product_page, name, idx):
    """проверка кода, премии, доступного количества продукта"""
    features = product_page.features_of_product
    assert name in features[idx].text


def test_ext_of_main_image(product_page):
    """проверка изображения продукта"""
    assert product_page.image_of_product.get_attribute("src").endswith(".jpg")


def test_price_of_product(product_page):
    """проверка цены продукта и валюты"""
    price = product_page.price_of_product
    currency = product_page.currency

    assert currency.text in price.text
    float_price = float(price.text.lstrip("$"))
    assert float_price > 0
