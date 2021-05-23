class ProductPageLocators:
    BLOCK_PRODUCT = {'css': '#content > div > div.col-sm-4'}
    HEADER_OF_PRODUCT = {'css': BLOCK_PRODUCT['css'] + " > h1"}
    FEATURES_OF_PRODUCT = {'css': BLOCK_PRODUCT['css'] + " > ul:nth-child(3) > li"}
    IMG_PRODUCT = {'css': "#content > div > div.col-sm-8 > ul.thumbnails > li:nth-child(1) > a > img"}
    PRICE = {'css': BLOCK_PRODUCT['css'] + " > ul:nth-child(4) > li:nth-child(1) > h2"}
    CURRENCY = {'css': "#form-currency > div > button > strong"} #TODO нужно перенести в компонент TopMenu
