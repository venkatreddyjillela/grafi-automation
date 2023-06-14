from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MyAccount:
    # My Account Page
    logo_grafi_xpath = '//img[@alt="grafi logo"]'
    link_firstDraftGenTab_xpath = '//a[normalize-space()="First Draft Generator"]'
    link_rephraserTab_xpath = '//a[normalize-space()="Rephraser"]'
    link_homeTab_xpath = '//a[normalize-space()="Home"]'

    button_myAccount_xpath = '//button[normalize-space()="My Account"]'
    button_subscription_xpath = '//a[@href="/subscription"]'

    drp_personalDetails_xpath = '//div[@id="panel1a-header"]/div[2]'

    txt_personalDetails_xpath = '//h3[normalize-space()="My Personal Details"]'

    txt_userName_xpath = '//div[normalize-space()="User Name"]'
    textbox_username_xpath = '//input[@placeholder="Example.1"]'
    txt_firstName_xpath = '//div[normalize-space()="First Name"]'
    textbox_firstName_xpath = '//input[@placeholder="User First Name"]'
    txt_lastName_xpath = '//div[normalize-space()="Last Name"]'
    textbox_lastName_xpath = '//input[@placeholder="User Last Name"]'
    txt_emailAddress_xpath = '//div[normalize-space()="Email Address"]'
    textbox_emailAddress_xpath = '//input[@placeholder="Example.1@gmail.com"]'



    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def isLogoDisplayed(self):
        return self.driver.find_element(By.XPATH, self.logo_grafi_xpath).is_displayed()

    def clickFirstDraftGenTab(self):
        self.driver.find_element(
            By.XPATH, self.link_firstDraftGenTab_xpath).click()

    def clickRephraserTab(self):
        self.driver.find_element(
            By.XPATH, self.link_rephraserTab_xpath).click()

    def clickHomeTab(self):
        self.driver.find_element(By.XPATH, self.link_homeTab_xpath).click()

    def clickMyAccountButton(self):
        self.driver.find_element(By.XPATH, self.button_myAccount_xpath).click()

    def clickSubscriptionButton(self):
        self.driver.find_element(By.XPATH, self.button_subscription_xpath).click()

    def clickPersonalDetailsDropdown(self):
        self.driver.find_element(By.XPATH, self.drp_personalDetails_xpath).click()

    def getPersonalDetailsText(self):
        return self.driver.find_element(By.XPATH, self.txt_personalDetails_xpath).text
    
    def getUserNameText(self):
        return self.driver.find_element(By.XPATH, self.txt_userName_xpath).text
    
    def getFirstNameText(self):
        return self.driver.find_element(By.XPATH, self.txt_firstName_xpath).text
    
    def getLastNameText(self):
        return self.driver.find_element(By.XPATH, self.txt_lastName_xpath).text
    
    def getEmailAddressText(self):
        return self.driver.find_element(By.XPATH, self.txt_emailAddress_xpath).text
    
    def getUserNameTextBoxValue(self):
        return self.driver.find_element(By.XPATH, self.textbox_username_xpath).get_attribute('value')
    
    def getFirstNameTextBoxValue(self):
        return self.driver.find_element(By.XPATH, self.textbox_firstName_xpath).get_attribute('value')
    
    def getLastNameTextBoxValue(self):
        return self.driver.find_element(By.XPATH, self.textbox_lastName_xpath).get_attribute('value')
    
    def getEmailAddressTextBoxValue(self):
        return self.driver.find_element(By.XPATH, self.textbox_emailAddress_xpath).get_attribute('value')
    
    # check username textbox is enabled or not
    def isUserNameTextBoxEnabled(self):
        return self.driver.find_element(By.XPATH, self.textbox_username_xpath).is_enabled()
    
    # check firstname textbox is enabled or not
    def isFirstNameTextBoxEnabled(self):
        return self.driver.find_element(By.XPATH, self.textbox_firstName_xpath).is_enabled()
    
    # check lastname textbox is enabled or not
    def isLastNameTextBoxEnabled(self):
        return self.driver.find_element(By.XPATH, self.textbox_lastName_xpath).is_enabled()
    
    # check email textbox is enabled or not
    def isEmailTextBoxEnabled(self):
        return self.driver.find_element(By.XPATH, self.textbox_emailAddress_xpath).is_enabled()

    def getMyAccountButtonText(self):
        return self.driver.find_element(By.XPATH, self.button_myAccount_xpath).text
    
    def getSubscriptionButtonText(self):
        return self.driver.find_element(By.XPATH, self.button_subscription_xpath).text
    
    def isPersonalDetailsDropdownExpanded(self):
        element = self.driver.find_element(By.XPATH, self.drp_personalDetails_xpath).get_attribute('class')
        if 'Mui-expanded' in element:
            return True
        else:
            return False
    
    # is my account button displayed
    def isMyAccountButtonDisplayed(self):
        return self.driver.find_element(By.XPATH, self.button_myAccount_xpath).is_displayed()
    
    # is subscription button displayed
    def isSubscriptionButtonDisplayed(self):
        return self.driver.find_element(By.XPATH, self.button_subscription_xpath).is_displayed()
    
    # is my account button enabled
    def isMyAccountButtonEnabled(self):
        return self.driver.find_element(By.XPATH, self.button_myAccount_xpath).is_enabled()
    
    # is subscription button enabled
    def isSubscriptionButtonEnabled(self):
        return self.driver.find_element(By.XPATH, self.button_subscription_xpath).is_enabled()
    
    # wait for curate page to load
    def waitForCuratePageToLoad(self):
        self.wait.until(EC.url_contains("inputContent"))
    # wait for home page to load
    def waitForHomePageToLoad(self):
        self.wait.until(EC.url_contains("home"))

    # wait for Rephraser page to load
    def waitForRephraserPageToLoad(self):
        self.wait.until(EC.url_contains("repurpose"))

    # wait for subscription page to load
    def waitForSubscriptionPageToLoad(self):
        self.wait.until(EC.url_contains("subscription"))
    