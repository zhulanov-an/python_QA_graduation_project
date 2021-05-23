from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver, url):
        self._driver = driver
        self._url = url

    def open(self):
        self._driver.get(self._url)

    @property
    def driver(self):
        return self._driver

    @driver.setter
    def driver(self, driver):
        self._driver = driver

    @property
    def title(self):
        return self._driver.title

    def __elements(self, selector: dict, link_text: str = None):
        by = None
        if link_text:
            by = By.LINK_TEXT
        else:
            types_of_locator = list(map(str.lower, selector.keys()))
            if 'css' in types_of_locator:
                by = By.CSS_SELECTOR
                selector = selector['css']
            elif 'xpath' in types_of_locator:
                by = By.XPATH
                selector = selector['xpath']
        return self._driver.find_elements(by, selector)

    def __element(self, selector: dict, index: int, link_text: str = None):
        return self.__elements(selector, link_text)[index]

    def _click(self, selector, index=0):
        ActionChains(self._driver).move_to_element(self.__element(selector, index)).click().perform()

    def _input(self, selector, value, index=0):
        element = self.__element(selector, index)
        element.clear()
        element.send_keys(value)

    def _wait_for_visible(self, selector, link_text=None, index=0, wait=3):
        return WebDriverWait(self._driver, wait).until(EC.visibility_of(self.__element(selector, index, link_text)))

    def _get_element_text(self, selector, index=0):
        return self.__element(selector, index).text

    def _get_elements(self, selector, link_text=None):
        return self.__elements(selector, link_text)

    def _get_element(self, selector, link_text=None):
        return self.__element(selector, 0, link_text)
