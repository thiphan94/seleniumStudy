from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class clickAndType():

    def test(self):
        baseURL = 'https://letskodeit.teachable.com/'
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(baseURL)
        driver.implicitly_wait(10)

        loginButton = driver.find_element(By.XPATH, "//div[@id='navbar']//a[@href = '/sign_in']")
        loginButton.click()

        emailField = driver.find_element(By.ID, 'user_email')
        emailField.send_keys('test')

        passwordField = driver.find_element(By.ID, 'user_password')
        passwordField.send_keys('test')

        time.sleep(5)

        emailField.clear()

        time.sleep(5)

        emailField.send_keys('test')


ff = clickAndType()
ff.test()
