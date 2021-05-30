class RegisterPageLocators:
    HEADER = {'css': '#content > h1'}
    FIRST_NAME_FIELD = {'css': '#input-firstname'}
    LAST_NAME_FIELD = {'css': '#input-lastname'}
    EMAIL_FIELD = {'css': '#input-email'}
    TELEPHONE_FIELD = {'css': '#input-telephone'}
    PASSWORD_FIELD = {'css': '#input-password'}
    CONFIRM_PASSWORD_FIELD = {'css': '#input-confirm'}
    SUBSCRIBE_YES_RADIO = {'css': '#content > form > fieldset:nth-child(3) > div > div > label:nth-child(1) > input[type=radio]'}
    SUBSCRIBE_NO_RADIO = {'css': '#content > form > fieldset:nth-child(3) > div > div > label:nth-child(2) > input[type=radio]'}
    PRIVACY_POLICY_CHECKBOX = {'css': '#content > form > div > div > input[type=checkbox]:nth-child(2)'}
    CONTINUE_BUTTON = {'css': '#content > form > div > div > input.btn.btn-primary'}
