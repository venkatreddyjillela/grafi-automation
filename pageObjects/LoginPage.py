from selenium.webdriver.common.by import By


class LoginPage:
    # Login Page
    textbox_email_xpath = '//input[@id="username"]'
    textbox_password_xpath = '//input[@id="password"]'
    button_login_xpath = '//input[@type="submit"]'
    button_signout_dropdown_xpath = '//button[@id = "composition-button"]'
    button_signout_xpath = '//button[normalize-space()="Sign Out"]'

    def __init__(self, driver):
        self.driver = driver

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

    def clickSignoutDropdown(self):
        self.driver.find_element(
            By.XPATH, self.button_signout_dropdown_xpath).click()

    def clickSignout(self):
        self.driver.find_element(By.XPATH, self.button_signout_xpath).click()
