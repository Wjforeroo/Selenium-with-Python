from unittest import TestLoader, TestSuite
from pyunitreport import HTMLTestRunner
from HtmlTestRunner import HTMLTestRunner
from assertions import AssertionsTest
from searchtest import SearchTest

assertions_test = TestLoader().loadTestsFromTestCase(AssertionsTest)
search_test = TestLoader().loadTestsFromTestCase(SearchTest)

smoke_test = TestSuite([assertions_test, search_test])

kwargs = {
    "output": 'reports', #Carpeta en la que se almacenara
    "report_name": "smoke_report", #Nombre del archivo
    "combine_reports": True, #Une los 2 reportes en un solo archivo HTML
    "add_timestamp": True, # Añade la fecha y la hora al nombre del archivo
}

runner = HTMLTestRunner(**kwargs) # Almacena el reporte en la variable runner
runner.run(smoke_test)