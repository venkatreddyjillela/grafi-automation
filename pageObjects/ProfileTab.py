from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ProfileTab:
    # Profile Tab (My Account, Subscriptions, Sign Out)
    txt_profileTitle_xpath = '//button[@id="composition-button"]'
    button_myAccount_xpath = '//h4[normalize-space()="My Account"]'
    button_subscription_xpath = '//h4[normalize-space()="Subscription"]'
    button_profileDropdown_xpath = '//button[@id = "composition-button"]'
    button_signout_xpath = '//button[normalize-space()="Sign Out"]'

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def clickProfileDropdown(self):
        self.driver.find_element(
            By.XPATH, self.button_profileDropdown_xpath).click()

    # get my account link text
    def getMyAccountLinkText(self):
        return self.driver.find_element(By.XPATH, self.button_myAccount_xpath).text
    
    # get subscription link text
    def getSubscriptionLinkText(self):
        return self.driver.find_element(By.XPATH, self.button_subscription_xpath).text
    
    # get sign out button text
    def getSignOutButtonText(self):
        return self.driver.find_element(By.XPATH, self.button_signout_xpath).text

    def clickMyAccount(self):
        self.driver.find_element(By.XPATH, self.button_myAccount_xpath).click()

    def clickSubscription(self):
        self.driver.find_element(
            By.XPATH, self.button_subscription_xpath).click()

    def clickSignout(self):
        self.driver.find_element(By.XPATH, self.button_signout_xpath).click()

    # is sign out button enabled
    def isSignOutButtonEnabled(self):
        return self.driver.find_element(By.XPATH, self.button_signout_xpath).is_enabled()
    
    # is sign out button displayed
    def isSignOutButtonDisplayed(self):
        return self.driver.find_element(By.XPATH, self.button_signout_xpath).is_displayed()

    # check profile title is displayed
    def isProfileTitleDisplayed(self):
        return self.driver.find_element(By.XPATH, self.txt_profileTitle_xpath).is_displayed()
    
    # wait for my account page to load
    def waitForMyAccountPageToLoad(self):
        self.wait.until(EC.url_contains("myAccount"))

    # wait for subscription page to load
    def waitForSubscriptionPageToLoad(self):
        self.wait.until(EC.url_contains("subscription"))

    # wait for login page to load
    def waitForLoginPageToLoad(self):
        self.wait.until(EC.url_contains("openid-connect"))