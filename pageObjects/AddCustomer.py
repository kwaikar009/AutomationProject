from pageObjects.loginPage import LoginPage
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium import webdriver


class AddCustomer:
    # Identify all the locators on the Add New Customer page
    mainCustomerLink="//a[@href='#']//p[contains(text(),'Customers')]"
    customerMenuItemLink="//a[@href='/Admin/Customer/List']//p[contains(text(),'Customers')]"
    addNewBtn="//a[@href='/Admin/Customer/Create']"
    emailTextboxid="//input[@id='Email']"
    passTextboxid="//input[@id='Password']"
    firstNameTextBox="//input[@id='FirstName']"
    lastNameTExtBox="//input[@id='LastName']"
    rdMaleGender_id="Gender_Male"
    rdFemaleGender_id="Gender_Female"
    company_textbox="//input[@id='Company']"
    cboxTaxExempt="//input[@id='IsTaxExempt']"
    txtNewsletter_Xpath="//span[@aria-owns='select2-SelectedNewsletterSubscriptionStoreIds-results']"
    liNewsletter_xpath="//li[@title='nopCommerce admin demo store']"
    txtCustomerRole_xpath="//span[@class='select2 select2-container select2-container--default select2-container--above']//input[@role='searchbox']"
    lstitemAdministrator_xpath="//li[@id='select2-SelectedCustomerRoleIds-result-9h6i-1']"
    lstitemForum_Members_xpath="//li[contains(text(),'Forum Moderators')]"
    lstitemGuests_xpath="//li[contains(text(),'Guests')]"
    lstitemRegistered_xpath="//li[contains(text(),'Registered')]"
    lstitemVendors = "//li[contains(text(),'Vendors')]"
    selectManagerVendor_xpath="//select[@id='VendorId']"
    cboxActive_xpath="//input[@id='Active']"
    cboxPassChange="//input[@id='MustChangePassword']"
    txtAreaComments="//textarea [@id='AdminComment']"
    btnSave_xpath="//button[@name='save']"

    #constrcutor
    def __init__(self,driver):
        self.driver=driver

    #access methods for all the web elements
    def clickOncustomerMenu(self):
        self.driver.find_element(By.XPATH,self.mainCustomerLink).click()

    def clickOncustomerMenuItem(self):
        self.driver.find_element(By.XPATH,self.addNewBtn).click()

    def clickOnAddCustomerBtn(self):
        self.driver.find_element(By.XPATH, self.customerMenuItemLink).click()

    def enterEmail(self,Email):
        self.driver.find_element(By.XPATH, self.emailTextboxid).send_keys(Email)

    def enterPassword(self,Password):
        self.driver.find_element(By.XPATH, self.passTextboxid).send_keys(Password)

    def enterFirstName(self,FirstName):
        self.driver.find_element(By.XPATH, self.firstNameTextBox).send_keys(FirstName)

    def enterLastName(self,LastName):
        self.driver.find_element(By.XPATH, self.lastNameTExtBox).send_keys(LastName)

    def selectGender(self,Gender):
        if Gender.lower()=="male":
            self.driver.find_element(By.ID,self.rdMaleGender_id).click()
        elif Gender.lower()=="female":
            self.driver.find_element(By.ID, self.rdFemaleGender_id).click()
        else:
            self.driver.find_element(By.ID, self.rdMaleGender_id).click()

    def selectCustomerRole(self,Role):
        self.driver.find_element(By.XPATH,self.txtCustomerRole_xpath).click()
        if Role.lower()=="administrator":
            itemSelected=self.driver.find_element(By.XPATH,self.lstitemAdministrator_xpath)
        elif Role.lower()=="forum moderators":
            itemSelected = self.driver.find_element(By.XPATH, self.lstitemForum_Members_xpath)
        elif Role.lower() == "guests":
            #prevSelectedItem=self.driver.find_element(By.XPATH,"//li[@title='Registered']//span[@class='select2-selection__choice__remove']")
            itemSelected = self.driver.find_element(By.XPATH, self.lstitemGuests_xpath)
        elif Role.lower() == "registered":
            self.driver.find_element(By.XPATH,"//span[@aria-activedescendant='select2-SelectedCustomerRoleIds-result-epe6-5']//li[@title ='Guests']//span").click()
            itemSelected = self.driver.find_element(By.XPATH, self.lstitemRegistered_xpath)
        elif Role.lower() == "vendors":
            itemSelected = self.driver.find_element(By.XPATH, self.lstitemVendors)
        else:
            itemSelected = self.driver.find_element(By.XPATH, self.lstitemGuests_xpath)

    def enterCompanyName(self, CompanyName):
        self.driver.find_element(By.XPATH, self.company_textbox).send_keys(CompanyName)

    def selectTaxExempt(self):
        self.driver.find_element(By.XPATH, self.cboxTaxExempt).click()

    def selectNewsletter(self):
        self.driver.find_element(By.XPATH, self.txtNewsletter_Xpath).click()
        self.driver.find_element(By.XPATH,self.liNewsletter_xpath).click()

    def selectManagerVendor(self,vendorValue):
        dropdownVendor= self.driver.find_element(By.XPATH,self.lstitemVendors)
        sel= Select(dropdownVendor)
        sel.select_by_value(vendorValue)

    def selectActive(self):
        self.driver.find_element(By.XPATH, self.cboxActive_xpath).click()
    def selectChangePassword(self):
        self.driver.find_element(By.XPATH, self.cboxPassChange).click()
    def enterComments(self, Comments):
        self.driver.find_element(By.XPATH, self.txtAreaComments).send_keys(Comments)

    def clickOnSaveBtn(self):
        self.driver.find_element(By.XPATH,self.btnSave_xpath).click()
