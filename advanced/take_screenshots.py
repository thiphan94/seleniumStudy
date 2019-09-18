from selenium import webdriver
from selenium.webdriver.common.by import By


class Screenshots():

    def test1(self):

        BaseURL = 'https://letskodeit.teachable.com'
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(BaseURL)
        driver.implicitly_wait(10)



        # Login button
        login = driver.find_element(By.XPATH, "//div[@id='navbar']//a[contains(text(), 'Login')]").click()

        # Find and fill the email
        email = driver.find_element(By.ID, 'user_email')
        email.send_keys('abc@test.com')

        # Find and fill the password
        password = driver.find_element(By.ID, 'user_password')
        password.send_keys('abc')

        # Click log in
        submitForm = driver.find_element(By.XPATH, "//input[@name='commit']").click()

        # Take a screenshot
        ScreenPath = '/Users/irina/Desktop/test.png'
        try:
            driver.save_screenshot(ScreenPath)
            print('Screenshot is saved here: ' + str(ScreenPath))
        except NotADirectoryError:
            print('No such directory')

        driver. quit()


ff = Screenshots()
ff.test1()