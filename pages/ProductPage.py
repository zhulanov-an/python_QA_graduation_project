from pages.BasePage import BasePage
from pages.locators.ProductPageLocators import ProductPageLocators as locator


class ProductPage(BasePage):
    def __init__(self, driver, url):
        super(ProductPage, self).__init__(driver, url)

    @property
    def text_header_product(self):
        return self._get_element_text(locator.HEADER_OF_PRODUCT)

    @property
    def features_of_product(self):
        return self._get_elements(locator.FEATURES_OF_PRODUCT)

    @property
    def image_of_product(self):
        return self._get_element(locator.IMG_PRODUCT)

    @property
    def price_of_product(self):
        return self._get_element(locator.PRICE)

    @property
    def currency(self):
        return self._get_element(locator.CURRENCY)
