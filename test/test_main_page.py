
import pytest
import time
from selenium.webdriver.common.by import By
from pages.main_page import MainPage
from pages.login_page import LoginPage

class MainPage(BasePage):
    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)



#
#
# class Test_work:
#     def test_guest_can_go_to_login_page(self, browser):
#         link = "http://selenium1py.pythonanywhere.com/"
#         page = MainPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
#         page.open()                      # открываем страницу
#         page.go_to_login_page()
#         login_page = LoginPage(browser, browser.current_url)
#         login_page.should_be_login_page()
#
#     def test_guest_should_see_login_link(self, browser):
#         link = "http://selenium1py.pythonanywhere.com/"
#         page = MainPage(browser, link)
#         page.open()
#         page.should_be_login_link()



    # def test_login_url(self, browser):
    #     link = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
    #     page = LoginPage(browser, link)
    #     page.open()
    #     page.should_be_login_page()
