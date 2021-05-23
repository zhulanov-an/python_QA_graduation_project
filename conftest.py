import allure
import pytest
import logging
import os
from selenium.webdriver.support.events import EventFiringWebDriver, AbstractEventListener
from selenium import webdriver

LOG_FILE = '../logs/selenium.log'

if os.path.exists(LOG_FILE):
    os.remove(LOG_FILE)
    print("Logs removed")

logging.basicConfig(level=logging.DEBUG,
                    filename=LOG_FILE,
                    format='%(asctime)s.%(msecs)03d | %(levelname)s | %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S'
                    )
print('logging configured')


class CustomListener(AbstractEventListener):

    @allure.step
    def before_navigate_to(self, url, driver):
        super().before_navigate_to(url, driver)

    @allure.step
    def after_navigate_to(self, url, driver):
        super().after_navigate_to(url, driver)

    @allure.step
    def before_navigate_back(self, driver):
        super().before_navigate_back(driver)

    @allure.step
    def after_navigate_back(self, driver):
        super().after_navigate_back(driver)

    @allure.step
    def before_navigate_forward(self, driver):
        super().before_navigate_forward(driver)

    @allure.step
    def after_navigate_forward(self, driver):
        super().after_navigate_forward(driver)

    @allure.step
    def before_find(self, by, value, driver):
        super().before_find(by, value, driver)

    @allure.step
    def after_find(self, by, value, driver):
        super().after_find(by, value, driver)

    @allure.step
    def before_click(self, element, driver):
        super().before_click(element, driver)

    @allure.step
    def after_click(self, element, driver):
        super().after_click(element, driver)

    @allure.step
    def before_change_value_of(self, element, driver):
        super().before_change_value_of(element, driver)

    @allure.step
    def after_change_value_of(self, element, driver):
        super().after_change_value_of(element, driver)

    @allure.step
    def before_execute_script(self, script, driver):
        super().before_execute_script(script, driver)

    @allure.step
    def after_execute_script(self, script, driver):
        super().after_execute_script(script, driver)

    @allure.step
    def before_close(self, driver):
        super().before_close(driver)

    @allure.step
    def after_close(self, driver):
        super().after_close(driver)

    @allure.step
    def before_quit(self, driver):
        super().before_quit(driver)

    @allure.step
    def after_quit(self, driver):
        super().after_quit(driver)

    @allure.step
    def on_exception(self, exception, driver):
        super().on_exception(exception, driver)


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", choices=["chrome", "firefox", "opera"],
                     help="browser", required=True)
    parser.addoption("--bversion", action="store", help="version of browser")
    parser.addoption("--executor", action="store", help="address of executor", default="127.0.0.1")
    parser.addoption("--pexec", action="store", help="port of executor", default="4444")


@pytest.fixture
def base_url():
    return "https://demo.opencart.com"


@pytest.fixture
def browser(request):
    browser = request.config.getoption("--browser")
    bversion = request.config.getoption("--bversion")
    executor = request.config.getoption("--executor")
    pexec = request.config.getoption("--pexec")

    caps = {
        "browserName": browser,
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": False
        }
    }

    if bversion:
        caps["browserVersion"] = bversion

    driver = EventFiringWebDriver(webdriver.Remote(
        command_executor=f"http://{executor}:{pexec}/wd/hub/",
        desired_capabilities=caps
    ), CustomListener())

    test_name = request.node.name

    logger = logging.getLogger(f'Logger_of_{browser}_{driver.capabilities["browserVersion"]}')

    def close_browser():
        if driver is not None:
            driver.quit()
            logger.info(f'browser for {test_name} closed')
        logger.info(f'test {test_name} ended')

    request.addfinalizer(close_browser)

    driver.maximize_window()

    logger.info(f'browser for {test_name} opened')
    return driver
