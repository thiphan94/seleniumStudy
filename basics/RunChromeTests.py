'''from selenium import webdriver
import os

class RunChromeTests():

    def test(self):
        driver_location = "/Users/irina/Documents/workspace_python/SeleniumProject/lib2/chromedriver"
        os.environ['webdriver.chrome.driver'] = driver_location

        # Instantiate FF Browser Command
        driver = webdriver.Chrome(driver_location)
        # Open the provided URL
        driver.get("https://dp2p.determine.com/d/protected/login.php?page=%2Fp%2Findex.php")

ff = RunChromeTests()
ff.test()'''

from selenium import webdriver
import os

class RunChromeTests():
    # http://chromedriver.storage.googleapis.com/index.html

    def test(self):
        driverLocation = "/Users/irina/Documents/workspace_python/SeleniumProject/lib2/chromedriver"
        os.environ["webdriver.chrome.driver"] = driverLocation
        # Instantiate Chrome Browser Command
        driver = webdriver.Chrome(driverLocation)
        # Open the provided URL
        driver.get("http://www.letskodeit.com")

ff = RunChromeTests()
ff.test()
