from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.select import Select


class Practice():

    def firstTest(self):
        '''This is a test for simple search of a hotel on Booking.com'''

        # define a driver
        driver = webdriver.Firefox()

        # define URL
        baseURL = 'https://busfor.ua/'

        # open and maximize the browser
        driver.maximize_window()

        # open the link
        driver.get(baseURL)

        # implicit wait for load
        driver.implicitly_wait(20)

        # find search field and enter the query
        fromField = driver.find_element(By.XPATH,"//form[@id='new_search']/div[1]/input[1]")
        fromField.send_keys("Одесса")
        time.sleep(2)

        whereField = driver.find_element(By.XPATH, "//form[@id='new_search']/div[2]/input[1]")
        whereField.send_keys("Киев")
        time.sleep(2)

        dateField = driver.find_element(By.XPATH, "//form[@id='new_search']/div[3]/div[1]/input[1]")
        dateField.send_keys('20/12/2017')
        time.sleep(2)

        dropdownQty = driver.find_element(By.XPATH, "//form[@id='new_search']/div[4]/select")
        sel = Select(dropdownQty)
        sel.select_by_index(1)

        searchButton = driver.find_element(By.XPATH, "//form[@id='new_search']/div[5]/input")
        searchButton.click()

ff = Practice()
ff.firstTest()