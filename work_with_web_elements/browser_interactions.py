from selenium import webdriver

class BrowserInteractions():

    def test(self):
        baseURL = 'https://letskodeit.teachable.com/p/practice'
        # set the driver
        driver = webdriver.Firefox()
        #Maximize a window
        driver.maximize_window()
        # open URL
        driver.get(baseURL)
        # get title
        title_page = driver.title
        print('This is a title: ' + title_page)
        # get current URL
        currentURL = driver.current_url
        print('Current URL is: ' + currentURL)
        # refresh the page
        driver.refresh()
        print('Page is just refreshed 1st time')
        driver.get(driver.current_url)
        print('Page is just refreshed 2nd time')
        # open another URL
        driver.get('https://letskodeit.teachable.com/')
        # browser back
        driver.back()
        # browser forward
        driver.forward()
        # get page source
        source = driver.page_source
        print(source)
        # browser close/quit
        driver.quit()

lol = BrowserInteractions()
lol.test()