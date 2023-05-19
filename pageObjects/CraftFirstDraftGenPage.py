from selenium.webdriver.common.by import By


class CraftFirstDraftGen:
    # First Draft Craft Page

    # Header
    hdr_yourPieceOutline_xpath = '//p[@class="MuiTypography-root MuiTypography-body1 MuiTypography-alignCenter outlineHeader fontFamilyPoppins fontWeight-600 css-1oy63y8"]'

    # Seo Subtopics
    lst_seoSubtopics_xpath = '(//div[@class="MuiGrid-root boxContent null css-rfnosa"])[2]/div'
    txt_subtopicNo_xpath = '(//div[@class="MuiGrid-root boxContent null css-rfnosa"])[1]/div[8]/div[1]/p'
    txt_subtopicText_xpath = '(//div[@class="MuiGrid-root boxContent null css-rfnosa"])[1]/div[8]/div[2]/p'
    button_plus_xpath = '(//div[@class="MuiGrid-root boxContent null css-rfnosa"])[1]/div[8]/div[3]/button'

    # Grafi Subtopics
    lst_grafiSubtopics_xpath = '(//div[@class="MuiGrid-root MuiGrid-item MuiGrid-grid-xs-12 boxOutline css-15j76c0"])[2]/div/div'
    txt_grafiSubtopicNo_xpath = '(//div[@class="MuiGrid-root MuiGrid-item MuiGrid-grid-xs-12 boxOutline css-15j76c0"])[2]/div/div[8]/div[1]/p'
    txt_grafiSubtopicText_xpath = '(//div[@class="MuiGrid-root MuiGrid-item MuiGrid-grid-xs-12 boxOutline css-15j76c0"])[2]/div/div[8]/div[2]/p'
    button_plus_xpath = '(//div[@class="MuiGrid-root MuiGrid-item MuiGrid-grid-xs-12 boxOutline css-15j76c0"])[2]/div/div[8]/div[3]/button'

    # References
    lst_references_xpath = '(//div[@class="MuiGrid-root MuiGrid-container boxContent null css-1d3bbye"])[1]/div'
    txt_referenceNo_xpath = '(//div[@class="MuiGrid-root MuiGrid-container boxContent null css-1d3bbye"])[1]/div[8]/div[1]/p'
    txt_referenceText_xpath = '(//div[@class="MuiGrid-root MuiGrid-container boxContent null css-1d3bbye"])[1]/div[8]/div[2]/a'
    txt_referenceSource_xpath = '(//div[@class="MuiGrid-root MuiGrid-container boxContent null css-1d3bbye"])[1]/div[8]/div[3]/p'
    checkbox_reference_xpath = '(//div[@class="MuiGrid-root MuiGrid-container boxContent null css-1d3bbye"])[1]/div[8]/div[4]/span'

    # add subtopic
    textbox_subtopic_xpath = '//input[@id="craftTopicsInput"]'
    button_addSubtopic_xpath = '//button[@id="addSubtopicButton"]'

    # word count dropdown
    dropdown_wordCount_xpath = '//div[@id="mui-component-select-wordCountDropDown"]'
    lst_wordCount_xpath = '//ul[@role="listbox"]/li'

    # Generate button
    button_generate_xpath = '//button[normalize-space()="Generate"]'

    # Back button
    button_back_xpath = '//button[@id="craftTopicsBackButton"]'

    def __init__(self, driver):
        self.driver = driver

    # Header
    def getYourPieceOutlineHeader(self):
        return self.driver.find_element(By.XPATH, self.hdr_yourPieceOutline_xpath).text

    # Seo Subtopics
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
    def setSubtopic(self, subtopic_text):
        subtopic_element = self.driver.find_element(
            By.XPATH, self.txt_subtopic_xpath)
        subtopic_element.clear()
        subtopic_element.send_keys(subtopic_text)

    def clickAddSubtopic(self):
        self.driver.find_element(
            By.XPATH, self.button_addSubtopic_xpath).click()

    # Word count
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

    # Generate button
    def clickGenerate(self):
        self.driver.find_element(By.XPATH, self.button_generate_xpath).click()

    # Back button
    def clickBack(self):
        self.driver.find_element(By.XPATH, self.button_back_xpath).click()
