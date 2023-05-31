from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
import time
        


class CurateFirstDraftGen:
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

    txt_addOnlineSource_xpath = '(//div[@class="addedContentBox MuiBox-root css-0"])[1]//p'

    txt_UploadableSources_xpath = '//p[contains(normalize-space(),"Uploadable Sources")]'
    input_dragAndDrop_xpath = '//div[@class="fileDropBox MuiBox-root css-6g8s6k"]'
    txt_dragAndDrop_xpath = '//p[contains(text(),"Drag & Drop files here")]'
    button_browseFile_xpath = '//label[normalize-space()="Browse File"]'

    button_next_xpath = '//button[normalize-space()="Next"]'

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 30)
        # Initialize an ActionChains object
        self.actions = ActionChains(self.driver)

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

    # is topic text box enabled
    def isTopicTextBoxEnabled(self):
        return self.driver.find_element(By.XPATH, self.textbox_topic_xpath).is_enabled()

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

    # get online sources text
    def getTextOnlineSources(self):
        return self.driver.find_element(By.XPATH, self.txt_onlineSource_xpath).text

    # get online sources textbox placeholder text
    def getOnlineSourcesPlaceholder(self):
        return self.driver.find_element(By.XPATH, self.textbox_onlineSource_xpath).get_attribute("placeholder")

    # get add url button text
    def getTextAddUrl(self):
        return self.driver.find_element(By.XPATH, self.button_addUrl_xpath).text

    def isOnlineSourcesTextBoxEnabled(self):
        return self.driver.find_element(By.XPATH, self.textbox_onlineSource_xpath).is_enabled()

    def setOnlineSource(self, online_source):
        online_source_element = self.driver.find_element(
            By.XPATH, self.textbox_onlineSource_xpath)
        # Wait for the online_source_element text box to be able to accept data
        # online_source_element = self.wait.until(
        #     EC.element_to_be_clickable((By.XPATH, self.textbox_onlineSource_xpath)))
        online_source_element.clear()
        online_source_element.send_keys(online_source)

    def clickAddUrl(self):
        # self.driver.find_element(By.XPATH, self.button_addUrl_xpath).click()
        # wait for the button to be clickable
        self.wait.until(EC.element_to_be_clickable((By.XPATH, self.button_addUrl_xpath))).click()

    def isAddUrlButtonEnabled(self):
        return self.driver.find_element(By.XPATH, self.button_addUrl_xpath).is_enabled()
    
    # get online source added url for verification
    def getOnlineSourceAddedUrl(self):
        online_source_urls = self.driver.find_elements(By.XPATH, self.txt_addOnlineSource_xpath)
        urls = []
        for source_url in online_source_urls:
            urls.append(source_url.text)
        return urls
        

    # get uploadable sources text
    def getTextUploadableSources(self):
        return self.driver.find_element(By.XPATH, self.txt_UploadableSources_xpath).text

    # get drag and drop text
    def getTextDragAndDrop(self):
        return self.driver.find_element(By.XPATH, self.txt_dragAndDrop_xpath).text

    def isDragAndDropEnabled(self):
        return self.driver.find_element(By.XPATH, self.txt_dragAndDrop_xpath).is_enabled()

    # get browse file button text
    def getTextBrowseFile(self):
        return self.driver.find_element(By.XPATH, self.button_browseFile_xpath).text

    def isBrowseFileButtonEnabled(self):
        return self.driver.find_element(By.XPATH, self.button_browseFile_xpath).get_attribute("aria-disabled")

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

    # perform drag and drop operation to upload files from local machine
    def performdragAndDropFiles(self, file_path):
        # Perform the drag and drop action
        self.actions.click_and_hold().move_to_element(
            self.input_dragAndDrop_xpath).release().perform()

        # Simulate the file drop by executing JavaScript
        js_script = """
        var dropEvent = document.createEvent('CustomEvent');
        dropEvent.initCustomEvent('drop', true, true, null);
        dropEvent.dataTransfer = new DataTransfer();
        dropEvent.dataTransfer.files = [new File([''], '{}')];
        arguments[0].dispatchEvent(dropEvent);
        """.format(file_path)
        self.driver.execute_script(js_script)

    # wait for online source textbox to be available for enetering data
    # def waitForOnlineSourceTextbox(self):
    #     self.wait.until(EC.visibility_of_element_located(self.textbox_onlineSource_xpath))
    #     self.wait.until(EC.element_to_be_clickable(self.textbox_onlineSource_xpath))

    # enter all the details in the curate first draft gen page
    def enterCurateFirstDraftGenDetails(self, topic, tone, reading_level, online_sources=[], file_paths=[], drag_file_paths=[]):
        # enter topic 
        self.setTopic(topic)
        # click tone dropdown
        self.clickTone()
        # select tone
        self.selectTone(tone)
        # click reading level dropdown
        self.clickReadingLevel()
        # select reading level
        self.selectReadingLevel(reading_level)
        # add online sources
        if online_sources != []:
            # print("online_sources: ", online_sources)
            for source in online_sources:
                # wait for online sources text box to be available to enter
                # self.waitForOnlineSourceTextbox
                self.setOnlineSource(source)
                self.clickAddUrl()
                time.sleep(5)

        # add files using drag and drop
        if drag_file_paths != []:
            for file_path in drag_file_paths:
                self.input_dragAndDrop_xpath(file_path)

        # add files using browse file
        if file_paths != []:
            for file in file_paths:
                self.addBrowseFile(file)

    # wait for craft first draft page to load
    def waitForCraftFirstDraftGenPageToLoad(self):
        self.wait.until(EC.url_contains("constructYourOutline"))