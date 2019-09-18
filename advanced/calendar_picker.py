from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class TestCalendarPicker():

    def test(self):
        BaseURL = 'https://www.expedia.com/'

        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(BaseURL)
        driver.implicitly_wait(10)


        # Open the 'Flights' tab
        flightsTab = driver.find_element_by_xpath('//button[@id="tab-flight-tab-hp"]')
        flightsTab.click()
        # Click the 'Departing date' picker
        departingDate = driver.find_element(By.XPATH, '//input[@id="flight-departing-hp-flight"]')
        departingDate.click()
        # Choose the department date
        testDepDate = driver.find_element(By.XPATH, '//div[@class ="datepicker-cal-month"][position()=1]//button[text()=31]')
        testDepDate.click()
        # Click the 'Returning' picker
        returningPicker = driver.find_element(By.XPATH, "//input[@id='flight-returning-hp-flight']")
        returningPicker.click()
        # Choose the returning date
        testRetDate = driver.find_element(By.XPATH, '//div[@class="datepicker-cal-month"][position()=2]//button[text()=1]')
        # Flying from Kiev
        ffrom = driver.find_element(By.XPATH, "//input[@id='flight-origin-hp-flight']")
        ffrom.send_keys('IEV')
        # Flying to London
        fto = driver.find_element(By.XPATH, "//input[@id='flight-destination-hp-flight']")
        fto.send_keys('London')
        # Click the 'Search' button
        search = driver.find_element(By.XPATH, "//form[@id='gcw-flights-form-hp-flight']//button[@type='submit']")
        search.click()

        time.sleep(3)
        driver.quit()


ff = TestCalendarPicker()
ff.test()














