import unittest
import time
import random

from behave import Given, When, Then
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from ASTA.Locators.Locators import Locators


class ASTA_task1():

    def __init__(self, driver):
        self.driver = driver

    def open_details(self):
        details = self.driver.find_element_by_class_name(Locators.open_details)
        details.click()

        # return print (details.text)

    @Given("I added random product to basket")
    def add_product(self, number_of_items):
        locators = Locators(self.driver)
        input_locator, button_locator = locators.return_xpath()

        product = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, input_locator)))
        product.clear()
        product.send_keys(number_of_items)
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, button_locator))).click()

    def more_than_100(self):
        self.add_product("101")

    def close_alert(self):
        alert = self.driver.switch_to.alert
        msg = alert.text
        assert "Łączna ilość produktów w koszyku nie może przekroczyć 100." == msg
        alert.accept()

    def count_items(self):
        i = 0
        basket = 0
        while i < random.randint(1, 10):
            number_of_items = random.randint(1, 10)
            basket += number_of_items
            self.add_product(number_of_items)
            i += 1
            time.sleep(5)

        summary_quantity = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, Locators.summary_quantity))).text
        assert int(summary_quantity) == basket

    def reset_data(self):
        self.add_product('1')
        reset = self.driver.find_element_by_xpath(Locators.reset)
        reset.click()
        time.sleep(5)
        current_basket = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, Locators.summary_quantity))).text
        assert int(current_basket) == 0

    def delete_item(self):
        #self.reset_data()
        self.add_product('1')

        time.sleep(3)
        var = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//button[contains(text(),'Usuń')]")))
        var.click()
        time.sleep(3)
        summary_quantity = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, Locators.summary_quantity))).text
        assert int(summary_quantity) == 0

