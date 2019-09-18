from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class Testtext():

    def test(self):
        driver = webdriver.Firefox()
        baseURL = 'https://letskodeit.teachable.com/p/practice'
        driver.maximize_window()
        driver.get(baseURL)
        driver.implicitly_wait(10)

        element = driver.find_element(By.ID, 'name')
        valueOntheElement = element.get_attribute('type')

        print(valueOntheElement)
        time.sleep(3)
        driver.quit()



ira = Testtext()
ira.test()