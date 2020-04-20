import unittest
import time
import HtmlTestRunner
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from ASTA.Pages.Page_Task1 import ASTA_task1


class test_task1(unittest.TestCase):

    @classmethod
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    def test_open_task(self):
        driver = self.driver
        driver.get('https://buggy-testingcup.pgs-soft.com/task_1')

        open_details = ASTA_task1(driver)
        open_details.open_details()
        #time.sleep(5)

    def test_more_than_100(self):
        driver = self.driver
        driver.get('https://buggy-testingcup.pgs-soft.com/task_1')

        for_test = ASTA_task1(driver)
        for_test.more_than_100()
        for_test.close_alert()

    def test_count_items(self):
        driver = self.driver
        driver.get('https://buggy-testingcup.pgs-soft.com/task_1')

        for_test = ASTA_task1(driver)
        for_test.count_items()

    def test_delete_from_basket(self):
        driver = self.driver
        driver.get('https://buggy-testingcup.pgs-soft.com/task_1')

        for_test = ASTA_task1(driver)
        for_test.delete_item()

    def test_reset(self):
        driver = self.driver
        driver.get('https://buggy-testingcup.pgs-soft.com/task_1')

        for_test = ASTA_task1(driver)
        for_test.reset_data()
        #time.sleep(5)

    @classmethod
    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:/Users/Warpath/PycharmProjects/allegro_tests/venv/ASTA/Reports'))
