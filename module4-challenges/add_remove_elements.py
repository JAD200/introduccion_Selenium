#   unittest
import unittest
#   selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
#   find_element
from selenium.webdriver.common.by import By
from time import sleep


class AddRemoveElements(unittest.TestCase):

    def setUp(self):
        # Installs the chrome driver (log_level=0: Disables teh log.info for the console)
        service = ChromeService(
            executable_path=ChromeDriverManager(log_level=0).install())
        self.driver = webdriver.Chrome(service=service)
        driver = self.driver
        driver.get('http://the-internet.herokuapp.com/')
        driver.find_element(By.LINK_TEXT, 'Add/Remove Elements').click()

    def test_add_remove(self):
        driver = self.driver

        elements_added = int(input('How many elements will you add? '))
        elements_remove = int(input('How many elements will you remove? '))
        total_elements = elements_added - elements_remove

        add_button = driver.find_element(
            By.XPATH, '//*[@id="content"]/div/button')

        sleep(3)

        for i in range(elements_added):
            add_button.click()

        for i in range(elements_remove):
            try:
                delete_button = driver.find_element(
                    By.CLASS_NAME, 'added-manually')
                delete_button.click()
            except:
                print('You are trying to delete more elements than the existent')
                break

        if total_elements > 0:
            print(f'There are {total_elements} elements on screen')
        else:
            print(f'There are 0 elements on screen')

        sleep(3)

    def tearDown(self):
        self.driver.implicitly_wait(3)
        self.driver.quit()


if __name__ == '__main__':
    unittest.main(verbosity=2)
