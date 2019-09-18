from selenium import webdriver
import time
from selenium.webdriver.common.by import By

class JavascriptPopup():

    def test(self):
        driver = webdriver.Firefox()
        BaseUrl = 'https://letskodeit.teachable.com/pages/practice'
        driver.maximize_window()

        # Open the URL
        driver.get(BaseUrl)
        driver.implicitly_wait(5)

        # Open the alert
        driver.find_element(By.ID, 'name').send_keys('Ira')
        time.sleep(2)
        driver.find_element(By.ID, 'alertbtn').click()
        alert1 = driver.switch_to.alert
        time.sleep(2)
        # Accept the alert (click OK)
        alert1.accept()
        time.sleep(2)
        # Open the confirm popup
        driver.find_element(By.ID, 'name').send_keys('Ira')
        driver.find_element(By.ID, 'confirmbtn').click()
        time.sleep(2)
        alert2 = driver.switch_to.alert

        # Decline the alert
        alert2.dismiss()
        time.sleep(2)
        driver.quit()


ff = JavascriptPopup()
ff.test()





