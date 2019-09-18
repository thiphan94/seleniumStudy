from selenium import webdriver

class RunFFTests():

    def test(self):
        # Instantiate FF Browser Command
        driver = webdriver.Firefox()
        # Open the provided URL
        driver.get("https://dp2p.determine.com/d/protected/login.php?page=%2Fp%2Findex.php")

ff = RunFFTests()
ff.test()