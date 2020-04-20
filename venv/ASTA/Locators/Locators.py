import unittest
import random
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class Locators():

    open_details = 'open-details'
    summary_quantity = 'summary-quantity'
    reset = '//*[@id="main-reset"]'

    def __init__(self, driver):
        self.driver = driver

    def return_product_list(self):
        products = []
        titles = WebDriverWait(self.driver, 5).until(EC.visibility_of_all_elements_located((By.XPATH, "//div[@class='caption']//h4")))
        for title in titles:
            products.append(title.text)
        return products

    def return_input(self, random_index):
        input = self.return_product_list()
        input_locator = "//h4[text()='" + input[random_index] + "']/following::input[1]"
        return input_locator

    def return_button(self, random_index):
        button = self.return_product_list()
        button_locator = "//h4[text()='" + button[random_index] + "']/following::button[1]"
        return button_locator

    def return_xpath(self):
        leng = len(self.return_product_list())
        random_index = random.randint(0, leng-1)

        input_locator = self.return_input(random_index)
        button_locator = self.return_button(random_index)

        return input_locator, button_locator