# Importamos webdriver de Selenium para interactuar con el navegador
from selenium import webdriver

import time


driver = webdriver.Chrome()#Inicialización del driver de chrome


driver.get("http://selenium.dev")#Abrir una página en especifico en el navegador

time.sleep(30)#Tiempo en el que permanecera la ventana abierta.

driver.quit()#Cerrar el navegador al finalizar



