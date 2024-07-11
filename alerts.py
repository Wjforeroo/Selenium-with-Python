import unittest # Importa el módulo unittest para escribir y ejecutar pruebas unitarias.
from pyunitreport import HTMLTestRunner # Importa HTMLTestRunner para generar informes HTML de las pruebas.
from selenium import webdriver # Importa webdriver de Selenium para la automatización del navegador.
from selenium.webdriver.support.ui import Select # Importa Select para interactuar con elementos de selección en formularios web.
from selenium.webdriver.common.by import By # Importa By para seleccionar elementos por diferentes estrategias (ID, clase, etc.).
from selenium.webdriver.common.alert import Alert # Importa Alert para manejar alertas en Selenium.
import time

class CompareProducts(unittest.TestCase):

    def setUp(self):
        """
        Prepara el entorno de prueba:
        - Inicia una instancia del navegador Chrome.
        - Configura un tiempo de espera implícito de 30 segundos para esperar a que los elementos aparezcan.
        - Maximiza la ventana del navegador.
        - Abre la página web http://demo-store.seleniumacademy.com/.
        """
        self.driver = webdriver.Chrome()
        driver = self.driver
        driver.implicitly_wait(30)
        driver.maximize_window()
        driver.get('http://demo-store.seleniumacademy.com/')

    def test_compare_products_removal_alerts(self):
        """
            Test alert:
        """

        driver = self.driver
        search_field = driver.find_element(By.NAME, 'q') # Encuentra el campo de búsqueda por su nombre ('q').
        search_field.clear() # Borra cualquier texto existente en el campo de búsqueda.

        search_field.send_keys('tee') # Ingresa 'tee' en el campo de búsqueda.
        search_field.submit() # Envía el formulario de búsqueda.

        driver.find_element(By.CLASS_NAME, 'link-compare').click() # Encuentra y hace clic en el enlace de comparación por su clase ('link-compare').

        driver.find_element(By.LINK_TEXT, 'Clear All').click() # Encuentra y hace clic en el enlace 'Clear All' por su texto de enlace.

        alert = Alert(driver) # Cambia el contexto a la alerta actual.
        alert_text = alert.text # Obtiene el texto de la alerta.

        self.assertEqual('Are you sure you would like to remove all products from your comparison?', alert_text) # Verifica que el texto de la alerta sea el esperado.
        time.sleep(10)
        alert.accept() # Acepta la alerta (hace clic en 'Aceptar').



    def tearDown(self):
        """
        Realiza la limpieza después de cada prueba:
        - Espera implícitamente por 3 segundos.
        - Cierra la instancia del navegador.
        """
        self.driver.implicitly_wait(15)
        self.driver.close()

if __name__ == '__main__':
    unittest.main(verbosity=2, testRunner= HTMLTestRunner(output='reports_alert', report_name='alert', report_title='Reporte de Alertas'))
"""
    Ejecuta las pruebas:
    - Configura la verbosidad de la salida a 2 para obtener más detalles.
    - Utiliza HTMLTestRunner para generar un informe HTML en la carpeta '' con el nombre ''.
"""