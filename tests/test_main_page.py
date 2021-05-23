import pytest
from pages.MainPage import MainPage


@pytest.fixture
def mainpage(browser, base_url):
    page = MainPage(browser, base_url)
    page.open()
    return page


def test_browser_title(mainpage):
    """проверка заголовка главной страницы"""
    assert "Your Store" in mainpage.title


def test_images_of_main_banner_have_ext_jpg(mainpage):
    """проверка наличия изображений с расширением jpg"""
    images = mainpage.images_of_main_banner
    for image in images:
        src = image.get_attribute('src')
        assert src.endswith('.jpg'), f'invalid ext of image: {src}'


def test_count_elements_of_featured_row_equal_four(mainpage):
    """проверка количества блоков в главном баннере"""
    items = mainpage.featured_items
    assert len(items) == 4


def test_count_of_main_pagination_items_equal_two(mainpage):
    """проверка количества изображений в главном пагинаторе"""
    items = mainpage.main_pagination_items
    assert len(items) == 2


def test_count_of_brand_pagination_items_equal_twelve(mainpage):
    """проверка количества брендов в пагинаторе"""
    items = mainpage.brand_pagination_items
    assert len(items) == 11
