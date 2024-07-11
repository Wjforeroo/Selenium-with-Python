import unittest
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from pyunitreport import HTMLTestRunner
from ddt import ddt, data, unpack
from time import sleep

@ddt
class Ejericio_a(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        driver = self.driver
        driver.get('http://demo-store.seleniumacademy.com/')
        driver.maximize_window()
        sleep(1)

    """
    Exercise 1: Navigation and Title Verification
        1-Open the page http://demo-store.seleniumacademy.com/.
        2-Verify that the title of the page is "Madison Island".
    """ 
    def test_1_navigations_check_title(self):
        "1: Navigation and Title Verification"
        driver = self.driver

        title_page = driver.title
        try:
            self.assertEqual(title_page, 'Madison Island')
            print(f'The title "{title_page}" is correct')
        except AssertionError as error:
            print(f'The title "{title_page}" is incorrect, the title correct is: "Madison Island"')

    """
Exercise 2: Product Search
    1-Open the page http://demo-store.seleniumacademy.com/.
    2-Use the search field to search for a specific product (e.g., "bag").
    3-Check that the search results contain the searched product.
    """
    @data (('bag', 2))
    @unpack
    def test_2_product_search(self, search_values, expected_count):
        "2: Product Search"
        driver = self.driver
        search = driver.find_element(By.NAME, 'q')
        search.clear()
        search.send_keys('bag')
        search.submit()

        products = driver.find_elements(By.XPATH, '//h2[@class="product-name"]/a')
        print(f'Found {len(products)} products')

        for product in products:
            print(product.text)

        self.assertEqual(len(products), expected_count)

    """
Ejercicio 3: Agregar Producto al Carrito
    1-Abrir la página http://demo-store.seleniumacademy.com/.
    2-Navegar a una categoría de productos (por ejemplo, "Accessories").
    3-Seleccionar un producto de esa categoría para agregarlo al carrito.
    4-Verificar que el producto se haya agregado correctamente al carrito.
    """
    
    """
Ejercicio 4: Proceso de Compra
    Abrir la página http://demo-store.seleniumacademy.com/.
    Elegir un producto y agregarlo al carrito.
    Ir al carrito y comenzar el proceso de compra.
    Llenar el formulario de información de envío y pago.
    Verificar que se haya completado la compra exitosamente y se muestre un mensaje de confirmación.
    Ejercicio 5: Registro de Usuario
    """

    """
Abrir la página http://demo-store.seleniumacademy.com/.
    Navegar a la página de registro de usuario.
    Llenar el formulario de registro con información válida.
    Verificar que el registro se haya completado exitosamente y se redirija a la página de inicio de sesión.
    Ejercicio 6: Inicio de Sesión
    Abrir la página http://demo-store.seleniumacademy.com/.
    Navegar a la página de inicio de sesión.
    Ingresar un nombre de usuario y contraseña válidos.
    Verificar que se haya iniciado sesión correctamente y se redirija a la página principal.
    """
    
    """
Ejercicio 7: Validación de Menú de Navegación
    Abrir la página http://demo-store.seleniumacademy.com/.
    Validar que todos los elementos principales del menú de navegación estén presentes y sean funcionales (por ejemplo, Home, Women, Men, Accessories, etc.).
    """
    

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main(verbosity=2, testRunner=HTMLTestRunner(output='Reports_Exercises', report_name='Exercises_a', report_title='Exercises_a'))