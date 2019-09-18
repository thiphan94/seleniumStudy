from selenium import webdriver

class FindByCSSandXpath():

    def test(self):

        driver = webdriver.Firefox()
        driver.get('https://letskodeit.teachable.com/p/practice')

        findbyCSS = driver.find_element_by_css_selector('legend')


        if findbyCSS is not None:
            print('we found element by your css selector')

        findbyXpath = driver.find_element_by_xpath("//*[@id='name']")

        if findbyXpath is not None:
            print('we found element by your XPath selector')



test1 = FindByCSSandXpath()
test1.test()