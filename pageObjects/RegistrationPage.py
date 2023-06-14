from selenium.webdriver.common.by import By


class RegistrationPage:
    # Registration Page
    txt_title_xpath = '//h1[@id="kc-page-title"]'

    txt_firstName_xpath = '//label[normalize-space()="First name"]'
    textbox_firstName_xpath = '//input[@id="firstName"]'
    txt_errorFirstName_xpath = '//span[@id="input-error-firstname"]'

    txt_lastName_xpath = '//label[normalize-space()="Last name"]'
    textbox_lastName_xpath = '//input[@id="lastName"]'
    txt_errorLastName_xpath = '//span[@id="input-error-lastname"]'

    txt_email_xpath = '//label[normalize-space()="Email"]'
    textbox_email_xpath = '//input[@id="email"]'
    txt_errorEmail_xpath = '//span[@id="input-error-email"]'

    txt_password_xpath = '//label[normalize-space()="Password"]'
    textbox_password_xpath = '//input[@id="password"]'
    txt_errorPassword_xpath = '//span[@id="input-error-password"]'

    txt_confirmPassword_xpath = '//label[normalize-space()="Confirm password"]'
    textbox_confirmPassword_xpath = '//input[@id="password-confirm"]'

    button_register_xpath = '//input[@value="Register"]'

    link_back_xpath = '//a[normalize-space()="Back"]'

    def __init__(self, driver):
        self.driver = driver

    def getTitle(self):
        return self.driver.find_element(By.XPATH, self.txt_title_xpath).text
