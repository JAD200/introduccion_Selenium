#   unittest
import unittest
#   selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
#   find_element
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AddRemoveElements(unittest.TestCase):

    def setUp(self):
        # Installs the chrome driver (log_level=0: Disables teh log.info for the console)
        service = ChromeService(
            executable_path=ChromeDriverManager(log_level=0).install())
        self.driver = webdriver.Chrome(service=service)
        driver = self.driver
        driver.get('http://the-internet.herokuapp.com/')
        driver.find_element(By.LINK_TEXT, 'Dynamic Controls').click()

    def test_dynamic_controls(self):
        driver = self.driver

        checkbox = driver.find_element(
            By.ID, 'checkbox')
        checkbox.click()

        remove_add_button = driver.find_element(
            By.CSS_SELECTOR, '#checkbox-example > button')
        remove_add_button.click()

        WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '#checkbox-example > button')))
        remove_add_button.click()

        enable_disable_button = driver.find_element(
            By.CSS_SELECTOR, '#input-example > button')
        enable_disable_button.click()

        WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '#input-example > button')))

        text_area = driver.find_element(
            By.CSS_SELECTOR, '#input-example > input[type=text]')
        text_area.send_keys('Platzi')

        enable_disable_button.click()

    def tearDown(self):
        self.driver.implicitly_wait(3)
        self.driver.quit()


if __name__ == '__main__':
    unittest.main(verbosity=2)
