import time
from utilies.readProperties import readConfig
from pageObjects.loginPage import LoginPage
from utilies.customLogger import logGen
import traceback
import sys

from selenium import webdriver
import pytest
from testCases import conftest

class Test_001_Login:
    #Values
   # baseUrl = readConfig.getAppUrl()
    userName = readConfig.getUserName()
    password = readConfig.getPassword()
    Log = logGen.logCreate()


    @pytest.mark.regression
    def test_VerifyHomePageTitle(self, setUp):
        try:
            self.Log.info('************* Test_001_Login************')
            self.Log.info('*************Verifying Login Page ************')
            # To launch the website verify the page title
            self.driver = setUp
            #self.driver.get(self.baseUrl)

            actual_Title = self.driver.title

            if actual_Title == "nopCommerce demo store. Login":
                assert True
                #self.driver.close()
                self.Log.info('*************Homepage Title test passed ************')

            else:
                assert False
                self.driver.save_screenshot('.\\Screenshots\\' + 'test_HomePageTitle.png')
                #self.driver.close()
                self.Log.info('*************Homepage Title test failed ************')


        except:
            self.driver.save_screenshot('.\\Screenshots\\' + 'test_HomePageTitleError.png')
           # self.driver.close()
            self.Log.warning('*************Error occurred in Homepage Title Test ************')
            self.Log.warning('*************Homepage Title test failed ************')
        finally:
            self.driver.close()

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_loginWithValidCredentials(self, setUp):
        try:
            self.Log.info('*************Verifying Login Test ************')
            self.driver = setUp
            #self.driver.get(self.baseUrl)

            self.lp = LoginPage(self.driver)
            self.lp.setUserName(self.userName)

            self.lp.setPassword(self.password)

            self.lp.loginBtnClick()
            time.sleep(4)
            login_Title = self.driver.title

            if login_Title == "Dashboard / nopCommerce administration":
                assert True
                self.Log.info('*************Login test passed ************')
               # self.driver.close()

            else:
                assert False
                self.driver.save_screenshot('.\\Screenshots\\' + 'test_LOGIN.png')
                self.Log.warning('*************Login test failed ************')
               # self.driver.close()
        except:
            self.driver.save_screenshot('.\\Screenshots\\' + 'test_LOGIN_Error.png')
            self.Log.error('*************Error occurred in Login Test ************')
            self.Log.warning('*************Login test failed ************')
            traceback.print_exc()
        finally:
            self.driver.close()