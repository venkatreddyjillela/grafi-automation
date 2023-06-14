from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Subscription:
    # Subscription Page
    logo_grafi_xpath = '//img[@alt="grafi logo"]'
    link_firstDraftGenTab_xpath = '//a[normalize-space()="First Draft Generator"]'
    link_rephraserTab_xpath = '//a[normalize-space()="Rephraser"]'
    link_homeTab_xpath = '//a[normalize-space()="Home"]'

    button_myAccount_xpath = '//a[@href="/myAccount"]'
    button_subscription_xpath = '//button[normalize-space()="Subscription"]'

    txt_currentPlan_xpath = '//h3[normalize-space()="Current Plan"]'
    drp_currentPlan_xpath = '(//div[@id="panel1a-header"])[1]/div[2]'

    txt_monthlyUsageHistory_xpath = '//h3[normalize-space()="Monthly Usage History"]'
    drp_monthlyUsageHistory_xpath = '(//div[@id="panel1a-header"])[2]/div[2]'

    txt_paymentHistory_xpath = '//h3[normalize-space()="Payment History"]'
    drp_paymentHistory_xpath = '(//div[@id="panel1a-header"])[3]/div[2]'


    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)