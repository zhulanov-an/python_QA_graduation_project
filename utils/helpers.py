from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def get_displayed_unique_element(browser, css):
    elements = WebDriverWait(browser, 10).until(
        EC.visibility_of_any_elements_located((By.CSS_SELECTOR, css))
    )
    assert len(elements) == 1
    return elements[0]