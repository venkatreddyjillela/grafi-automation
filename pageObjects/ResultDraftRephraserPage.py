from selenium.webdriver.common.by import By

class ResultDraftRephraser:
    # Result Draft Rephraser Page
    textbox_title_xpath = '//input[@id="mui-64"]'
    txt_generatedText_xpath = '//div[@class="ql-editor"]'
    button_downloadDraft_xpath = '//button[normalize-space()="Download Draft"]'
    button_saveDraft_xpath = '//button[normalize-space()="Save Draft"]'
    button_rephrase_xpath = '//button[@id="rephrase"]'

    button_calculate_xpath = '//button[@id="calculateButton"]'
    txt_calculateScore_xpath = '//p[@class="MuiTypography-root MuiTypography-body1 percentageText fontFamilyInter fontWeight-600 css-9l3uo3"]'
    button_viewDetails_xpath = '//button[@id="viewDetails"]'
    button_viewDetailsClose_xpath = '//button[@class="MuiButtonBase-root MuiIconButton-root MuiIconButton-sizeMedium modalClose css-1yxmbwk"]'

    button_tips_xpath = '//button[normalize-space()="Tips"]'
    button_tipsClose_xpath = '//div[@class="drawerClosebtnWrapper repurposeEdit MuiBox-root css-0"]'
    


    def __init__(self, driver):
        self.driver = driver

    def setTitle(self, title):
        title_element = self.driver.find_element(
            By.XPATH, self.textbox_title_xpath)
        title_element.clear()
        title_element.send_keys(title)

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
        self.driver.find_element(By.XPATH, self.button_viewDetails_xpath).click()

    def clickViewDetailsClose(self):
        self.driver.find_element(By.XPATH, self.button_viewDetailsClose_xpath).click()

    # Tips
    def clickTips(self):
        self.driver.find_element(By.XPATH, self.button_tips_xpath).click()

    def clickTipsClose(self):
        self.driver.find_element(By.XPATH, self.button_tipsClose_xpath).click()
        

