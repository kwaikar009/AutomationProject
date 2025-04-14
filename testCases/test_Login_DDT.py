import time
from utilies.readProperties import readConfig
from pageObjects.loginPage import LoginPage
from utilies.customLogger import logGen
import traceback
import sys
from utilies import XlUtils

from selenium import webdriver
import pytest
from testCases import conftest

class Test_002_Login:
    #Values
    Log = logGen.logCreate()
    path =".//testData/LoginTestData.xlsx"


    @pytest.mark.regression
    def test_loginWithValidCredentials(self, setUp):
        try:
            self.Log.info('*************Test_002_Login_DDT ************')
            self.Log.info('*************Verifying Login Test with DDT ************')
            self.driver = setUp


            self.lp = LoginPage(self.driver)

            self.rowcount = XlUtils.getRowCount(self.path,'Sheet1')
            print("No of rows are,",self.rowcount)
            #Create a empty list to store the results of all DDT values
            list_status =[]

            for r in range(2,self.rowcount+1):
                self.user = XlUtils.readData(self.path,'Sheet1',r,1)
                self.pwd = XlUtils.readData(self.path, 'Sheet1', r, 2)
                self.exp = XlUtils.readData(self.path, 'Sheet1', r, 3)

                print(self.user,self.pwd,self.exp)
                self.lp.setUserName(self.user)
                self.lp.setPassword(self.pwd)
                self.lp.loginBtnClick()

                time.sleep(4)
                login_Title = self.driver.title
                print(login_Title)

                if login_Title == "Dashboard / nopCommerce administration":
                    if self.exp.lower()=="pass":
                        self.Log.info('*************Login test passed ************')
                        list_status.append("Pass")
                        self.lp.logOutLinkClick()
                    elif self.exp.lower()=="fail":
                        self.driver.save_screenshot('.\\Screenshots\\' + 'test_LOGIN.png')
                        self.Log.info('*************Login test failed ************')
                        list_status.append("Fail")
                        self.lp.logOutLinkClick()

                else:
                    if self.exp.lower() == "fail":
                        self.driver.save_screenshot('.\\Screenshots\\' + 'test_LOGIN.png')
                        self.Log.info('*************Login test failed ************')
                        list_status.append("Pass")
                        self.lp.logOutLinkClick()
        except:
            self.driver.save_screenshot('.\\Screenshots\\' + 'test_LOGIN_Error.png')
            self.Log.error('*************Error occurred in Login Test ************')
            self.Log.warning('*************Login test failed ************')
           # self.lp.logOutLinkClick()
           # traceback.print_exc()
        finally:
            self.driver.close()

        if "Fail" not in list_status:
            assert True
            self.Log.info('*************Entire Login DDT test passed ************')
        else:
            assert False
            self.Log.info('*************Entire Login DDT test failed ************')

        self.Log.info('*************End of Test_002_Login************')