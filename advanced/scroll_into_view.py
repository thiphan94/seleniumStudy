from selenium import webdriver
import time

class ScrollIntoView():

    def test(self):
        driver = webdriver.Firefox()
        driver.maximize_window()
        BaseURL = 'https://letskodeit.teachable.com/pages/practice'
        driver.get(BaseURL)
        driver.implicitly_wait(3)

        # Scroll up
        driver.execute_script('window.scrollBy(0, 1000);')
        time.sleep(3)


        # Scroll down
        driver.execute_script('window.scrollBy(0, -1000);')
        time.sleep(3)

        # Scroll into view
        element = driver.find_element_by_id('mousehover')
        driver.execute_script('arguments[0].scrollIntoView(true);', element)
        time.sleep(3)
        driver.execute_script('window.scrollBy(0, -150);')
        time.sleep(3)

        # Native way to scroll
        driver.execute_script('window.scrollBy(0, -1000);')
        location = element.location_once_scrolled_into_view
        print('Location: ' + str(location))
        time.sleep(3)

        driver.quit()


ff = ScrollIntoView()
ff.test()