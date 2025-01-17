import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

class SearchTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        driver = self.driver
        driver.implicitly_wait(30)
        driver.maximize_window()
        driver.get('http://demo-store.seleniumacademy.com/')
    
    def test_search_tee(self):
        driver = self.driver
        search_field = driver.find_element(By.NAME, 'q')
        search_field.clear()

        search_field.send_keys('tee')
        search_field.submit()

    def test_search_shaker(self):
        driver = self.driver
        search_field = driver.find_element(By.NAME, 'q')

        search_field.send_keys('salt shaker')
        search_field.submit()

        product = driver.find_elements(By.XPATH, '//*[@id="product-collection-image-389"]')
        self.assertEqual(1, len(product))

    
    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()