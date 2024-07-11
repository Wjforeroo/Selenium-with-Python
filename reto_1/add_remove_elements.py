import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class AddRemoveElements(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        driver = self.driver
        driver.get('https://the-internet.herokuapp.com/')
        
        driver.find_element(By.LINK_TEXT, 'Add/Remove Elements').click()
        

    def test_add_remove(self):
        driver = self.driver
        elements_added = int(input('How many elements will you add: '))
        elements_removed = int (input('How many elements will you remove: '))
        total_elements = elements_added - elements_removed

        add_button = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/button')
        time.sleep(3)

        for i in range(elements_added):
            add_button.click()

        for i in range(elements_removed):
            try:
                delete_button = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div/button')
                delete_button.click()
            except:
                print("You're trying to delete more elements the existent")
                break

        if total_elements > 0:
            print(f"There are {total_elements} elements on screen")
        else:
            print("There 0 are elements on screen")

        time.sleep(5)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main(verbosity=2)