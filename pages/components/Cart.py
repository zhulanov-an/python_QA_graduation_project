from pages.BasePage import BasePage


class Cart(BasePage):
    SEARCH_BUTTON = {'css': '#cart > button'}

    def __init__(self, driver):
        super().__init__(driver)
