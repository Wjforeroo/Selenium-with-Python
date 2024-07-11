import unittest # Importa el módulo unittest para escribir y ejecutar pruebas unitarias.
from pyunitreport import HTMLTestRunner # Importa HTMLTestRunner para generar informes HTML de las pruebas.
from selenium import webdriver # Importa webdriver de Selenium para la automatización del navegador.
from selenium.webdriver.support.ui import Select # Importa Select para interactuar con elementos de selección en formularios web.
from selenium.webdriver.common.by import By # Importa By para seleccionar elementos por diferentes estrategias (ID, clase, etc.).
from selenium.webdriver.common.alert import Alert # Importa Alert para manejar alertas en Selenium.
import time
from selenium.webdriver.support.ui import WebDriverWait # Importa WebDriverWait para esperas explícitas.
from selenium.webdriver.support import expected_conditions as EC # Importa EC para condiciones esperadas en WebDriverWait.

class ExplicitWaitTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome() # Inicializa el driver de Chrome para controlar el navegador.
        driver = self.driver
        driver.get('http://demo-store.seleniumacademy.com/') # Abre la página de demostración del sitio Selenium Academy.

    def test_account_link(self):
        WebDriverWait(self.driver, 10).until(lambda s: s.find_element(By.ID, "select-language").get_attribute("length") =="3") # Espera explícita hasta que el elemento con ID "select-language" tenga un atributo "length" igual a "3".

        account = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.LINK_TEXT, 'ACCOUNT'))) # Espera explícita hasta que el enlace con texto 'ACCOUNT' sea visible y luego hace clic en él.
        account.click()

    def test_create_new_customer(self):
        self.driver.find_element(By.LINK_TEXT,('ACCOUNT')).click() # Hace clic en el enlace con texto 'ACCOUNT'.

        my_account = WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.LINK_TEXT, 'My Account')))# Espera explícita hasta que el enlace con texto 'My Account' sea visible y luego hace clic en él.
        my_account.click()

        create_account_button = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.LINK_TEXT, 'CREATE AN ACCOUNT'))) # Espera explícita hasta que el botón 'CREATE AN ACCOUNT' sea clickable y luego hace clic en él.
        create_account_button.click()

        WebDriverWait(self.driver, 10).until(EC.title_contains('Create New Customer Account'))  # Espera explícita hasta que el título de la página contenga 'Create New Customer Account'.

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main( verbosity=2 ) # Ejecuta todas las pruebas definidas en esta clase usando unittest y muestra detalles completos (verbosity=2).