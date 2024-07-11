import unittest
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

class Tables(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        driver = self.driver
        driver.get('https://the-internet.herokuapp.com/')
        driver.find_element(By.LINK_TEXT, 'Sortable Data Tables').click()

    def test_sort_tables(self):
        driver = self.driver

        table_data = [[] for i in range(5)]
        print(table_data)

        for row in range (5):
            header = driver.find_element(By.XPATH, f'//*[@id="table1"]/thead/tr/th[{row + 1}]/span')
            table_data[row].append(header.text)

            for column in range (4):
                row_data = driver.find_element(By.XPATH, f'//*[@id="table1"]/tbody/tr[{column + 1}]/td[{row + 1}]')
                table_data[row].append(row_data.text)
        
        print(table_data)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main(verbosity=2)