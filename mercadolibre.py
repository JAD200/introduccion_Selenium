#   unittest
import unittest
#   selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
#   Find element
from selenium.webdriver.common.by import By

from time import sleep


class TestMercadoLibre(unittest.TestCase):

    def setUp(self):
        # Installs the chrome driver (log_level=0: Disables teh log.info for the console)
        service = ChromeService(
            executable_path=ChromeDriverManager(log_level=0).install())
        self.driver = webdriver.Chrome(service=service)
        driver = self.driver
        driver.get('https://mercadolibre.com/')
        driver.maximize_window()

    def test_search_ps4(self):
        driver = self.driver

        country = driver.find_element(By.ID, 'CO')
        country.click()

        cookies_accept_button = driver.find_element(
            By.CSS_SELECTOR, 'body > div:nth-child(7) > div.cookie-consent-banner-opt-out > div.cookie-consent-banner-opt-out__actions > button.cookie-consent-banner-opt-out__action.cookie-consent-banner-opt-out__action--primary.cookie-consent-banner-opt-out__action--key-accept')
        cookies_accept_button.click()

        search_field = driver.find_element(By.NAME, 'as_word')
        search_field.click()
        search_field.clear()
        search_field.send_keys('playstation 4')
        search_field.submit()
        sleep(3)

        location = driver.find_element(By.PARTIAL_LINK_TEXT, 'Bogotá D.C.')
        driver.execute_script("arguments[0].click();", location)
        sleep(3)

        condition = driver.find_element(By.PARTIAL_LINK_TEXT, 'Nuevo')
        condition.click()
        sleep(3)

        order_menu = driver.find_element(
            By.CLASS_NAME, 'andes-dropdown__standalone-arrow')
        order_menu.click()

        highest_price = driver.find_element(
            By.CSS_SELECTOR, '#andes-dropdown-más-relevantes-list-option-price_desc > div > div > span')
        highest_price.click()
        sleep(3)

        articles = []
        prices = []
        for i in range(5):
            article_name = driver.find_element(
                By.XPATH, f'//*[@id="root-app"]/div/div/section/ol/li[{i + 1}]/div/div/div[2]/div[1]/a/h2').text
            articles.append(article_name)

            article_price = driver.find_element(
                By.XPATH, f'//*[@id="root-app"]/div/div/section/ol/li[{i + 1}]/div/div/div[2]/div[2]/div[1]/div[1]/div/div/div/span[1]/span[2]/span[2]').text
            prices.append(article_price)

        print(f'\nArticulos: {articles}\nPrecios: {prices}' + '\n' * 2)

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main(verbosity=2)
