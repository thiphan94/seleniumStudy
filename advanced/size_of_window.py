from selenium import webdriver

class JavaScriptExecution():

    def test(self):
        driver = webdriver.Firefox()
        driver.maximize_window()
        # driver.get("https://letskodeit.teachable.com/pages/practice")
        driver.execute_script("window.location = 'https://letskodeit.teachable.com/pages/practice';")
        driver.implicitly_wait(3)

        height = driver.execute_script("return window.innerHeight;")
        width = driver.execute_script("return window.innerWidth")

        print('Width is :' + str(width))
        print('Height is :' + str(height))

        driver.quit()

ff = JavaScriptExecution()
ff.test()