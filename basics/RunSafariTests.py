from selenium import webdriver
import os


class RunSafariTest():

    def test(self):
        # show the pass to selenium standalone server
        server_location = '/Users/irina/Documents/workspace_python/SeleniumProject/selenium-server-standalone-3.7.1'
        os.environ['SELENIUM_SAFARI_JAR'] = server_location
        # declare the driver
        driver = webdriver.Safari()
        # open the web page
        driver.get("http://www.letskodeit.com")


page = RunSafariTest()
page.test()
