from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time

class MOuseHover:

    def test(self):
        # SETUP
        driver = webdriver.Firefox()
        driver.maximize_window()
        BaseURL = "https://letskodeit.teachable.com/pages/practice"
        driver.get(BaseURL)
        driver.implicitly_wait(3)

        # Scroll down to the element
        driver.execute_script('window.scrollBy(0,600);')
        time.sleep(2)

        # Find the element to mouse hover and the element to click
        button = driver.find_element(By.ID, 'mousehover')
        elementXPATH = "//div[@class='mouse-hover-content']//a[text()='Top']"
        element = driver.find_element(By.XPATH, elementXPATH)

        # Mousehover
        try:
            actions = ActionChains(driver)
            actions.move_to_element(button).perform()
            time.sleep(2)
            element.click()
            time.sleep(2)
            print('We just clicked on the hidden element!')
        except:
            print('haha! Something went wrong!')

        driver.quit()

ff = MOuseHover()
ff.test()