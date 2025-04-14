from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys



class LoginPage:
    # page Element locators
    _email_id='Email'
    _passowrd_id='Password'
    #_loginBtn_xpath= "//button[@class='button-1 login-button']"
    _loginBtn_xpath= "//button[contains(text(),'Log in')]"
    _logout_link_LinkText ="Logout"

    def __init__(self,driver):
        self.driver=driver

    #action methods
    def setUserName(self,userName):
        emailtextBox = self.driver.find_element(By.ID,self._email_id)
        emailtextBox.clear()
        # emailtextBox.send_keys(Keys.CONTROL + "a")
        # emailtextBox.send_keys(Keys.DELETE)
        emailtextBox.send_keys(userName)
        #text = self.driver.execute_script("return arguments[0].value;", emailtextBox)
        #print("email textbox text is :", text)
    def setPassword(self,pwd):
        passtextBox = self.driver.find_element(By.ID,self._passowrd_id)
        passtextBox.clear()
        # passtextBox.send_keys(Keys.CONTROL +"a")
        # passtextBox.send_keys(Keys.DELETE)
        passtextBox.send_keys(pwd)
        #text = self.driver.execute_script("return arguments[0].value;", passtextBox)
        #print("PASSWORD textbox text is :", text)
    def loginBtnClick(self):
        loginBtn = self.driver.find_element(By.XPATH,self._loginBtn_xpath)
        loginBtn.click()

    def logOutLinkClick(self):
        logOutLink = self.driver.find_element(By.LINK_TEXT,self._logout_link_LinkText)
        logOutLink.click()