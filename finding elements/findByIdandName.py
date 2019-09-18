from selenium import webdriver

class FindByIDorName():

    def test(self):

        practice_page = 'https://letskodeit.teachable.com/p/practice'
        driver = webdriver.Firefox()
        driver.get(practice_page)

        find_by_id = driver.find_element_by_id('openwindow')

        if find_by_id is not None:
            print('we found element by id')

        find_by_name = driver.find_element_by_name('fpapi_comm_iframe')

        if find_by_name is not None:
            print('we found element by name')


lol = FindByIDorName()
lol.test()