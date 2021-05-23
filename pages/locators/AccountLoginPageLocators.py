class AccountLoginPageLocators:
    BLOCK_NEW_CUSTOMER = {"css": "#content > div > div:nth-child(1) > div"}
    HEADER_NEW_CUSTOMER = {'css': BLOCK_NEW_CUSTOMER['css'] + " > h2"}
    BUTTON_NEW_CUSTOMER_CONTINUE = {'css': BLOCK_NEW_CUSTOMER['css'] + " > a"}

    BLOCK_RETURNING_CUSTOMER = {"css": "#content > div > div:nth-child(2) > div"}
    HEADER_RETURNING_CUSTOMER = {'css': BLOCK_RETURNING_CUSTOMER['css'] + " > h2"}

    INPUT_EMAIL = {"css": "#input-email"}
    INPUT_PASSWORD = {"css": "#input-password"}
    BUTTON_LOGIN = {"css": BLOCK_RETURNING_CUSTOMER['css'] + " > form > input"}
