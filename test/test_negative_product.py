from pages.base_page import BasePage
from pages.product_page import ProductPage
from pages.product_page import ProductPageLocators
import pytest

@pytest.mark.parametrize('link', [
        pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail),
        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        ])
class Testwork:
    def test_guest_cant_see_success_message_after_adding_product_to_basket(self, browser, link):
        page = ProductPage(browser, link)
        page.open()  # Открываем страницу товара
        page.add_basket()  # Добавляем товар в корзину
        page.should_not_be_success_message()  # Проверяем, что нет сообщения об успехе с помощью is_not_element_present

    def test_guest_cant_see_success_message(self, browser, link):
        page = ProductPage(browser, link)
        page.open()  # Открываем страницу товара
        page.should_not_be_success_message() # Проверяем, что нет сообщения об успехе с помощью is_not_element_present

    def test_message_disappeared_after_adding_product_to_basket(self, browser, link):
        page = ProductPage(browser, link)
        page.open()  # Открываем страницу товара
        page.add_basket()  # Добавляем товар в корзину
        page.success_message_is_disappeared() # Проверяем, что нет сообщения об успехе с помощью is_disappeared
