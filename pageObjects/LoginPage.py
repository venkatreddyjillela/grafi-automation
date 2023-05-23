from selenium.webdriver.common.by import By


class LoginPage:
    # Login Page
    txt_title_xpath = '//h1[@id="kc-page-title"]'
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

    def getTitle(self):
        return self.driver.find_element(By.XPATH, self.txt_title_xpath).text

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

    def clickLogin(self):
        self.driver.find_element(By.XPATH, self.button_login_xpath).click()

    def clickForgotPassword(self):
        self.driver.find_element(
            By.XPATH, self.link_forgotPassword_xpath).click()

    def getNewUserText(self):
        return self.driver.find_element(By.XPATH, self.txt_newUser_xpath).text

    def clickRegister(self):
        self.driver.find_element(By.XPATH, self.link_register_xpath).click()

    # check logo is displayed
    def isLogoDisplayed(self):
        return self.driver.find_element(By.XPATH, self.img_logo_xpath).is_displayed()

    def getLogoText(self):
        return self.driver.find_element(By.XPATH, self.txt_logo_xpath).text

    def isLoginButtonEnabled(self):
        return self.driver.find_element(By.XPATH, self.button_login_xpath).is_enabled()
