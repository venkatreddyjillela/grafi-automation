from selenium.webdriver.common.by import By


class ForgotPasswordPage:
    # Registration Page
    txt_title_xpath = '//h1[@id="kc-page-title"]'

    def __init__(self, driver):
        self.driver = driver

    def getTitle(self):
        return self.driver.find_element(By.XPATH, self.txt_title_xpath).text
