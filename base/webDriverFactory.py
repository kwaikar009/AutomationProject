from selenium import webdriver
from utilies.readProperties import readConfig

class WebDriverFactory:

    def __init__(self,browser):
        self.browser= browser

    def getWebDriverInstance(self):
        baseUrl = readConfig.getAppUrl()
        browser = self.browser.lower()
        if browser=="chrome":
            driver = webdriver.Chrome()
        elif browser=="firefox":
            driver=webdriver.Firefox()
        else:
            driver=webdriver.Ie()

        driver.maximize_window()
        driver.implicitly_wait(2)
        driver.get(baseUrl)
        return driver
