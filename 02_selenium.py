import unittest
from selenium import webdriver
import time

class TestMethods(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()


    def test_suite(self):
        driver = self.driver
        driver.get('https://www.wposs.com')

    def tearDown(self):
        time.sleep(15)
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
