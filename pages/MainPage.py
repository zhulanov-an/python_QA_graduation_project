from pages.BasePage import BasePage
from pages.locators.MainPageLocators import MainPageLocators as locator


class MainPage(BasePage):
    def __init__(self, driver, url):
        super(MainPage, self).__init__(driver, url)

    @property
    def images_of_main_banner(self):
        return self._get_elements(locator.IMAGES_IN_MAIN_SLIDER)

    @property
    def featured_items(self):
        return self._get_elements(locator.FEATURED_ITEMS)

    @property
    def brand_pagination_items(self):
        return self._get_elements(locator.BRAND_PAGINATION_ITEMS)

    @property
    def main_pagination_items(self):
        return self._get_elements(locator.MAIN_PAGINATION_ITEMS)
