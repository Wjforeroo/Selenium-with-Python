import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from pyunitreport import HTMLTestRunner
import time

class RegisterNewUser(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        driver = self.driver
        driver.implicitly_wait(15)
        driver.maximize_window()
        driver.get('http://demo-store.seleniumacademy.com')

    def test_new_user(self):
        driver = self.driver
        driver.find_element(By.XPATH, '/html/body/div/div[2]/header/div/div[2]/div/a/span[2]').click()
        time.sleep(5)
        driver.find_element(By.XPATH, '/html/body/div/div[2]/header/div/div[5]/div/ul/li[6]/a').click()
        time.sleep(5)

        create_account_button = driver.find_element(By.XPATH, '/html/body/div/div[2]/div[2]/div/div/div[2]/form/div/div[1]/div[2]/a/span/span')
        time.sleep(5)
        self.assertTrue(create_account_button.is_displayed() and create_account_button.is_enabled())
        create_account_button.click()
        time.sleep(5)

        self.assertEqual('Create New Customer Account', driver.title)

        first_name = driver.find_element(By.ID, 'firstname')
        middle_name = driver.find_element(By.ID, 'middlename')
        last_name = driver.find_element(By.ID, 'lastname')
        email_address = driver.find_element(By.ID, 'email_address')
        password = driver.find_element(By.ID, 'password')
        confirm_password = driver.find_element(By.ID, 'confirmation')
        new_letter_subscription = driver.find_element(By.ID, 'is_subscribed')
        submit_button = driver.find_element(By.CLASS_NAME, 'button')
        time.sleep(5)

        self.assertTrue(first_name.is_enabled() 
                        and middle_name.is_enabled()
                        and last_name.is_enabled()
                        and email_address.is_enabled()
                        and password.is_enabled()
                        and confirm_password.is_enabled()
                        and new_letter_subscription.is_enabled()
                        and submit_button.is_enabled())
        
        first_name.send_keys('test')
        driver.implicitly_wait(15)
        middle_name.send_keys('Qa')
        driver.implicitly_wait(15)
        last_name.send_keys('Ocaña')
        driver.implicitly_wait(15)
        email_address.send_keys('tester@wiki.com')
        driver.implicitly_wait(15)
        password.send_keys('1234567890')
        driver.implicitly_wait(15)
        confirm_password.send_keys('1234567890')
        driver.implicitly_wait(15)
        new_letter_subscription.click()
        driver.implicitly_wait(15)
        submit_button.click()
        time.sleep(5)



    def tearDown(self):
        self.driver.implicitly_wait(30)
        self.driver.quit()

if __name__ == "__main__":
        unittest.main(verbosity=2, testRunner=HTMLTestRunner(output='reportes', report_name='Crear_usuario'))