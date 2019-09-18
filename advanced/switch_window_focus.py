from selenium import webdriver
import time

class SwitchBetweenWindows():

    def test(self):
        driver = webdriver.Firefox()
        driver.maximize_window()
        BaseURL = 'https://letskodeit.teachable.com/pages/practice'
        driver.get(BaseURL)
        driver.implicitly_wait(3)

        # Find parent handle (window with focus on)
        parent_handle = driver.current_window_handle
        print('Parent handle: ' + parent_handle)

        # Click the button to open another window
        driver.find_element_by_id('openwindow').click()

        # Define handles
        handles = driver.window_handles
        for handle in handles:
            print('Handle: ' + handle)

            # Switch to another handle
            if handle not in parent_handle:
                driver.switch_to.window(handle)
                print('We successfully swithched to handle:' + handle)
                search_field = driver.find_element_by_id('search-courses')
                search_field.send_keys('python')
                time.sleep(3)
                driver.close()

        # Switch back to parent handle
        driver.switch_to.window(parent_handle)
        print('We switched back to the parent handle' + parent_handle)
        driver.find_element_by_id('name').send_keys('test is successful')
        time.sleep(3)
        driver.quit() 


ff = SwitchBetweenWindows()
ff.test()