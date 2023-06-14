from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Rephraser:
    # Rephraser Page
    logo_grafi_xpath = '//img[@alt="grafi logo"]'
    link_firstDraftGenTab_xpath = '//a[normalize-space()="First Draft Generator"]'
    link_rephraserTab_xpath = '//a[normalize-space()="Rephraser"]'
    link_homeTab_xpath = '//a[normalize-space()="Home"]'

    # Header
    txt_header_xpath = """//h4[@aria-label="genarate ideas and content using porsonalised AI assistance"]"""

    txt_uploadUrlText_xpath = '//div[@for="url"]'
    textbox_uploadUrl_xpath = '//input[@id="textBoxMedium"]'

    txt_tone_xpath = '//label[@aria-label="tone"]'
    drp_tone_xpath = '//div[@id="mui-component-select-tone"]'
    select_tone_xpath = '//ul[@role="listbox"]/li'

    txt_readingLevel_xpath = '//label[@aria-label="readinglevel"]'
    drp_readingLevel_xpath = '//div[@id="mui-component-select-readinglevel"]'
    select_readingLevel_xpath = '//ul[@role="listbox"]/li'
    button_submit_xpath = '//button[normalize-space()="Submit"]'

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 30)

    def isLogoDisplayed(self):
        return self.driver.find_element(By.XPATH, self.logo_grafi_xpath).is_displayed()

    def getTextFirstDraftGenTab(self):
        return self.driver.find_element(By.XPATH, self.link_firstDraftGenTab_xpath).text

    def getTextRephraserTab(self):
        return self.driver.find_element(By.XPATH, self.link_rephraserTab_xpath).text

    def getTextHomeTab(self):
        return self.driver.find_element(By.XPATH, self.link_homeTab_xpath).text

    def isFirstDraftGenTabSelected(self):
        return self.driver.find_element(By.XPATH, self.link_firstDraftGenTab_xpath).get_attribute("aria-selected")

    def isRephraserTabSelected(self):
        return self.driver.find_element(By.XPATH, self.link_rephraserTab_xpath).get_attribute("aria-selected")

    def isHomeTabSelected(self):
        return self.driver.find_element(By.XPATH, self.link_homeTab_xpath).get_attribute("aria-selected")

    def clickFirstDraftGenTab(self):
        self.driver.find_element(
            By.XPATH, self.link_firstDraftGenTab_xpath).click()

    def clickRephraserTab(self):
        self.driver.find_element(
            By.XPATH, self.link_rephraserTab_xpath).click()

    def clickHomeTab(self):
        self.driver.find_element(By.XPATH, self.link_homeTab_xpath).click()

    def getHeaderText(self):
        return self.driver.find_element(By.XPATH, self.txt_header_xpath).text

    def getUploadUrlText(self):
        return self.driver.find_element(By.XPATH, self.txt_uploadUrlText_xpath).text

     # is url text box enabled
    def isUploadUrlTextBoxEnabled(self):
        return self.driver.find_element(By.XPATH, self.textbox_uploadUrl_xpath).is_enabled()

    # get topic textbox placeholder
    def getUploadUrlTextBoxPlaceholder(self):
        return self.driver.find_element(By.XPATH, self.textbox_uploadUrl_xpath).get_attribute("placeholder")

    def setUploadUrl(self, uploadUrl):
        uploadUrl_element = self.driver.find_element(
            By.XPATH, self.textbox_uploadUrl_xpath)
        uploadUrl_element.clear()
        uploadUrl_element.send_keys(uploadUrl)

    # get tone text
    def getTextTone(self):
        return self.driver.find_element(By.XPATH, self.txt_tone_xpath).text

    # get tone dropdown placeholder text
    def getTonePlaceholder(self):
        return self.driver.find_element(By.XPATH, self.drp_tone_xpath).text

    # check all the tone options available
    def getToneOptions(self):
        tone_elements = self.driver.find_elements(
            By.XPATH, self.select_tone_xpath)
        tone_options = []
        for tone_element in tone_elements:
            tone_options.append(tone_element.get_attribute("data-value"))
        return tone_options

    def clickTone(self):
        self.driver.find_element(By.XPATH, self.drp_tone_xpath).click()

    # is tone enabled
    def isToneDropDownEnabled(self):
        return self.driver.find_element(By.XPATH, self.drp_tone_xpath).get_attribute("aria-disabled")

    def selectTone(self, tone):
        # tone_elements = self.driver.find_elements(
        #     By.XPATH, self.select_tone_xpath)
        # use explicit wait
        tone_elements = self.wait.until(EC.presence_of_all_elements_located(
            (By.XPATH, self.select_tone_xpath)))
        for tone_element in tone_elements:
            if tone_element.get_attribute("data-value") == tone:
                tone_element.click()
                break

    # get reading level text
    def getTextReadingLevel(self):
        return self.driver.find_element(By.XPATH, self.txt_readingLevel_xpath).text

    # is reading level enabled
    def isReadingLevelDropDownEnabled(self):
        return self.driver.find_element(By.XPATH, self.drp_readingLevel_xpath).get_attribute("aria-disabled")

    # get reading level dropdown placeholder text
    def getReadingLevelPlaceholder(self):
        return self.driver.find_element(By.XPATH, self.drp_readingLevel_xpath).text

    # check all the reading level options available
    def getReadingLevelOptions(self):
        # reading_level_elements = self.driver.find_elements(
        #     By.XPATH, self.select_readingLevel_xpath)
        # use explicit wait
        reading_level_elements = self.wait.until(EC.presence_of_all_elements_located(
            (By.XPATH, self.select_readingLevel_xpath)))

        reading_level_options = []
        for reading_level_element in reading_level_elements:
            reading_level_options.append(
                reading_level_element.get_attribute("data-value"))
        return reading_level_options

    def clickReadingLevel(self):
        self.driver.find_element(
            By.XPATH, self.drp_readingLevel_xpath).click()

    def selectReadingLevel(self, reading_level):
        reading_level_elements = self.driver.find_elements(
            By.XPATH, self.select_readingLevel_xpath)
        for reading_level_element in reading_level_elements:
            value = reading_level_element.get_attribute("data-value")
            if value == reading_level:
                reading_level_element.click()
                break

    # get Submit button text
    def getTextSubmitButton(self):
        return self.driver.find_element(By.XPATH, self.button_submit_xpath).text

    # is Submit button enabled
    def isSubmitButtonEnabled(self):
        return self.driver.find_element(By.XPATH, self.button_submit_xpath).is_enabled()

    # click Submit button
    def clickSubmit(self):
        self.driver.find_element(By.XPATH, self.button_submit_xpath).click()

    def enterRephraserDetails(self, uploadUrl, tone, reading_level):
        self.setUploadUrl(uploadUrl)
        self.clickTone()
        self.selectTone(tone)
        self.clickReadingLevel()
        self.selectReadingLevel(reading_level)

    # wait for result draft rephraser page to load
    def waitForResultDraftRephraserPageToLoad(self):
        WebDriverWait(self.driver, 120).until(
            EC.url_contains("repurpose/Draft"))
