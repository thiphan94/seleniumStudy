from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time

class DragAndDrop:

    def test(self):
        # SETUP
        driver = webdriver.Firefox()
        driver.maximize_window()
        BaseURL = "https://jqueryui.com/droppable/"
        driver.get(BaseURL)
        driver.implicitly_wait(3)

        # Switch to iframe
        driver.switch_to.frame(0)

        # Find elements
        from_element = driver.find_element(By.ID, 'draggable')
        to_element = driver.find_element(By.ID, 'droppable')

        # perform actions
        try:
            actions = ActionChains(driver)
            # 1 case
            #actions.drag_and_drop(from_element, to_element).perform()

            # 2 case
            #actions.click_and_hold(from_element).move_to_element(to_element).release().perform()

            # 3 case
            actions.click_and_hold(from_element).release(to_element).perform()

            time.sleep(3)

        except:
            print('HAHA! something went wrong bitch')

        driver.quit()

ff = DragAndDrop()
ff.test()