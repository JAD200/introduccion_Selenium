import unittest
#   unittest
import unittest
#   selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
#   find_element
from selenium.webdriver.common.by import By


class RegisterNewUser(unittest.TestCase):

    def setUp(self):
        # Installs the chrome driver (log_level=0: Disables teh log.info for the console)
        service = ChromeService(executable_path=ChromeDriverManager(log_level=0).install())
        self.driver = webdriver.Chrome(service=service)
        driver = self.driver
        driver.implicitly_wait(30)
        driver.maximize_window()
        driver.get('http://demo-store.seleniumacademy.com/')

    def test_new_user(self):
        driver = self.driver
        driver.find_element(
            By.XPATH, '//*[@id="header"]/div/div[2]/div/a/span[2]').click()
        driver.find_element(By.LINK_TEXT, 'Log In').click()

        create_account_button = driver.find_element(
            By.XPATH, '//*[@id="login-form"]/div/div[1]/div[2]/a/span/span')
        self.assertTrue(
            create_account_button.is_displayed()
            and create_account_button.is_enabled)
        create_account_button.click()

        self.assertEqual('Create New Customer Account', driver.title)

        first_name = driver.find_element(By.ID, 'firstname')
        middle_name = driver.find_element(By.ID, 'middlename')
        last_name = driver.find_element(By.ID, 'lastname')
        email_address = driver.find_element(By.ID, 'email_address')
        news_letter_subscription = driver.find_element(
            By.ID, 'is_subscribed')
        password = driver.find_element(By.ID, 'password')
        confirm_password = driver.find_element(By.ID, 'confirmation')
        submit_button = driver.find_element(
            By.XPATH, '//*[@id="form-validate"]/div[2]/button/span/span')

        self.assertTrue(
            first_name.is_enabled()
            and middle_name.is_enabled()
            and last_name.is_enabled()
            and email_address.is_enabled()
            and news_letter_subscription.is_enabled()
            and password.is_enabled()
            and confirm_password.is_enabled()
            and submit_button.is_enabled()
        )

        first_name.send_keys('Test')
        middle_name.send_keys('User')
        last_name.send_keys('Register')
        email_address.send_keys('Test@test.com')
        password.send_keys('TEST')
        confirm_password.send_keys('TEST')
        submit_button.click()

    def tearDown(self):
        self.driver.implicitly_wait(3)
        self.driver.quit()


if __name__ == '__main__':
    unittest.main(verbosity=2)
