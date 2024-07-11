import unittest # Importa el módulo unittest para escribir y ejecutar pruebas unitarias.
from pyunitreport import HTMLTestRunner # Importa HTMLTestRunner para generar informes HTML de las pruebas.
from selenium import webdriver # Importa webdriver de Selenium para la automatización del navegador.
from selenium.webdriver.support.ui import Select # Importa Select para interactuar con elementos de selección en formularios web.
from selenium.webdriver.common.by import By # Importa By para seleccionar elementos por diferentes estrategias (ID, clase, etc.).

class LanguageOptions(unittest.TestCase):

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

    def test_select_languaje(self):
        """
        Prueba la selección de idioma en la página web:
        - Define opciones esperadas de idiomas ('English', 'French', 'German').
        - Captura las opciones de idioma actualmente disponibles en el selector.
        - Verifica que haya exactamente 3 opciones disponibles.
        - Compara las opciones esperadas con las opciones disponibles.
        - Verifica que 'English' esté seleccionado inicialmente.
        - Selecciona 'German' en el selector de idioma.
        - Verifica que la URL actual contenga 'store=german'.
        - Reestablece la selección del idioma a 'English' por índice.
        """

        exp_options = ['English','French','German'] # Opciones esperadas de idiomas.
        act_options = [] # Lista para almacenar las opciones de idioma actuales.

        select_language = Select(self.driver.find_element(By.ID,'select-language')) # Crea un objeto Select para el selector de idioma.
        self.driver.implicitly_wait(5) # Espera implícitamente por 5 segundos.

        self.assertEqual(3, len(select_language.options)) # Verifica que haya exactamente 3 opciones en el selector.

        for option in select_language.options: # Itera sobre las opciones del selector y las agrega a act_options.
            act_options.append(option.text)

        self.assertListEqual(exp_options, act_options) # Compara las opciones esperadas con las opciones actuales.

        self.assertEqual('English', select_language.first_selected_option.text) # Verifica que 'English' esté seleccionado inicialmente.

        select_language.select_by_visible_text('German') # Selecciona 'German' en el selector de idioma.

        self.assertTrue('store=german' in self.driver.current_url) # Verifica que la URL actual contenga 'store=german'.

        self.driver.implicitly_wait(15) # Espera implícitamente por 15 segundos.
        select_language = Select(self.driver.find_element(By.ID, 'select-language')) # Crea un nuevo objeto Select para el selector de idioma.
        select_language.select_by_index(0) # Reestablece la selección del idioma a 'English' por índice.

    def tearDown(self):
        """
        Realiza la limpieza después de cada prueba:
        - Espera implícitamente por 3 segundos.
        - Cierra la instancia del navegador.
        """
        self.driver.implicitly_wait(3)
        self.driver.close()

if __name__ == "__main__":
    unittest.main(verbosity=2, testRunner=HTMLTestRunner(output="reports_language_Options",report_name="Test_select_language", report_title="Lenguajes de la pagina"))
"""
    Ejecuta las pruebas:
    - Configura la verbosidad de la salida a 2 para obtener más detalles.
    - Utiliza HTMLTestRunner para generar un informe HTML en la carpeta 'reports' con el nombre 'Test_select_language'.
"""