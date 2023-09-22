import time
from pages.base_page import BasePage
from pages.product_page import ProductPage
from pages.product_page import ProductPageLocators
from pages.login_page import LoginPage
import pytest

@pytest.mark.parametrize('link', [
        pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail),
        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
        # "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
        # "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
        # "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
        # "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
        # "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
        # "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
        # "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
        # "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
        # "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"
    ])
class Testwork:

    # def test_shop_basket(self, browser, link):
    #     page = ProductPage(browser, link)
    #     page.open()    # открываем страницу
    #     page.add_basket()
    #     page.solve_quiz_and_get_code()
    #     print("Сейчас мы тут")
    #     page.test_asserts()
    #     time.sleep(3)

    def test_guest_should_see_login_link_on_product_page(self, browser, link):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        page = ProductPage(browser, link)
        page.open()
        page.should_be_login_link()


    def test_guest_can_go_to_login_page_from_product_page(self, browser, link):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        page = LoginPage(browser, link)
        page.open()
        page.go_to_login_page()
        page.should_be_login_page()



