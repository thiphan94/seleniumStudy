from selenium import webdriver
from selenium.webdriver.common.by import By

class FindBy():

    def test(self):
        driver = webdriver.Firefox()
        driver.get('https://letskodeit.teachable.com/p/practice')

        findbytag = driver.find_element(By.TAG_NAME, 'h1')

        if findbytag is not None:
            print('we found your element by tag')


kek = FindBy()
kek.test()