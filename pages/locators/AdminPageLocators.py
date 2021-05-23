class AdminPageLocators:
    LOGOUT = {'css': '#header > div > ul > li:nth-child(2) > a'}
    PROFILE = {'css': '#header > div > ul > li.dropdown > a'}
    MENU_TOP_ITEMS = {'css': '#menu > li > a'}
    PRODUCT_TABLE = {'css': '#form-product > div > table'}
    COLUMNS_OF_HEAD_TABLE = {'css': PRODUCT_TABLE['css'] + '> thead > tr > td'}