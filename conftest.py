import allure
import pytest
import logging
from selenium.webdriver.support.events import EventFiringWebDriver, AbstractEventListener
from selenium import webdriver

LOG_FILE = './logs/selenium.log'

logging.basicConfig(level=logging.CRITICAL,
                    filename=LOG_FILE,
                    format='%(asctime)s.%(msecs)03d | %(levelname)s | %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S'
                    )
print('logging configured')


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
# https://github.com/pytest-dev/pytest/issues/230#issuecomment-402580536
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    if rep.outcome != 'passed':
        item.status = 'failed'
    else:
        item.status = 'passed'


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

    @allure.step("браузер закрыт")
    def after_quit(self, driver):
        super().after_quit(driver)

    @allure.step("произошла ошибка {exception}")
    def on_exception(self, exception, driver):
        super().on_exception(exception, driver)


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", choices=["chrome", "firefox", "opera"],
                     help="browser", default='firefox')
    parser.addoption("--bversion", action="store", help="version of browser", default='85.0')
    parser.addoption("--target", action="store", help="address of testing resource", default="192.168.1.104")
    parser.addoption("--executor", action="store", help="address of executor", default="192.168.1.104")
    parser.addoption("--pexec", action="store", help="port of executor", default="4444")
    parser.addoption("--local", action="store_true")


@pytest.fixture
def base_url(request):
    target = f"http://{request.config.option.target}"
    with allure.step(f'базовый адрес "{target}"'):
        return target


# @allure.step('конфигурация браузера')
@pytest.fixture
def browser(request):
    browser = request.config.option.browser
    bversion = request.config.option.bversion
    executor = request.config.option.executor
    pexec = request.config.option.pexec
    local = request.config.option.local

    def close_browser():
        test_name = request.node.name
        if request.node.status == 'failed':
            allure.attach(
                name=driver.session_id,
                body=driver.get_screenshot_as_png(),
                attachment_type=allure.attachment_type.PNG
            )
        driver.quit()
        logger.info(f'browser for {test_name} closed')
        logger.info(f'test {test_name} ended')

    if local:
        if browser == "chrome":
            options = webdriver.ChromeOptions()
            options.add_argument("--ignore-certificate-errors")
            driver = webdriver.Chrome(options=options)
        elif browser == "firefox":
            options = webdriver.FirefoxOptions()
            options.accept_insecure_certs = True
            driver = webdriver.Firefox(options=options)
        else:
            raise NotImplementedError

        logger = logging.getLogger(f'Logger_of_{browser}_{driver.capabilities["browserVersion"]}')

        request.addfinalizer(close_browser)
        driver.maximize_window()
        driver.implicitly_wait(5)
        return driver

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

    request.addfinalizer(close_browser)

    driver.maximize_window()

    logger.info(f'browser for {test_name} opened')
    return driver


@allure.step('получение данных администратора opencart')
@pytest.fixture
def admin():
    return "user", "bitnami"


@allure.step('получение данных некорректного клиента')
@pytest.fixture
def wrong_user():
    return "wrong", "wrong"
