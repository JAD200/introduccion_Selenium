#   unittest
import unittest
#   selenium
from selenium import webdriver
#   Exception for the asserts when we validate an element presence
from selenium.common.exceptions import NoSuchElementException
#   Helps to call the exceptions we want to validate
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


class AssertionsTests(unittest.TestCase):

    def setUp(self):
        # Installs the chrome driver (log_level=0: Disables the log.info for the console)
        service = ChromeService(
            executable_path=ChromeDriverManager(log_level=0).install())
        self.driver = webdriver.Chrome(service=service)
        driver = self.driver
        driver.implicitly_wait(30)
        driver.maximize_window()
        driver.get('http://demo-store.seleniumacademy.com/')

    def test_search_field(self):
        #*  This is the same as this: search_field = driver.find_element_by_name('q')
        self.assertTrue(self.is_element_present(By.NAME, 'q'))

    def test_language_option(self):
        #*  This is the same as this: search_field = driver.find_element_by_id('select-language')
        self.assertTrue(self.is_element_present(By.ID, 'select-language'))

    def tearDown(self):
        self.driver.quit()

    #*   To know if the elements is present
        ##  how: selector type
        ##  what: its value
    def is_element_present(self, how, what):
        #   Searches the elements by parameter
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as variable:
            return False
        return True


if __name__ == '__main__':
    unittest.main(verbosity=2)
