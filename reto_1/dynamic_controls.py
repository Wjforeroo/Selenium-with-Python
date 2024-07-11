import unittest # Importa el módulo unittest para pruebas unitarias
from selenium import webdriver # Importa la clase webdriver del módulo selenium
from selenium.webdriver.common.by import By # Importa la estrategia de selección By del módulo selenium
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class DynamicControls(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        driver = self.driver
        driver.get('https://the-internet.herokuapp.com/')
        time.sleep(2)
        driver.find_element(By.LINK_TEXT, 'Dynamic Controls').click()
        time.sleep(2)

    def test_dynamic_controls(self):
        driver = self.driver

        checkbox = driver.find_element(By.CSS_SELECTOR, '#checkbox > input[type=checkbox]')
        checkbox.click()

        remove_add_button = driver.find_element(By.CSS_SELECTOR, '#checkbox-example > button')
        remove_add_button.click

        WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#checkbox-example > button')))
        remove_add_button.click()

        enable_disable_button = driver.find_element(By.CSS_SELECTOR, '#input-example > button')
        enable_disable_button.click()
        WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#input-example > input[type=text]')))
        text_area = driver.find_element(By.CSS_SELECTOR, '#input-example > input[type=text]')
        text_area.send_keys('Platzi')

        enable_disable_button.click()
        



        
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main(verbosity=2)