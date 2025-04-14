from selenium import webdriver
from selenium.webdriver.common.by import By
from pageObjects.loginPage import LoginPage
from pageObjects.AddCustomer import AddCustomer


class SearchCustomer:
    #Identify the locator values for email,firstname,LastName,Search Button and Table
    txtEmail_id="SearchEmail"
    txtFirstName_id="SearchFirstName"
    txtLastName_id="SearchLastName"
    btnSearch_id="search-customers"
    tbCustList="//table[@id='customers-grid']"
    tbCustList_rows="//table[@id ='customers-grid']//tr"
    tbCustList_Cols="//table[@id='customers-grid']//tr//td"


    def __init__(self,driver):
        self.driver=driver

    def enterEmail(self,email):
        self.driver.find_element(By.ID,self.txtEmail_id).send_keys(email)

    def enterFirstName(self, FirstName):
        self.driver.find_element(By.ID, self.txtFirstName_id).send_keys(FirstName)

    def enterLastName(self, LastName):
        self.driver.find_element(By.ID, self.txtLastName_id).send_keys(LastName)

    def clickSearchBtn(self):
        self.driver.find_element(By.ID,self.btnSearch_id).click()

    def searchByEmail(self,email):
        myTable= self.driver.find_element(By.ID,self.tbCustList)
        myTableRows= self.driver.find_element(By.XPATH,self.tbCustList_rows)
        myTableCols = self.driver.find_element(By.XPATH,self.tbCustList_Cols)

        for row in myTableRows:
            for col in myTableCols:
                if email in row[col].text:
                    print("Customer Found")
                    flag=True
                    break
                else:
                    print("Customer Not Found")
                    flag=False
        return flag

    def searchByName(self,FullName):
        myTable= self.driver.find_element(By.ID,self.tbCustList)
        myTableRows= self.driver.find_element(By.XPATH,self.tbCustList_rows)
        myTableCols = self.driver.find_element(By.XPATH,self.tbCustList_Cols)

        for row in myTableRows:
            for col in myTableCols:
                if FullName in row[col].text:
                    print("Customer Found")
                    flag=True
                    break
                else:
                    print("Customer Not Found")
                    flag=False
        return flag

