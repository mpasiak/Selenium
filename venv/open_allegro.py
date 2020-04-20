import time

from selenium import webdriver

chrome_browser = webdriver.Chrome()
url = "https://buggy-testingcup.pgs-soft.com/"

chrome_browser.get(url)
time.sleep(3)

link = chrome_browser.find_element_by_link_text("Zadanie 1")
link.click()