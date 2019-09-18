from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time

class Slider:

    def test(self):
        # SETUP
        driver = webdriver.Firefox()
        driver.maximize_window()
        BaseURL = "https://jqueryui.com/slider/"
        driver.get(BaseURL)
        driver.implicitly_wait(3)

        # Switch to iframe
        driver.switch_to.frame(0)

        # Find element
        slider_path = "//div[@id='slider']/span"
        slider = driver.find_element(By.XPATH, slider_path)

        # perform actions
        try:
            actions = ActionChains(driver)
            actions.drag_and_drop_by_offset(slider, 100, 0).perform()
            time.sleep(3)

        except:
            print('HAHA! something went wrong bitch')

        driver.quit()

ff = Slider()
ff.test()