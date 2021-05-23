from pages.BasePage import BasePage


class Search(BasePage):
    SEARCH_INPUT = {'css': '#search > input'}
    SEARCH_BUTTON = {'css': '#search > span > button'}

    def __init__(self, driver):
        super().__init__(driver)
