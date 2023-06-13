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
    button_subscription_xpath = '//button[normalize-space()="Subscription"]'

    drp_personalDetails_xpath = '//div[@class="MuiAccordionSummary-expandIconWrapper css-1fx8m19"]'

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
        self.wait = WebDriverWait(self.driver, 30)

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

    def getTextMyAccountButton(self):
        return self.driver.find_element(By.XPATH, self.button_myAccount_xpath).text
    
    def getTextSubscriptionButton(self):
        return self.driver.find_element(By.XPATH, self.button_subscription_xpath).text
    
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
    
    


    