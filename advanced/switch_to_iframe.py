from selenium import webdriver
import time

class SwitchToIframe():

    def test(self):
        driver = webdriver.Firefox()
        driver.maximize_window()
        BaseURL = 'https://letskodeit.teachable.com/pages/practice'
        driver.get(BaseURL)
        driver.implicitly_wait(3)
        driver.execute_script('window.scrollBy(0, 1000);')

        # Switch to iFrame by ID
        driver.switch_to.frame('courses-iframe')

        # Search within the iFrame
        search_field = driver.find_element_by_id('search-courses')
        search_field.send_keys('python')
        time.sleep(3)

        # Switch back to default content
        driver.switch_to.default_content()
        driver.execute_script('window.scrollBy(0, -1000);')
        driver.find_element_by_id('name').send_keys('test is successful')
        time.sleep(3)
        driver.quit()


ff = SwitchToIframe()
ff.test()