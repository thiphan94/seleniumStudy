from selenium import webdriver

class FindByClassTag():

    def test(self):

        driver = webdriver.Firefox()
        driver.get('https://letskodeit.teachable.com/p/practice')

        findByClass = driver.find_element_by_class_name('btn-style')

        if findByClass is not None:
            print('we found element by class')

        findbytag = driver.find_element_by_tag_name('h1')

        if findbytag is not None:
            print('we found element by tag')



test1 = FindByClassTag()
test1.test()