from selenium.webdriver.common.by import By


class ProfileTab:
    # Profile Tab (My Account, Subscriptions, Sign Out)

    txt_profileTitle_xpath = '//button[@id="composition-button"]'
    button_myAccount_xpath = '//h4[normalize-space()="My Account"]'
    button_subscription_xpath = '//h4[normalize-space()="Subscription"]'
    button_profileDropdown_xpath = '//button[@id = "composition-button"]'
    button_signout_xpath = '//button[normalize-space()="Sign Out"]'

    def __init__(self, driver):
        self.driver = driver

    def clickProfileDropdown(self):
        self.driver.find_element(
            By.XPATH, self.button_profileDropdown_xpath).click()

    def clickSignout(self):
        self.driver.find_element(By.XPATH, self.button_signout_xpath).click()

    def clickMyAccount(self):
        self.driver.find_element(By.XPATH, self.button_myAccount_xpath).click()

    def clickSubscription(self):
        self.driver.find_element(
            By.XPATH, self.button_subscription_xpath).click()

    # check profile title is displayed
    def isProfileTitleDisplayed(self):
        return self.driver.find_element(By.XPATH, self.txt_profileTitle_xpath).is_displayed()
