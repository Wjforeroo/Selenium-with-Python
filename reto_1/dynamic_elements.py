import unittest # Importa el módulo unittest para pruebas unitarias
from selenium import webdriver # Importa la clase webdriver del módulo selenium
from selenium.webdriver.common.by import By # Importa la estrategia de selección By del módulo selenium
import time # Importa el módulo time para manejar esperas y pausas

class DynamicElements(unittest.TestCase): # Define una clase DynamicElements que hereda de unittest.TestCase

    def setUp(self): # Método que se ejecuta antes de cada método de prueba
        self.driver = webdriver.Chrome() # Inicia una instancia de Chrome WebDriver y la guarda en self.driver
        driver = self.driver # Asigna self.driver a una variable local driver para facilitar su acceso
        driver.get("https://the-internet.herokuapp.com/") # Abre la URL en el navegador
        driver.find_element(By.LINK_TEXT, 'Disappearing Elements').click() # Encuentra y hace clic en un elemento con el texto 'Disappearing Elements'

    def test_name_elements(self):  # Método de prueba para buscar nombres de elementos
        driver = self.driver # Asigna self.driver a una variable local driver para facilitar su acceso

        options = [] # Inicializa una lista vacía para almacenar opciones
        menu = 5 # Establece el número máximo de elementos a buscar
        tries = 1 # Inicializa un contador de intentos

        while len(options) < 5: # Bucle que se ejecuta mientras la lista options tenga menos de 5 elementos
            options.clear() # Limpia la lista options en cada iteración

            for i in range (menu): # Bucle que itera desde 0 hasta menu - 1
                try:
                    options_name = driver.find_element(By.XPATH, f'/html/body/div[2]/div/div/ul/li[{i + 1}]/a') # Busca un elemento específico usando XPath
                    options.append(options_name.text) # Agrega el texto del elemento encontrado a la lista options
                    print(options) # Imprime la lista options
                except:
                    print(f'Options number "{i+1}" Gallery is NOT FOUND') # Imprime un mensaje si el elemento no se encuentra
                    tries+=1 # Incrementa el contador de intentos 
                    driver.refresh() # Refresca la página si no se encuentra el elemento esperado

        print(f'Finish in {tries} tries') # Imprime el número total de intentos al finalizar el bucle while

    def tearDown(self): # Método que se ejecuta después de cada método de prueba
        self.driver.quit() # Cierra el navegador y libera los recursos.

if __name__ == "__main__": # Condición para verificar si el archivo se está ejecutando directamente
    unittest.main(verbosity=2) # Ejecuta todas las pruebas definidas en la clase DynamicElements con nivel de detalle 2