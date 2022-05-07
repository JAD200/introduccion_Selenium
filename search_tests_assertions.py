#   unittest
import unittest
#   selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


class SearchTest(unittest.TestCase):

    def setUp(self):
        # Installs the chrome driver (log_level=0: Disables teh log.info for the console)
        service = ChromeService(
            executable_path=ChromeDriverManager(log_level=0).install())
        self.driver = webdriver.Chrome(service=service)
        driver = self.driver
        driver.implicitly_wait(30)
        driver.maximize_window()
        driver.get('http://demo-store.seleniumacademy.com/')

    def test_search_tee(self):
        driver = self.driver
        search_field = driver.find_element_by_name('q')
        # limpia el campo de búsqueda en caso de que haya algún texto.
        search_field.clear()

        # simulamos la escritura del teclado para poner "tee"
        search_field.send_keys('tee')
        # envía los datos ('tee') para que la página muestre los resultados de "tee"
        search_field.submit()

    def test_search_salt_shaker(self):
        driver = self.driver
        search_field = driver.find_element_by_name('q')

        # escribimos 'salt shaker' en la barra de búsqueda
        search_field.send_keys('salt shaker')
        search_field.submit()  # enviamos la petición

        # hago una lista de los resultados buscando los elementos por su Xpath. Es la forma más rápida.
        products = driver.find_elements_by_xpath('//*[@id="top"]/body/div/div[2]/div[2]/div/div[2]/div[2]/div[3]/ul/li/div/h2/a')
        # vamos a preguntar si la cantidad de resultados es igual a 1
        self.assertEqual(1, len(products))

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main(verbosity=2)
