import unittest  # Importa el módulo unittest para la escritura y ejecución de pruebas unitarias
from selenium import webdriver  # Importa la clase WebDriver de Selenium para la automatización del navegador
from google_page import GooglePage  # Importa la clase GooglePage desde el módulo google_page

class GoogleTest(unittest.TestCase):  # Define la clase GoogleTest que hereda de unittest.TestCase

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()  # Inicializa una instancia del navegador Chrome al inicio de la clase

    def test_search(self):
        google = GooglePage(self.driver)  # Crea una instancia de GooglePage pasando el driver del navegador
        google.open()  # Abre la página de Google
        google.search('Platzi')  # Realiza una búsqueda en Google con el término 'Platzi'

        self.assertEqual('Platzi', google.keyword)  # Verifica que el término de búsqueda sea 'Platzi'

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()  # Cierra el navegador al finalizar todas las pruebas de la clase

if __name__ == "__main__":
    unittest.main()  # Ejecuta las pruebas cuando se ejecuta el script directamente