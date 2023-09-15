from selenium.webdriver.common.by import *
from selenium import webdriver


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")



class LoginPageLocators():
    registration_form = (By.NAME, "registration_submit")
    login_form = (By.NAME, "login_submit")
