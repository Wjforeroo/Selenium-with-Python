from selenium import webdriver  # Importa la clase WebDriver de Selenium para la automatización del navegador
from selenium.webdriver.common.by import By  # Importa el módulo By de Selenium para localizar elementos
from selenium.webdriver.support.ui import WebDriverWait  # Importa WebDriverWait de Selenium para esperas explícitas
from selenium.webdriver.support import expected_conditions as EC  # Importa aliases para condiciones esperadas de Selenium

class GooglePage(object):
    def __init__(self, driver):
        self._driver = driver  # Inicializa el driver de Selenium recibido como parámetro
        self._url = 'https://google.com'  # URL de Google
        self.search_locator = 'q'  # Localizador del campo de búsqueda en Google (name='q')

    @property
    def is_loaded(self):
        WebDriverWait(self._driver, 10).until(EC.presence_of_element_located((By.NAME, 'q')))  # Espera hasta que el campo de búsqueda esté presente
        return True  # Retorna True cuando la página está cargada y lista para interactuar

    @property
    def keyword(self):
        input_field = self._driver.find_element(By.NAME, 'q')  # Encuentra el campo de búsqueda
        return input_field.get_attribute('value')  # Retorna el valor actual del campo de búsqueda

    def open(self):
        self._driver.get(self._url)  # Abre la URL de Google en el navegador

    def type_search(self, keyword):
        input_field = self._driver.find_element(By.NAME, 'q')  # Encuentra el campo de búsqueda
        input_field.send_keys(keyword)  # Ingresa el texto de búsqueda especificado en el campo

    def click_submit(self):
        input_field = self._driver.find_element(By.NAME, 'q')  # Encuentra el campo de búsqueda
        input_field.submit()  # Envía el formulario de búsqueda haciendo clic en Enter (submit)

    def search(self, keyword):
        self.type_search(keyword)  # Ingresa el texto de búsqueda en el campo
        self.click_submit()  # Envía el formulario de búsqueda haciendo clic en Enter (submit)
                                             