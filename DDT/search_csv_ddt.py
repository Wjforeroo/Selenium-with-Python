import csv, unittest  # Importa los módulos csv y unittest
from ddt import ddt, data, unpack  # Importa las decoraciones ddt necesarias para pruebas basadas en datos
from selenium import webdriver  # Importa la clase WebDriver de Selenium para la automatización del navegador
from selenium.webdriver.common.by import By  # Importa el módulo By de Selenium para localizar elementos
from pyunitreport import HTMLTestRunner  # Importa HTMLTestRunner de pyunitreport para generar informes HTML

def get_data(file_name):
    rows = []
    data_file = open(file_name, 'r')  # Abre el archivo CSV especificado en modo lectura
    reader = csv.reader(data_file)  # Crea un lector CSV para leer el archivo
    next(reader, None)  # Omite la primera fila del archivo (encabezados)

    for row in reader:  # Itera sobre cada fila restante en el archivo CSV
        rows.append(row)  # Agrega cada fila a la lista de filas
    return rows  # Retorna todas las filas del archivo CSV como una lista de listas

@ddt  # Decorador que indica que la clase usará Data-Driven Tests (DDT)
class SearchDDT(unittest.TestCase):  # Define la clase de pruebas unitarias que hereda de unittest.TestCase

    def setUp(self):
        self.driver = webdriver.Chrome()  # Inicializa una instancia del navegador Chrome
        driver = self.driver  # Asigna la instancia del navegador a una variable local
        driver.get('http://demo-store.seleniumacademy.com/')  # Abre la URL especificada en el navegador

    @data(*get_data('\\Users\\WPOSS\\Documents\\Selenium\\DDT\\testdata.csv'))  # Define los datos para pruebas basadas en datos (data-driven)
    @unpack  # Desempaqueta los datos para que coincidan con los parámetros del método de prueba
    def test_search_ddt(self, search_value, expected_count):
        driver = self.driver  # Obtiene la instancia del navegador desde la configuración

        search_field = driver.find_element(By.NAME, 'q')  # Encuentra el campo de búsqueda por su nombre
        search_field.clear()  # Borra cualquier texto presente en el campo de búsqueda
        search_field.send_keys(search_value)  # Ingresa el valor de búsqueda en el campo
        search_field.submit()  # Envía el formulario de búsqueda

        products = driver.find_elements(By.XPATH, '//h2[@class="product-name"]/a')  # Encuentra todos los productos que coinciden con el XPath especificado
        
        expected_count = int(expected_count)  # Convierte expected_count a un entero

        if expected_count > 0:  # Si se esperan resultados positivos
            self.assertEqual(expected_count, len(products))  # Verifica que la cantidad de productos coincida con expected_count
        else:  # Si no se esperan resultados
            message = driver.find_element(By.NAME,'note-msg')  # Encuentra el mensaje de búsqueda sin resultados
            self.assertEqual('Your search returns no results.', message)  # Verifica que el mensaje sea el esperado

        print(f'Found {len(products)} products')  # Imprime la cantidad de productos encontrados

    def tearDown(self):
        self.driver.quit()  # Cierra la instancia del navegador y termina la sesión de prueba

if __name__ == "__main__":
    unittest.main(verbosity=2,  # Configura el nivel de detalle de la salida de la prueba
                  testRunner=HTMLTestRunner(output='Resports_DDT',  # Directorio de salida para los informes HTML
                                            report_title='Search',  # Título del informe HTML
                                            report_name='Search_csv_ddt'))  # Nombre del archivo de informe HTML
