#   unittest
import unittest
#   selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
#   Page Obejct
from google_page import GooglePage


class GoogleTest(unittest.TestCase):

    @classmethod
    def setUp(cls):
        # Installs the chrome driver (log_level=0: Disables teh log.info for the console)
        service = ChromeService(
            executable_path=ChromeDriverManager(log_level=0).install())
        cls.driver = webdriver.Chrome(service=service)

    def test_search(self):
        #   Defines google as the class GooglePage
        google = GooglePage(self.driver)
        #   Calls the open func
        google.open()
        #   Call  the search func
        google.search('Platzi')
        #   Ensures that the keyword send is correct
        self.assertEqual('Platzi', google.keyword)

    @classmethod
    def tearDown(cls):
        cls.driver.close()


if __name__ == '__main__':
    unittest.main(verbosity=2)
