from selenium.webdriver.common.by import By


class FirstDraftGenCurate:
    # First Draft Curate Page
    logo_grafi_xpath = '//img[@alt="grafi logo"]'
    link_firstDraftGenTab_xpath = '//a[normalize-space()="First Draft Generator"]'
    link_rephraserTab_xpath = '//a[normalize-space()="Rephraser"]'
    link_homeTab_xpath = '//a[normalize-space()="Home"]'

    txt_header_xpath = '//span[@class="fontWeight-700"]'

    txt_topic_xpath = '//p[contains(text(),"What topic do you want to write about?")]'
    textbox_topic_xpath = '(//input[@id="textBoxMedium"])[1]'

    txt_tone_xpath = '//p[normalize-space()="Tone"]'
    drp_tone_xpath = '//div[@id="mui-component-select-tone"]'
    select_tone_xpath = '//ul[@role="listbox"]/li'

    txt_readingLevel_xpath = '//p[normalize-space()="Reading Level"]'
    drp_readingLevel_xpath = '//div[@id="mui-component-select-readinglevel"]'
    select_readingLevel_xpath = '//ul[@role="listbox"]/li'

    txt_onlineSource_xpath = '//p[contains(normalize-space(),"Online Sources")]'
    textbox_onlineSource_xpath = '(//input[@id="textBoxMedium"])[2]'
    txt_addUrl_xpath = '//p[normalize-space()="Add URL"]'
    button_addUrl_xpath = '//button[normalize-space()="Add URL"]'

    txt_UploadableSources_xpath = '//p[contains(normalize-space(),"Uploadable Sources")]'
    txt_dragAndDrop_xpath = '//p[contains(text(),"Drag & Drop files here")]'
    button_browseFile_xpath = '//input[@accept=".pdf"]'

    button_next_xpath = '//button[normalize-space()="Next"]'

    def __init__(self, driver):
        self.driver = driver

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

    def getTextTopic(self):
        return self.driver.find_element(By.XPATH, self.txt_topic_xpath).text

    # get topic textbox placeholder
    def getTopicPlaceholder(self):
        return self.driver.find_element(By.XPATH, self.textbox_topic_xpath).get_attribute("placeholder")

    def setTopic(self, topic):
        topic_element = self.driver.find_element(
            By.XPATH, self.textbox_topic_xpath)
        topic_element.clear()
        topic_element.send_keys(topic)

    # is topic enabled
    def isTopicEnabled(self):
        return self.driver.find_element(By.XPATH, self.textbox_topic_xpath).is_enabled()

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
    def isToneEnabled(self):
        return self.driver.find_element(By.XPATH, self.drp_tone_xpath).is_enabled()

    def selectTone(self, tone):
        tone_elements = self.driver.find_elements(
            By.XPATH, self.select_tone_xpath)
        for tone_element in tone_elements:
            if tone_element.get_attribute("data-value") == tone:
                tone_element.click()
                break

    # get reading level text
    def getTextReadingLevel(self):
        return self.driver.find_element(By.XPATH, self.txt_readingLevel_xpath).text

    # is reading level enabled
    def isReadingLevelEnabled(self):
        return self.driver.find_element(By.XPATH, self.drp_readingLevel_xpath).is_enabled()

    # get reading level dropdown placeholder text
    def getReadingLevelPlaceholder(self):
        return self.driver.find_element(By.XPATH, self.drp_readingLevel_xpath).text

    # check all the reading level options available
    def getReadingLevelOptions(self):
        reading_level_elements = self.driver.find_elements(
            By.XPATH, self.select_readingLevel_xpath)
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

    # get online sources text
    def getTextOnlineSources(self):
        return self.driver.find_element(By.XPATH, self.txt_onlineSource_xpath).text

    # get online sources textbox placeholder text
    def getOnlineSourcesPlaceholder(self):
        return self.driver.find_element(By.XPATH, self.textbox_onlineSource_xpath).get_attribute("placeholder")

    # get add url button text
    def getTextAddUrl(self):
        return self.driver.find_element(By.XPATH, self.button_addUrl_xpath).text

    def setOnlineSource(self, online_source):
        online_source_element = self.driver.find_element(
            By.XPATH, self.textbox_onlineSource_xpath)
        online_source_element.clear()
        online_source_element.send_keys(online_source)

    def clickAddUrl(self):
        self.driver.find_element(By.XPATH, self.button_addUrl_xpath).click()

    # get uploadable sources text
    def getTextUploadableSources(self):
        return self.driver.find_element(By.XPATH, self.txt_uploadableSource_xpath).text

    # get drag and drop text
    def getTextDragAndDrop(self):
        return self.driver.find_element(By.XPATH, self.txt_dragAndDrop_xpath).text

    # get browse file button text
    def getTextBrowseFile(self):
        return self.driver.find_element(By.XPATH, self.button_browseFile_xpath).text

    # add files from local machine
    def addBrowseFile(self, file_path):
        self.driver.find_element(
            By.XPATH, self.button_browseFile_xpath).send_keys(file_path)

    # get next button text
    def getTextNextButton(self):
        return self.driver.find_element(By.XPATH, self.button_next_xpath).text

    # is next button enabled
    def isNextButtonEnabled(self):
        return self.driver.find_element(By.XPATH, self.button_next_xpath).is_enabled()

    # click next button
    def clickNext(self):
        self.driver.find_element(By.XPATH, self.button_next_xpath).click()

    # enter all the details in the curate first draft gen page
    def enterCurateFirstDraftGenDetails(self, topic, tone, reading_level, online_source="", file_path=""):
        self.setTopic(topic)
        self.selectTone(tone)
        self.selectReadingLevel(reading_level)
        if online_source != "":
            self.setOnlineSource(online_source)
            self.clickAddUrl()
        if file_path != "":
            self.addBrowseFile(file_path)
        self.clickNext()