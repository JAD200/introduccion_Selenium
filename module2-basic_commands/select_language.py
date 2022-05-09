#   unittest
import unittest
#   selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
#   find_element
from selenium.webdriver.common.by import By
#   Manipulate the dropdown menu
from selenium.webdriver.support.ui import Select


class SelectLanguageOptions(unittest.TestCase):

    def setUp(self):
        # Installs the chrome driver (log_level=0: Disables teh log.info for the console)
        service = ChromeService(
            executable_path=ChromeDriverManager(log_level=0).install())
        self.driver = webdriver.Chrome(service=service)
        driver = self.driver
        driver.implicitly_wait(30)
        driver.maximize_window()
        driver.get('http://demo-store.seleniumacademy.com/')

    def test_select_language(self):
        # List to check available languages
        exp_options = ['English', 'French', 'German']
        # Store the options to choose
        act_options = []
        # Access the dropdown selection
        select_language = Select(self.driver.find_elements_by_id('select-language'))
        # To check the correct amount of languages
        # '.options' allows the introduction to the dropdown options
        self.assertEqual(3, len(select_language.options))

        for option in select_language.options:
            act_options.append(option.text)

        # verifico que la lista de opciones disponibles y activas sean idénticas
        self.assertListEqual(exp_options, act_options)

        # Checks if word "English" it's the first option selected
        self.assertEqual('English', select_language.first_selected_option.text)

        # Selects 'German' by the visible text
        select_language.select_by_visible_text('German')

        # Verifies if the website is in German
        # Asking Selenium if the url contains the next words 'store=german'
        self.assertTrue('store=german' in self.driver.current_url)

        select_language = Select(
            self.driver.find_elements_by_id('select-language'))
        select_language.select_by_index(0)

    def tearDown(self):
        self.driver.implicitly_wait(3)
        self.driver.quit()


if __name__ == '__main__':
    unittest.main(verbosity=2)
