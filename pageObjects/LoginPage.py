from selenium.webdriver.common.by import By


class LoginPage:
    # Login Page
    txt_loginHeader_xpath = '//h1[@id="kc-page-title"]'
    txt_emailLabel_xpath = '//label[normalize-space()="Email"]'
    txt_passwordLabel_xpath = '//label[normalize-space()="Password"]'
    textbox_email_xpath = '//input[@id="username"]'
    textbox_password_xpath = '//input[@id="password"]'
    button_login_xpath = '//input[@type="submit"]'
    link_forgotPassword_xpath = '//a[normalize-space()="Forgot Password?"]'
    txt_newUser_xpath = '//div[@id="kc-info"]//span[1]'
    link_register_xpath = '//a[normalize-space()="Register"]'
    img_logo_xpath = '//img[@alt="Logo"]'
    txt_logo_xpath = '//div[@id="kc-logo-text"]'

    def __init__(self, driver):
        self.driver = driver

    def getLoginHeader(self):
        return self.driver.find_element(By.XPATH, self.txt_loginHeader_xpath).text
    
    def getEmailLabel(self):
        return self.driver.find_element(By.XPATH, self.txt_emailLabel_xpath).text
    
    def getPasswordLabel(self):
        return self.driver.find_element(By.XPATH, self.txt_passwordLabel_xpath).text

    def setEmail(self, email):
        email_element = self.driver.find_element(
            By.XPATH, self.textbox_email_xpath)
        email_element.clear()
        email_element.send_keys(email)

    def setPassword(self, password):
        password_element = self.driver.find_element(
            By.XPATH, self.textbox_password_xpath)
        password_element.clear()
        password_element.send_keys(password)

    # get login button text
    def getLoginButtonText(self):
        return self.driver.find_element(
            By.XPATH, self.button_login_xpath).get_attribute("value")

    def clickLogin(self):
        self.driver.find_element(By.XPATH, self.button_login_xpath).click()

    # get forgot password link text
    def getForgotPasswordText(self):
        return self.driver.find_element(
            By.XPATH, self.link_forgotPassword_xpath).text

    def clickForgotPassword(self):
        self.driver.find_element(
            By.XPATH, self.link_forgotPassword_xpath).click()

    def getNewUserText(self):
        return self.driver.find_element(By.XPATH, self.txt_newUser_xpath).text
    
    # get register link text
    def getRegisterLinkText(self):
        return self.driver.find_element(By.XPATH, self.link_register_xpath).text

    def clickRegister(self):
        self.driver.find_element(By.XPATH, self.link_register_xpath).click()

    # check logo is displayed
    def isLogoDisplayed(self):
        return self.driver.find_element(By.XPATH, self.img_logo_xpath).is_displayed()

    def getLogoText(self):
        return self.driver.find_element(By.XPATH, self.txt_logo_xpath).text

    def isLoginButtonEnabled(self):
        return self.driver.find_element(By.XPATH, self.button_login_xpath).is_enabled()
    
    # login button dipalyed or not
    def isLoginButtonDisplayed(self):
        return self.driver.find_element(By.XPATH, self.button_login_xpath).is_displayed()
    
    def userLogin(self, email, password):
        self.setEmail(email)
        self.setPassword(password)
        self.clickLogin()

    # email text box placeholder
    def getEmailPlaceholder(self):
        return self.driver.find_element(By.XPATH, self.textbox_email_xpath).get_attribute("placeholder")
    
    # password text box placeholder
    def getPasswordPlaceholder(self):
        return self.driver.find_element(By.XPATH, self.textbox_password_xpath).get_attribute("placeholder")
    


    
