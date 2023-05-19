from selenium.webdriver.common.by import By


class FinalDraftFirstDraftGen:
    # Final Draft First Draft Gen Page
    textbox_topic_xpath = '//input[@id="mui-64"]'
    txt_generatedText_xpath = '//div[@class="ql-editor"]'
    button_downloadDraft_xpath = '//button[normalize-space()="Download Draft"]'
    button_saveDraft_xpath = '//button[normalize-space()="Save Draft"]'
    button_rephrase_xpath = '//button[@id="rephrase"]'

    button_calculate_xpath = '//button[@id="calculateButton"]'
    txt_calculateScore_xpath = '//p[@class="MuiTypography-root MuiTypography-body1 percentageText fontFamilyInter fontWeight-600 css-9l3uo3"]'
    button_viewDetails_xpath = '//button[@id="viewDetails"]'
    button_viewDetailsClose_xpath = '//button[@class="MuiButtonBase-root MuiIconButton-root MuiIconButton-sizeMedium modalClose css-1yxmbwk"]'

    drp_reference_xpath = '//div[@class="MuiAccordionSummary-expandIconWrapper css-1fx8m19"]'
    lst_referenceCitations_xpath = '//div[@class="MuiAccordionDetails-root accordianBox-contentBox css-u7qq7e"]/div'
    txt_referenceNo_xpath = '//div[@class="MuiAccordionDetails-root accordianBox-contentBox css-u7qq7e"]/div[8]/p'
    txt_referenceText_xpath = '//div[@class="MuiAccordionDetails-root accordianBox-contentBox css-u7qq7e"]/div[8]/div/p/a'

    button_help_xpath = '//button[normalize-space()="Help"]'
    button_Xmark_xpath = '//div[@class="drawerClosebtnWrapper repurposeEdit MuiBox-root css-0"]'

    def __init__(self, driver):
        self.driver = driver

    def setTopic(self, topic):
        topic_element = self.driver.find_element(
            By.XPATH, self.textbox_topic_xpath)
        topic_element.clear()
        topic_element.send_keys(topic)

    def getGeneratedText(self):
        return self.driver.find_element(By.XPATH, self.txt_generatedText_xpath).text

    def clickDownloadDraft(self):
        self.driver.find_element(
            By.XPATH, self.button_downloadDraft_xpath).click()

    def clickSaveDraft(self):
        self.driver.find_element(By.XPATH, self.button_saveDraft_xpath).click()

    def clickRephrase(self):
        self.driver.find_element(By.XPATH, self.button_rephrase_xpath).click()

    # Calculate Score
    def clickCalculate(self):
        self.driver.find_element(By.XPATH, self.button_calculate_xpath).click()

    def getCalculateScore(self):
        return self.driver.find_element(By.XPATH, self.txt_calculateScore_xpath).text

    def clickViewDetails(self):
        self.driver.find_element(
            By.XPATH, self.button_viewDetails_xpath).click()

    # Reference & Citation
    def clickReferenceDropdown(self):
        self.driver.find_element(By.XPATH, self.drp_reference_xpath).click()

    def getCountReferenceCitations(self):
        return len(self.driver.find_elements(By.XPATH, self.lst_referenceCitations_xpath))

    def getReferenceText(self):
        return self.driver.find_element(By.XPATH, self.txt_referenceText_xpath).text

    def getReferenceNo(self):
        return self.driver.find_element(By.XPATH, self.txt_referenceNo_xpath).text

    # Help
    def clickHelp(self):
        self.driver.find_element(By.XPATH, self.button_help_xpath).click()

    def closeHelp(self):
        self.driver.find_element(By.XPATH, self.button_Xmark_xpath).click()
