from selenium.webdriver.common.by import *
from selenium import webdriver


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")



class LoginPageLocators():
    registration_form = (By.NAME, "registration_submit")
    login_form = (By.NAME, "login_submit")

class ProductPageLocators():
    ADD_ITEM = (By.CSS_SELECTOR, ".btn.btn-lg.btn-primary.btn-add-to-basket")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > div > strong")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    LOGIN_PAGE_CHECK = (By.CSS_SELECTOR, '.btn.btn-lg.btn-primary')
