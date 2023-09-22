import time

from .base_page import BasePage
from selenium import *
from selenium.webdriver.common.by import By
from .base_page import BasePage
from .locators import ProductPageLocators





class ProductPage(BasePage):
    def test_asserts(self):
        # self.add_basket()
        self.item_name()
        self.price_book()
        self.should_not_be_success_message()

    def add_basket(self):
        assert self.is_element_present(*ProductPageLocators.ADD_ITEM), "No exist button add_basket"
        add_item = self.browser.find_element(*ProductPageLocators.ADD_ITEM)
        add_item.click()

    def item_name(self):
        time.sleep(3)
        book_name_main = self.browser.find_element(By.XPATH, '//*[@id="content_inner"]/article/div[1]/div[2]/h1')
        main_name = book_name_main.text
        name_book = self.browser.find_element(By.CSS_SELECTOR, "#messages > div:nth-child(1) > div > strong")
        item_name = name_book.text
        assert item_name == main_name, "Название книги не совпадает"

    def price_book(self):
        time.sleep(3)
        book_price_main = self.browser.find_element(By.XPATH, '//*[@id="content_inner"]/article/div[1]/div[2]/p[1]')
        main_price = book_price_main.text
        price_book = self.browser.find_element(By.XPATH, '//*[@id="messages"]/div[3]/div/p[1]/strong')
        text_price = price_book.text
        assert text_price == main_price, "Цена добавленного товара не соответствует указанной"


    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented, but should not be"

    def success_message_is_disappeared(self):
        assert self.success_message_is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), "Success message has not appeared"
