from selenium import webdriver

class FindByLinkText():

    def test(self):

        driver = webdriver.Firefox()
        driver.get('https://letskodeit.teachable.com/p/practice')

        findByLink = driver.find_element_by_link_text('Login')

        if findByLink is not None:
            print('we found element by your text in the link')

        findbypartiallinktext = driver.find_element_by_partial_link_text('Pract')

        if findbypartiallinktext is not None:
            print('we found element by your partial link text')



test1 = FindByLinkText()
test1.test()