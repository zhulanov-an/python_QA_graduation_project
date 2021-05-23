class MainMenuLocators:
    MENU = {'css': '#menu > div.collapse.navbar-collapse.navbar-ex1-collapse > ul'}
    DESKTOPS = {'css': MENU['css'] + ' > li:nth-child(1) > a'}
    LAPTOPS = {'css': MENU['css'] + ' > li:nth-child(2) > a'}
    COMPONENTS = {'css': MENU['css'] + ' > li:nth-child(3) > a'}
    TABLETS = {'css': MENU['css'] + ' > li:nth-child(4) > a'}
    SOFTWARE = {'css': MENU['css'] + ' > li:nth-child(5) > a'}
    PHONES = {'css': MENU['css'] + ' > li:nth-child(6) > a'}
    CAMERAS = {'css': MENU['css'] + ' > li:nth-child(7) > a'}
    MP3PLAYERS = {'css': MENU['css'] + ' > li:nth-child(8) > a'}
