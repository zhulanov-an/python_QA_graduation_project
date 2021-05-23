class FooterLocators:
    FOOTER = {'css': 'body > footer'}

    INFORMATION_COLUMN = {'css': FOOTER['css'] + ' > div > div > div:nth-child(1) > ul'}
    ABOUT_US = {'css': INFORMATION_COLUMN['css'] + ' > li:nth-child(1) > a'}
    DELIVERY_INFORMATION = {'css': INFORMATION_COLUMN['css'] + ' > li:nth-child(2) > a'}
    PRIVACY_POLICY = {'css': INFORMATION_COLUMN['css'] + ' > li:nth-child(3) > a'}
    TERMS_CONDITIONS = {'css': INFORMATION_COLUMN['css'] + ' > li:nth-child(4) > a'}

    CUSTOMER_SERVICE_COLUMN = {'css': FOOTER['css'] + ' > div > div > div:nth-child(2) > ul'}
    CONTACT_US = {'css': CUSTOMER_SERVICE_COLUMN['css'] + ' > li:nth-child(1) > a'}
    RETURNS = {'css': CUSTOMER_SERVICE_COLUMN['css'] + ' > li:nth-child(2) > a'}
    SITE_MAP = {'css': CUSTOMER_SERVICE_COLUMN['css'] + ' > li:nth-child(3) > a'}

    EXTRAS_COLUMN = {'css': FOOTER['css'] + ' > div > div > div:nth-child(3) > ul'}
    BRANDS = {'css': EXTRAS_COLUMN['css'] + ' > li:nth-child(1) > a'}
    GIFT = {'css': EXTRAS_COLUMN['css'] + ' > li:nth-child(2) > a'}
    CERTIFICATES = {'css': EXTRAS_COLUMN['css'] + ' > li:nth-child(3) > a'}
    AFFILIATE = {'css': EXTRAS_COLUMN['css'] + ' > li:nth-child(4) > a'}
    SPECIALS = {'css': EXTRAS_COLUMN['css'] + ' > li:nth-child(5) > a'}

    MY_ACCOUNT_COLUMN = {'css': FOOTER['css'] + ' > div > div > div:nth-child(4) > ul'}
    MY_ACCOUNT = {'css': MY_ACCOUNT_COLUMN['css'] + ' > li:nth-child(1) > a'}
    ORDER = {'css': MY_ACCOUNT_COLUMN['css'] + ' > li:nth-child(2) > a'}
    HISTORY = {'css': MY_ACCOUNT_COLUMN['css'] + ' > li:nth-child(3) > a'}
    WISHLIST = {'css': MY_ACCOUNT_COLUMN['css'] + ' > li:nth-child(4) > a'}
    NEWSLETTER = {'css': MY_ACCOUNT_COLUMN['css'] + ' > li:nth-child(5) > a'}

    COPYRIGHT = {'css': 'body > footer > div > p'}
