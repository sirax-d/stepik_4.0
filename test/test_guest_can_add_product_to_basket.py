import time
from pages.base_page import BasePage
from pages.product_page import ProductPage
from pages.product_page import ProductPageLocators
import pytest


class Testwork:
    @pytest.mark.parametrize('link', [
        pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail),
        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"
    ])
    def test_shop_basket(self, browser, link):
        page = ProductPage(browser, link)
        page.open()    # открываем страницу
        page.add_basket()
        page.solve_quiz_and_get_code()
        print("Сейчас мы тут")
        page.test_asserts()
        time.sleep(3)
