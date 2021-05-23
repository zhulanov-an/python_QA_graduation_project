class TopMenuLocators:
    MAIN_HEADER = {'css': '# top > div'}
    BUTTON_CURRENCY = {'css': '# form-currency > div > button'}
    CURRENT_CURRENCY = {'css': BUTTON_CURRENCY['css'] + ' > strong'}

    CONTACT_US = {'css': '#top-links > ul > li:nth-child(1) > a > i'}
    MY_ACCOUNT_DROPDOWN = {'css': '#top-links > ul > li.dropdown > a > span.hidden-xs.hidden-sm.hidden-md'}
    REGISTER = {'css': '#top-links > ul > li.dropdown.open > ul > li:nth-child(1) > a'}
    LOGIN = {'css': '#top-links > ul > li.dropdown.open > ul > li:nth-child(2) > a'}
    WISH_LIST = {'css':'#wishlist-total > span'}
    SHOPPING_CART = {'css':'#top-links > ul > li:nth-child(4) > a > span'}
    CHECKOUT = {'css':'top-links > ul > li:nth-child(5) > a > span'}
