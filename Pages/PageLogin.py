import unittest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

class PageLogin(object):
    def __init__(self, driver):
        self.driver = driver
        self.username_box = (By.ID, "user-name")
        self.password_box = (By.ID, "password")
        self.login_btn = (By.ID, "login-button")

    def login(self, user_name, password):
        self.driver.find_element(*self.username_box).send_keys(user_name)
        self.driver.find_element(*self.password_box).send_keys(password)
        try:
            submit = WebDriverWait(self.driver, 3).until(expected_conditions.element_to_be_clickable(self.login_btn))
        except:
            print("Element is not clickable")
        self.driver.find_element(*self.login_btn).click()
        self.driver.implicitly_wait(5)

    def verify_login_page(self):
        title = self.driver.find_element_by_xpath("//span[@class='title']")
        tc = unittest.TestCase("__init__")
        tc.asserEqual(title, "Products")

