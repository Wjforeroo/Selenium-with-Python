import unittest # Importa el módulo unittest para escribir y ejecutar pruebas unitarias.
from pyunitreport import HTMLTestRunner # Importa HTMLTestRunner para generar informes HTML de las pruebas.
from selenium import webdriver # Importa webdriver de Selenium para la automatización del navegador.
from selenium.webdriver.support.ui import Select # Importa Select para interactuar con elementos de selección en formularios web.
from selenium.webdriver.common.by import By # Importa By para seleccionar elementos por diferentes estrategias (ID, clase, etc.).
from selenium.webdriver.common.alert import Alert # Importa Alert para manejar alertas en Selenium.
import time

class NavigationTest(unittest.TestCase):

    def setUp(self):
        # Configuración inicial antes de cada prueba

        self.driver = webdriver.Chrome() # Inicializa el driver de Chrome para controlar el navegador.
        driver = self.driver
        driver.maximize_window() # Maximiza la ventana del navegador.
        driver.get('https://google.com') # Abre la página de Google.

    def test_browser_navigation(self):
        # Prueba de navegación del navegador
        
        driver = self.driver
        search_field = driver.find_element(By.NAME,"q") # Encuentra el campo de búsqueda en Google por su nombre.
        search_field.clear() # Borra cualquier texto existente en el campo de búsqueda.
        search_field.send_keys("Platzi") # Envía las teclas "Platzi" al campo de búsqueda.
        search_field.submit() # Envía el formulario de búsqueda.

        driver.back() # Navega hacia atrás en la historia de navegación.
        
        driver.forward() # Navega hacia adelante en la historia de navegación.
        
        driver.refresh() # Actualiza la página actual.
        

    def tearDown(self):
        # Limpieza posterior a cada prueba
        self.driver.quit() # Cierra el navegador y libera los recursos.

if __name__ == "__main__":
    unittest.main(verbosity= 2) # Ejecuta las pruebas definidas en esta clase usando unittest y muestra detalles completos (verbosity=2).