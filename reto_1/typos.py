import unittest  # Importa el módulo unittest para definir y ejecutar casos de prueba unitarios
from selenium import webdriver  # Importa la clase webdriver del módulo selenium para interactuar con el navegador
from selenium.webdriver.common.by import By  # Importa la clase By del módulo selenium.webdriver.common.by para métodos de localización

class Typos(unittest.TestCase):  # Define una clase Typos que hereda de unittest.TestCase, lo que indica que es un caso de prueba
                                    # unittest.TestCase proporciona los métodos y aserciones para la creación de casos de prueba
                                    
    def setUp(self):  # Define el método setUp, que se ejecuta antes de cada método de prueba
        self.driver = webdriver.Chrome()  # Inicializa el driver de Chrome para automatizar el navegador
        driver = self.driver  # Crea una referencia local al driver
        driver.get('https://the-internet.herokuapp.com/')  # Abre la URL especificada en el navegador
        driver.find_element(By.LINK_TEXT, 'Typos').click()  # Localiza y hace clic en el elemento que contiene el texto 'Typos'

    def test_find_typos(self):  # Define el método de prueba test_find_typos
        driver = self.driver  # Obtiene una referencia al driver desde la instancia de la clase
        
        paragraph_to_check = driver.find_element(By.CSS_SELECTOR, '#content > div > p:nth-child(3)')  # Localiza un párrafo específico usando un selector CSS
        text_to_check = paragraph_to_check.text  # Obtiene el texto del párrafo y lo asigna a la variable text_to_check
        print(text_to_check)  # Imprime el texto del párrafo en la consola

        tries = 1  # Inicializa el contador de intentos en 1
        found = False  # Inicializa la bandera found en False
        correct_text = "Sometimes you'll see a typo, other times you won't."  # Define el texto correcto que se espera encontrar

        while text_to_check != correct_text:  # Inicia un bucle while que se ejecuta mientras el texto no sea el correcto
            driver.refresh()  # Refresca la página en el navegador
            tries += 1  # Incrementa el contador de intentos en 1
            paragraph_to_check = driver.find_element(By.CSS_SELECTOR, '#content > div > p:nth-child(3)')  # Vuelve a obtener el párrafo después del refresco
            text_to_check = paragraph_to_check.text  # Actualiza el texto a verificar con el nuevo texto del párrafo
        else:  # Cuando la condición del bucle while se vuelve falsa (se encuentra el texto correcto)
            found = True  # Establece found en True

        self.assertEqual(found, True)  # Asegura que la variable found sea True usando la aserción assertEqual
        print(f'It took {tries} tries to find the typo')  # Imprime el número de intentos que tomó encontrar el typo

    def tearDown(self):  # Define el método tearDown, que se ejecuta después de cada método de prueba
        pass  # No realiza ninguna acción específica en este caso

if __name__ == "__main__":  # Verifica si el script está siendo ejecutado directamente
    unittest.main(verbosity=2)  # Ejecuta todos los casos de prueba definidos en la clase Typos, con detalle de salida