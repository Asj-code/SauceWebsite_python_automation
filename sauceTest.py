import unittest
from selenium import webdriver
from Pages.PageLogin import *
from Pages.ItemDropdown import *


class SauceTest(unittest.TestCase):
    def setUp(self):
        path = "Drivers/chromedriver"
        self.driver = webdriver.Chrome(path)
        self.driver.get("https://www.saucedemo.com/")
        self.page_login = PageLogin(self.driver)
        self.page_login.login("standard_user", "secret_sauce")
        self.item_dropdown = ItemsDropdown(self.driver)

    def test_select_item(self):
        self.item_dropdown.select_item("Name (A to Z)")

    def tearDown(self):
        self.driver.quit()
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
