import unittest
from selenium.webdriver.support.ui import Select


class ItemsDropdown(object):

    def __init__(self, driver):
        self.driver = driver
        self.items_dropdown = Select(self.driver.find_element_by_xpath("//select[@class='product_sort_container']"))

    def select_item(self, text):
        tc = unittest.TestCase("__init__")
        tc.assertEqual(self.items_dropdown.first_selected_option.text.strip(), text)





