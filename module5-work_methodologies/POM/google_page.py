from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class GooglePage(object):
    def __init__(self, driver):
        #   The driver and the url are "private", the search_locator isn't
        self._driver = driver
        self._url = 'http://google.com'
        self.search_locator = 'q'

    #   Makes sure the search_locator is available
    @property
    def is_loaded(self):
        WebDriverWait(self._driver, 10).until(
            EC.presence_of_element_located((By.NAME, 'q')))
        return True

    #   Gets the keyword for the search bar
    @property
    def keyword(self):
        _input_field = self._driver.find_element(By.NAME, 'q')
        return _input_field.get_attribute('value')

    #*   Opens the url
    def open(self):
        self._driver.get(self._url)

    #   Writes the keyword in the search bar
    def type_search(self, keyword):
        _input_field = self._driver.find_element(By.NAME, 'q')
        _input_field.send_keys(keyword)

    #   Submits the data
    def click_submit(self):
        _input_field = self._driver.find_element(By.NAME, 'q')
        _input_field.submit()

    #*   Combines all the actions and executes them
    def search(self, keyword):
        self.type_search(keyword)
        self.click_submit()
