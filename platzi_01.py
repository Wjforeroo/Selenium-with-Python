# Importamos unittest para escribir y ejecutar pruebas
import unittest
# Importamos HTMLTestRunner para generar reportes HTML de las pruebas
from pyunitreport import HTMLTestRunner
# Importamos webdriver de Selenium para interactuar con el navegador
from selenium import webdriver

# Creamos una clase que hereda de unittest.TestCase
class HelloWorld(unittest.TestCase):

    # Método setUpClass, que se ejecuta una vez antes de todas las pruebas
    @classmethod
    def setUpClass(cls):
        # Configuramos el driver de Chrome con opciones adicionales
        options = webdriver.ChromeOptions()
        options.add_argument('--ignore-certificate-errors')  # Ignora errores de certificado
        options.add_argument('--ignore-ssl-errors')  # Ignora errores SSL
        cls.driver = webdriver.Chrome(options=options)  # Inicializa el driver de Chrome con las opciones configuradas

        cls.driver.implicitly_wait(10)  # Configura una espera implícita de 10 segundos

    # Caso de prueba para visitar la página de Platzi
    def test_hello_world(self):
        driver = self.driver  # Obtiene el driver desde la instancia de la clase
        driver.get('https://www.platzi.com')  # Abre la página de Platzi en el navegador
    
    def test_visit_wikipedia(self):
        driver = self.driver
        driver.get('https://www.wikipedia.org')

    # Método tearDownClass, que se ejecuta una vez después de todas las pruebas
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()  # Cierra la instancia del navegador al finalizar todas las pruebas

# Bloque para ejecutar las pruebas si se corre este archivo directamente
if __name__ == "__main__":
    # Ejecutamos las pruebas con verbosity 2 para un detalle más alto
    # Usamos HTMLTestRunner para generar un reporte HTML en la carpeta 'reportes'
    # con el nombre 'hello-world-report'
    unittest.main(verbosity=2, testRunner=HTMLTestRunner(output='reports_hello_world', report_name='hello-world-report'))