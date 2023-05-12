from selenium.webdriver.common.by import By


class Rephraser:
    # Rephraser Page

    # Header
    txt_header_xpath = '//h4[@aria-label="genarate ideas and content using porsonalised AI assistance"]'
    textbox_uploadUrl_xpath = '//input[@id="textBoxMedium"]'
    drp_tone_xpath = '//div[@id="mui-component-select-tone"]'
    select_tone_xpath = '//ul[@role="listbox"]/li'
    drp_reading_level_xpath = '//div[@id="mui-component-select-readinglevel"]'
    select_reading_level_xpath = '//ul[@role="listbox"]/li'
    button_submit_xpath = '//button[normalize-space()="Submit"]'

    def __init__(self, driver):
        self.driver = driver

    def getHeader(self):
        return self.driver.find_element(By.XPATH, self.txt_header_xpath).text

    def setUploadUrl(self, uploadUrl):
        uploadUrl_element = self.driver.find_element(
            By.XPATH, self.textbox_uploadUrl_xpath)
        uploadUrl_element.clear()
        uploadUrl_element.send_keys(uploadUrl)

    def clickTone(self):
        self.driver.find_element(By.XPATH, self.drp_tone_xpath).click()

    def selectTone(self, tone):
        tone_elements = self.driver.find_elements(
            By.XPATH, self.select_tone_xpath)
        for tone_element in tone_elements:
            if tone_element.get_attribute("data-value") == tone:
                tone_element.click()
                break

    def clickReadingLevel(self):
        self.driver.find_element(
            By.XPATH, self.drp_reading_level_xpath).click()

    def selectReadingLevel(self, reading_level):
        reading_level_elements = self.driver.find_elements(
            By.XPATH, self.select_reading_level_xpath)
        for reading_level_element in reading_level_elements:
            value = reading_level_element.get_attribute("data-value")
            if value == reading_level:
                reading_level_element.click()
                break

    def clickSubmit(self):
        self.driver.find_element(By.XPATH, self.button_submit_xpath).click()
