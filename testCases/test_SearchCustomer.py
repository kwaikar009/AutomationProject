import string
from pageObjects.searchCustomer import SearchCustomer
from pageObjects.AddCustomer import AddCustomer
from pageObjects.loginPage import LoginPage
from utilies.readProperties import readConfig
from utilies.customLogger import logGen
import pytest
import time


class Test_004SearchCustomer:
    userName = readConfig.getUserName()
    password = readConfig.getPassword()
    Log = logGen.logCreate()


    @pytest.mark.regression
    def test_SearchCustomerByEmail(self, setUp):
        self.Log.info('************* Test_004SearchCustomer************')
        self.Log.info('*************Verifying Search Customer Page ************')
        # To assign appropriate driver through Webfactory method and then login
        self.driver = setUp
        lp = LoginPage(self.driver)
        lp.setUserName(self.userName)
        lp.setPassword(self.password)
        lp.loginBtnClick()

        self.Log.info('*************Login Successful************')
        self.Log.info('*************Starting Search Customer************')

        self.addCust = AddCustomer(self.driver)
        self.addCust.clickOncustomerMenu()
        self.addCust.clickOnAddCustomerBtn()
        self.addCust.clickOnAddCustomerBtn()

        self.Log.info('*************Searching for the Existing Customer by email************')
        self.searchCust = SearchCustomer(self.driver)
        self.searchCust.enterEmail("steve_gates@nopCommerce.com")
        self.searchCust.clickSearchBtn()

        self.Log.info('*****************************Validating the Search Customer Page using Email********************************')
        status=self.searchCust.searchByEmail("steve_gates@nopCommerce.com")
        if status == True:
            assert True==True
            self.Log.info('************************Customer Found Successfully********************************')
        else:
            assert True == False
            self.driver.save_screenshot(".\\screenshots\\" + "SearchCustomer_NotFound.png")
            self.Log.warning('************************Customer was not found********************************')

        self.driver.close()
        self.Log.info("**********************End of Search Customer Test usimg Email************************")


        @pytest.mark.regression
        def test_SearchCustomerByEmail(self, setUp):
            self.Log.info('************* Test_004SearchCustomer************')
            self.Log.info('*************Verifying Search Customer Page ************')
            # To assign appropriate driver through Webfactory method and then login
            self.driver = setUp
            lp = LoginPage(self.driver)
            lp.setUserName(self.userName)
            lp.setPassword(self.password)
            lp.loginBtnClick()

            self.Log.info('*************Login Successful************')
            self.Log.info('*************Starting Search Customer using Name************')

            self.addCust = AddCustomer(self.driver)
            self.addCust.clickOncustomerMenu()
            self.addCust.clickOnAddCustomerBtn()
            self.addCust.clickOnAddCustomerBtn()

            self.Log.info('*************Searching for the Existing Customer using Name************')
            self.searchCust = SearchCustomer(self.driver)
            self.searchCust.enterFirstName("steve")
            self.searchCust.enterLastName("gates")
            self.searchCust.clickSearchBtn()

            self.Log.info(
                '*****************************Validating the Search Customer Page********************************')
            status = self.searchCust.searchByName("steve gates")
            if status == True:
                assert True == True
                self.Log.info('************************Customer Found Successfully using Name********************************')
            else:
                assert True == False
                self.driver.save_screenshot(".\\screenshots\\" + "SearchCustomer_NotFound.png")
                self.Log.warning('************************Customer was not found********************************')

            self.driver.close()
            self.Log.info("**********************End of Search Customer Test using Name************************")
