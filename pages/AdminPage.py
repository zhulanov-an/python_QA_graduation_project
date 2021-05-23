from pages.BasePage import BasePage
from pages.locators.AdminPageLocators import AdminPageLocators as locator


class AdminPage(BasePage):
    def __init__(self, driver, url):
        super(AdminPage, self).__init__(driver,
                                        url)

    @property
    def logout_link(self):
        return self._get_element(locator.LOGOUT)

    @property
    def profile(self):
        return self._get_element(locator.PROFILE)

    @property
    def left_menu_top_items(self):
        return self._get_elements(locator.MENU_TOP_ITEMS)

    @property
    def product_table(self):
        return self._get_element(locator.PRODUCT_TABLE)

    @property
    def product_table_headers(self):
        return self._get_elements(locator.COLUMNS_OF_HEAD_TABLE)

    def logout(self):
        self.logout_link.click()

    def move_to_item_in_left_menu_by_name(self, path_menu: str):
        raw_items = path_menu.split('>')
        for item in list(map(str.strip, raw_items)):
            xpath = f'//*[@id="menu"]//a[contains(text(), "{item}")]'
            find = {'xpath': xpath}
            el = self._wait_for_visible(find)
            el.click()
