#   unittest
import unittest
#   selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
#   find_element
from selenium.webdriver.common.by import By


class Typos(unittest.TestCase):

    def setUp(self):
        # Installs the chrome driver (log_level=0: Disables teh log.info for the console)
        service = ChromeService(
            executable_path=ChromeDriverManager(log_level=0).install())
        self.driver = webdriver.Chrome(service=service)
        driver = self.driver
        driver.get('http://the-internet.herokuapp.com/')
        driver.find_element(By.LINK_TEXT, 'Typos').click()

    def test_typos(self):
        driver = self.driver
        #   Finds the text with the typo
        paragraph_to_check = driver.find_element(By.CSS_SELECTOR, '#content > div > p:nth-child(3)')
        #   Changes the type of the paragraph to text
        text_to_check = paragraph_to_check.text
        #   Verifies if text_to_check is the same as paragraph_to_check
        self.assertEqual(text_to_check, paragraph_to_check.text)

        tries = 1
        found = False
        correct_text = "Sometimes you'll see a typo, other times you won't."

        #*   Refreshes the page until it finds the correct text
        while text_to_check != correct_text:
            paragraph_to_check = driver.find_element(By.CSS_SELECTOR, '#content > div > p:nth-child(3)')
            text_to_check = paragraph_to_check.text
            driver.refresh()
            tries += 1

        #*   Refreshes the page until found equals TRUE
        while not found:
            if text_to_check == correct_text:
                found = True
                driver.refresh()
        #   Continues with the program when found is TRUE
        self.assertEqual(found, True)

        print(f'It took {tries} tries to find the typo')

    def tearDown(self):
        self.driver.implicitly_wait(3)
        self.driver.quit()


if __name__ == '__main__':
    unittest.main(verbosity=2)
