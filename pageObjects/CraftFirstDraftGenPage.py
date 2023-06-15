from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CraftFirstDraftGen:
    # First Draft Craft Page

    # logo on the page
    logo_grafi_xpath = '//img[@alt="grafi logo"]'

    # Tabs on the page
    link_firstDraftGenTab_xpath = '//a[normalize-space()="First Draft Generator"]'
    link_rephraserTab_xpath = '//a[normalize-space()="Rephraser"]'
    link_homeTab_xpath = '//a[normalize-space()="Home"]'

    # Header
    hdr_yourPieceOutline_xpath = '//p[@class="MuiTypography-root MuiTypography-body1 MuiTypography-alignCenter outlineHeader fontFamilyPoppins fontWeight-600 css-1oy63y8"]'

    # Seo Subtopics
    txt_seoSubtopicsTitle_xpath = "//p[normalize-space()='Subtopic recommendations from Grafi']"
    lst_seoSubtopics_xpath = '(//div[@class="MuiGrid-root boxContent null css-rfnosa"])[2]/div'
    txt_subtopicNo_xpath = '(//div[@class="MuiGrid-root boxContent null css-rfnosa"])[1]/div[8]/div[1]/p'
    txt_subtopicText_xpath = '(//div[@class="MuiGrid-root boxContent null css-rfnosa"])[1]/div[8]/div[2]/p'
    button_plus_xpath = '(//div[@class="MuiGrid-root boxContent null css-rfnosa"])[1]/div[8]/div[3]/button'

    # Grafi Subtopics
    txt_grafiSubtopicsTitle_xpath = '//p[contains(text(),"Subtopic recommendations based on GRAFI")]'
    lst_grafiSubtopics_xpath = '(//div[@class="MuiGrid-root MuiGrid-item MuiGrid-grid-xs-12 boxOutline css-15j76c0"])[2]/div/div'
    txt_grafiSubtopicNo_xpath = '(//div[@class="MuiGrid-root MuiGrid-item MuiGrid-grid-xs-12 boxOutline css-15j76c0"])[2]/div/div[8]/div[1]/p'
    txt_grafiSubtopicText_xpath = '(//div[@class="MuiGrid-root MuiGrid-item MuiGrid-grid-xs-12 boxOutline css-15j76c0"])[2]/div/div[8]/div[2]/p'
    button_plus_xpath = '(//div[@class="MuiGrid-root MuiGrid-item MuiGrid-grid-xs-12 boxOutline css-15j76c0"])[2]/div/div[8]/div[3]/button'

    # References
    txt_referencesTitle_xpath = "//p[normalize-space()='Subtopic recommendations from Grafi']"
    lst_references_xpath = '(//div[@class="MuiGrid-root MuiGrid-container boxContent null css-1d3bbye"])[1]/div'
    txt_referenceNo_xpath = '(//div[@class="MuiGrid-root MuiGrid-container boxContent null css-1d3bbye"])[1]/div[8]/div[1]/p'
    txt_referenceText_xpath = '(//div[@class="MuiGrid-root MuiGrid-container boxContent null css-1d3bbye"])[1]/div[8]/div[2]/a'
    txt_referenceSource_xpath = '(//div[@class="MuiGrid-root MuiGrid-container boxContent null css-1d3bbye"])[1]/div[8]/div[3]/p'
    checkbox_reference_xpath = '(//div[@class="MuiGrid-root MuiGrid-container boxContent null css-1d3bbye"])[1]/div[8]/div[4]/span'

    # add subtopic
    txt_addSubtopicTitle_xpath = "//p[normalize-space()='Craft Your Outline Here']"
    textbox_subtopic_xpath = '//input[@id="craftTopicsInput"]'
    button_addSubtopic_xpath = '//button[@id="addSubtopicButton"]'

    # word count dropdown
    txt_wordCountTitle_xpath = "//p[@class='MuiFormHelperText-root']"
    dropdown_wordCount_xpath = '//div[@id="mui-component-select-wordCountDropDown"]'
    lst_wordCount_xpath = '//ul[@role="listbox"]/li'

    # create your outline
    txt_createYourOutlineTitle_xpath = "//h1[normalize-space()='Create your outline']"

    # Generate button
    button_generate_xpath = '//button[normalize-space()="Generate"]'

    # Back button
    button_back_xpath = '//button[@id="craftTopicsBackButton"]'

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
        self.wait2 = WebDriverWait(self.driver, 300)


    def isLogoDisplayed(self):
        return self.driver.find_element(By.XPATH, self.logo_grafi_xpath).is_displayed()

    # click Home tab
    def clickHomeTab(self):
        self.driver.find_element(By.XPATH, self.link_homeTab_xpath).click()

    # click Rephraser tab
    def clickRephraserTab(self):
        self.driver.find_element(
            By.XPATH, self.link_rephraserTab_xpath).click()

    # click First Draft Generator tab
    def clickFirstDraftGenTab(self):
        self.driver.find_element(
            By.XPATH, self.link_firstDraftGenTab_xpath).click()

    # Header
    def getYourPieceOutlineHeader(self):
        return self.driver.find_element(By.XPATH, self.hdr_yourPieceOutline_xpath).text

    # Seo Subtopics
    def getSeoSubtopicsTitle(self):
        return self.driver.find_element(By.XPATH, self.txt_seoSubtopicsTitle_xpath).text

    def getCountSeoSubtopics(self):
        return len(self.driver.find_elements(By.XPATH, self.lst_seoSubtopics_xpath))

    def getAllSeoSubtopicsText(self, countSeoSubtopics):
        lst_subtopics = []
        for i in range(1, countSeoSubtopics+1):
            subtopic_text = self.driver.find_element(
                By.XPATH, self.txt_subtopicText_xpath.replace('8', str(i))).text
            lst_subtopics.append(subtopic_text)
        return lst_subtopics

    def getSeoSubtopicText(self, subtopicNo):
        return self.driver.find_element(By.XPATH, self.txt_subtopicText_xpath.replace('8', str(subtopicNo))).text

    def addSeoSubtopic(self, subtopicNo):
        self.driver.find_element(
            By.XPATH, self.button_plus_xpath.replace('8', str(subtopicNo))).click()

    def getSeoSubtopicNo(self, subtopicNo):
        return self.driver.find_element(By.XPATH, self.txt_subtopicNo_xpath.replace('8', str(subtopicNo))).text

    def addFirstSeoSubtopic(self):
        self.driver.find_element(
            By.XPATH, self.button_plus_xpath.replace('8', str(1))).click()

    def addLastSeoSubtopic(self, countSeoSubtopics):
        self.driver.find_element(By.XPATH, self.button_plus_xpath.replace(
            '8', str(countSeoSubtopics))).click()

    # Grafi Subtopics
    def getGrafiSubtopicsTitle(self):
        return self.driver.find_element(By.XPATH, self.txt_grafiSubtopicsTitle_xpath).text

    def getCountGrafiSubtopics(self):
        return len(self.driver.find_elements(By.XPATH, self.lst_grafiSubtopics_xpath))

    def getAllGrafiSubtopicsText(self, countGrafiSubtopics):
        lst_subtopics = []
        for i in range(1, countGrafiSubtopics+1):
            subtopic_text = self.driver.find_element(
                By.XPATH, self.txt_grafiSubtopicText_xpath.replace('8', str(i))).text
            lst_subtopics.append(subtopic_text)
        return lst_subtopics

    def getGrafiSubtopicText(self, subtopicNo):
        return self.driver.find_element(By.XPATH, self.txt_grafiSubtopicText_xpath.replace('8', str(subtopicNo))).text

    def addGrafiSubtopic(self, subtopicNo):
        self.driver.find_element(
            By.XPATH, self.button_plus_xpath.replace('8', str(subtopicNo))).click()

    def getGrafiSubtopicNo(self, subtopicNo):
        return self.driver.find_element(By.XPATH, self.txt_grafiSubtopicNo_xpath.replace('8', str(subtopicNo))).text

    def addFirstGrafiSubtopic(self):
        self.driver.find_element(
            By.XPATH, self.button_plus_xpath.replace('8', str(1))).click()

    def addLastGrafiSubtopic(self, countGrafiSubtopics):
        self.driver.find_element(By.XPATH, self.button_plus_xpath.replace(
            '8', str(countGrafiSubtopics))).click()

    # References
    def getReferencesTitle(self):
        return self.driver.find_element(By.XPATH, self.txt_referencesTitle_xpath).text

    def getCountReferences(self):
        return len(self.driver.find_elements(By.XPATH, self.lst_references_xpath))

    def getAllReferencesText(self, countReferences):
        lst_references = []
        for i in range(1, countReferences+1):
            reference_text = self.driver.find_element(
                By.XPATH, self.txt_referenceText_xpath.replace('8', str(i))).text
            lst_references.append(reference_text)
        return lst_references

    def getReferenceText(self, referenceNo):
        return self.driver.find_element(By.XPATH, self.txt_referenceText_xpath.replace('8', str(referenceNo))).text

    def getReferenceSource(self, referenceNo):
        return self.driver.find_element(By.XPATH, self.txt_referenceSource_xpath.replace('8', str(referenceNo))).text

    def getReferenceNo(self, referenceNo):
        return self.driver.find_element(By.XPATH, self.txt_referenceNo_xpath.replace('8', str(referenceNo))).text

    def addReference(self, referenceNo):
        reference_checkbox_element = self.driver.find_element(
            By.XPATH, self.checkbox_reference_xpath.replace('8', str(referenceNo)))
        if not reference_checkbox_element.is_selected():
            reference_checkbox_element.click()

    def removeReference(self, referenceNo):
        reference_checkbox_element = self.driver.find_element(
            By.XPATH, self.checkbox_reference_xpath.replace('8', str(referenceNo)))
        if reference_checkbox_element.is_selected():
            reference_checkbox_element.click()

    def removeAllPmcReferences(self):
        count_references = self.getCountReferences()
        for i in range(1, count_references+1):
            reference_source = self.getReferenceSource(i)
            if reference_source == 'Source - PubMed Central':
                self.removeReference(i)

    def removeAllMedlineReferences(self):
        count_references = self.getCountReferences()
        for i in range(1, count_references+1):
            reference_source = self.getReferenceSource(i)
            if reference_source == 'Source - Medline plus-GHR':
                self.removeReference(i)

    def removeAllUserAddedReferences(self):
        count_references = self.getCountReferences()
        for i in range(1, count_references+1):
            reference_source = self.getReferenceSource(i)
            if reference_source == 'Source - User Supplied':
                self.removeReference(i)

    def removeAllReferences(self):
        count_references = self.getCountReferences()
        for i in range(1, count_references+1):
            self.removeReference(i)

    def addAllUserAddedReferences(self):
        count_references = self.getCountReferences()
        for i in range(1, count_references+1):
            reference_source = self.getReferenceSource(i)
            if reference_source == 'Source - User Supplied':
                self.addReference(i)

    def addAllPmcReferences(self):
        count_references = self.getCountReferences()
        for i in range(1, count_references+1):
            reference_source = self.getReferenceSource(i)
            if reference_source == 'Source - PubMed Central':
                self.addReference(i)

    def addAllMedlineReferences(self):
        count_references = self.getCountReferences()
        for i in range(1, count_references+1):
            reference_source = self.getReferenceSource(i)
            if reference_source == 'Source - Medline plus-GHR':
                self.addReference(i)

    # Own subtopic
    def getAddSubtopicTitle(self):
        return self.driver.find_element(By.XPATH, self.txt_addSubtopicTitle_xpath).text

    def setSubtopic(self, subtopic_text):
        subtopic_element = self.driver.find_element(
            By.XPATH, self.txt_subtopic_xpath)
        subtopic_element.clear()
        subtopic_element.send_keys(subtopic_text)

    def clickAddSubtopic(self):
        self.driver.find_element(
            By.XPATH, self.button_addSubtopic_xpath).click()

    # Word count
    def getWordCountTitle(self):
        return self.driver.find_element(By.XPATH, self.txt_wordCountTitle_xpath).text

    def clickWordCountDropdown(self):
        self.driver.find_element(
            By.XPATH, self.dropdown_wordCount_xpath).click()

    def selectWordCount(self, word_count):
        word_count_elements = self.driver.find_elements(
            By.XPATH, self.lst_wordCount_xpath)
        for word_count_element in word_count_elements:
            if word_count_element.text == word_count:
                word_count_element.click()
                break

    # create your timeline
    def getTimelineTitle(self):
        return self.driver.find_element(By.XPATH, self.txt_createYourOutlineTitle_xpath).text

    # Generate button
    def clickGenerate(self):
        self.driver.find_element(By.XPATH, self.button_generate_xpath).click()

    # Back button
    def clickBack(self):
        self.driver.find_element(By.XPATH, self.button_back_xpath).click()

        # wait for home page to load
    def waitForHomePageToLoad(self):
        self.wait.until(EC.url_contains("home"))

    # wait for Rephraser page to load
    def waitForRephraserPageToLoad(self):
        self.wait.until(EC.url_contains("repurpose"))

    # wait for Curate page to load
    def waitForCuratePageToLoad(self):
        self.wait.until(EC.url_contains("inputContent"))

    # wait for final draft page to load
    def waitForFinalDraftPageToLoad(self):
        self.wait.until(EC.url_contains("inputContent/draft"))
