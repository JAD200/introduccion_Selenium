import unittest
#   unittest
import unittest
#   selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
#   find_element
from selenium.webdriver.common.by import By


class CompareProducts(unittest.TestCase):

    def setUp(self):
        # Installs the chrome driver (log_level=0: Disables teh log.info for the console)
        service = ChromeService(
            executable_path=ChromeDriverManager(log_level=0).install())
        self.driver = webdriver.Chrome(service=service)
        driver = self.driver
        driver.implicitly_wait(30)
        driver.maximize_window()
        driver.get('http://demo-store.seleniumacademy.com/')

    def test_compare_products_removal_alert(self):
        driver = self.driver
        search_field = driver.find_element(By.NAME, 'q')
        #   Cleaning the search_fields is a good practice
        search_field.clear()

        search_field.send_keys('tee')
        search_field.submit()

        driver.find_element(By.CLASS_NAME, 'link-compare').click()
        driver.find_element(By.LINK_TEXT, 'Clear All').click()

        #   Variable to interact with the pop-up
        alert = driver.switch_to_alert()
        #   Extracts the text shown
        alert_text = alert.text

        #   Verifies the text from the alert
        self.assertEqual(
            'Are you sure you would like to remove all products from your comparison?', alert_text)

        alert.accept()

    def tearDown(self):
        self.driver.implicitly_wait(3)
        self.driver.quit()


if __name__ == '__main__':
    unittest.main(verbosity=2)
