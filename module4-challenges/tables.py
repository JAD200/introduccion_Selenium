#   unittest
import unittest
#   selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
#   find_element
from selenium.webdriver.common.by import By


class Tables(unittest.TestCase):

    def setUp(self):
        # Installs the chrome driver (log_level=0: Disables teh log.info for the console)
        service = ChromeService(
            executable_path=ChromeDriverManager(log_level=0).install())
        self.driver = webdriver.Chrome(service=service)
        driver = self.driver
        driver.get('http://the-internet.herokuapp.com/')
        driver.find_element(By.LINK_TEXT, 'Sortable Data Tables').click()

    def test_sort_tables(self):
        driver = self.driver
        headers_quantity = 5
        rows_quantity = 4
        #   Empty table for the data
        table_data = [[] for i in range(headers_quantity)]
        print(table_data)
        #   Goes over all the headers
        for i in range(headers_quantity):
            header = driver.find_element(
                By.XPATH, f'//*[@id="table1"]/thead/tr/th[{i + 1}]/span')
            table_data[i].append(header.text)
        #   Goes over all the rows
            for j in range(rows_quantity):
                row_data = driver.find_element(
                    By.XPATH, f'//*[@id="table1"]/tbody/tr[{j + 1}]/td[{i + 1}]')  # {j +1} and {i + 1} is to sort the headers and rows
                table_data.append(row_data.text)

        print(table_data)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main(verbosity=2)
