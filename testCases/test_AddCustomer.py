import string

from pageObjects.AddCustomer import AddCustomer
from pageObjects.loginPage import LoginPage
from utilies.readProperties import readConfig
from utilies.customLogger import logGen
import pytest
import time
import random
from selenium.webdriver.common.by import By


class Test_003AddCustomer:
    userName = readConfig.getUserName()
    password = readConfig.getPassword()
    Log = logGen.logCreate()

    def generateRandomEmail(self):
        domain = "automation.com"
        email_Length = 10
        email_str = ''.join(random.choice(string.ascii_lowercase) for _ in range(0, email_Length))
        email = email_str + "@" + domain
        return email

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_AddNewCustomer(self, setUp):
        self.Log.info('************* Test_003AddCustomer************')
        self.Log.info('*************Verifying Add New Customer Page ************')
        # To assign appropriate driver through Webfactory method and then login
        self.driver = setUp
        lp = LoginPage(self.driver)
        lp.setUserName(self.userName)
        lp.setPassword(self.password)
        lp.loginBtnClick()

        self.Log.info('*************Login Successful************')
        self.Log.info('*************Starting Add New Customer************')

        self.addCust = AddCustomer(self.driver)
        self.addCust.clickOncustomerMenu()
        self.addCust.clickOnAddCustomerBtn()
        self.addCust.clickOnAddCustomerBtn()

        self.Log.info('*************Filling all the details for the New Customer************')
        self.Email = self.generateRandomEmail()
        self.addCust.enterEmail(self.Email)
        self.addCust.enterPassword("test123")
        self.addCust.enterFirstName("Mr Abc")
        self.addCust.enterLastName("Dalmira")
        self.addCust.selectGender("male")
        self.addCust.selectCustomerRole("registered")
        self.addCust.enterCompanyName("Mainstream company")
        self.addCust.selectTaxExempt()
        self.addCust.selectNewsletter()
        self.addCust.selectManagerVendor("Vendor 2")
        self.addCust.enterComments("Adding new customer")
        self.addCust.clickOnSaveBtn()
        self.Log.info('*************New Customer added successfully************')

        self.Log.info('*****************************Validating the Add Customer Page********************************')
        self.msg = self.driver.find_element(By.XPATH, "//div[@class = 'alert alert-success alert-dismissable']").text
        if "The new customer has been added successfully." in self.msg:
            assert True == True
            self.Log.info('************************Customer Added Successfully********************************')
        else:
            assert True == False
            self.driver.save_screenshot(".\\screenshots\\" + "AddCustomer_Error.png")
            self.Log.error('************************Add Customer functionality failed********************************')

        self.driver.close()
        self.Log.info("**********************End of Add New Customer Test************************")
