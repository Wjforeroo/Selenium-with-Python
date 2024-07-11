import unittest  # Importa el módulo unittest para escribir y ejecutar pruebas unitarias
from ddt import ddt, data, unpack  # Importa las decoraciones necesarias de DDT (Data-Driven Tests)
from selenium import webdriver  # Importa la clase WebDriver de Selenium para la automatización del navegador
from selenium.webdriver.common.by import By  # Importa el módulo By de Selenium para seleccionar elementos

@ddt  # Decorador que indica que la clase usará Data-Driven Tests
class SearchDDT(unittest.TestCase):  # Define la clase de pruebas unitarias que hereda de unittest.TestCase

    def setUp(self):
        self.driver = webdriver.Chrome()  # Inicializa una instancia del navegador Chrome
        driver = self.driver  # Asigna la instancia del navegador a una variable local
        driver.get('http://demo-store.seleniumacademy.com/')  # Abre la URL especificada en el navegador

    @data(('dress', 4), ('music', 5))  # Define los datos para los tests data-driven
    @unpack  # Desempaqueta los datos para que coincidan con los parámetros del método de prueba
    def test_search_ddt(self, search_value, expected_count):
        driver = self.driver  # Obtiene la instancia del navegador desde la configuración

        search_field = driver.find_element(By.NAME, 'q')  # Encuentra el campo de búsqueda por su nombre
        search_field.clear()  # Borra cualquier texto presente en el campo de búsqueda
        search_field.send_keys(search_value)  # Ingresa el valor de búsqueda en el campo
        search_field.submit()  # Envía el formulario de búsqueda

        products = driver.find_elements(By.XPATH, '//h2[@class="product-name"]/a')  # Encuentra todos los productos encontrados por el XPath especificado
        print(f'Found {len(products)} products')  # Imprime la cantidad de productos encontrados

        for product in products:  # Itera sobre cada producto encontrado
            print(product.text)  # Imprime el texto del producto

        self.assertEqual(expected_count, len(products))  # Verifica que la cantidad de productos encontrados coincida con el valor esperado

    def tearDown(self):
        self.driver.quit()  # Cierra la instancia del navegador y termina la sesión de prueba

if __name__ == "__main__":
    unittest.main(verbosity=2)  # Ejecuta todas las pruebas unitarias cuando se ejecute el script, con detalle de salida 2

