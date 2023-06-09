import pytest
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from TestData.testData import firstDraftGenPageData
from utilities.helperFunctions import HelperFunctions


class Test_CurateFirstDraftGenPage:
    baseURL = ReadConfig.getApplicationURL()
    logger = LogGen.loggen()
    helper = HelperFunctions()
    topic = firstDraftGenPageData['topic']
    tone = firstDraftGenPageData['tone']
    reading_level = firstDraftGenPageData['reading_level']
    online_source1 = firstDraftGenPageData['online_source1']
    online_source2 = firstDraftGenPageData['online_source2']
    file_path1 = firstDraftGenPageData['file_path1']
    file_path2 = firstDraftGenPageData['file_path2']

    logger.info(
        "*************** Test_CurateFirstDraftGenPage ***************")

    @pytest.mark.regression
    def test_CurateFirstDraftGenPage(self, setup):
        # test all the elements on the Curate First Draft Gen Page
        # self.fd = self.openCurateFirstDraftGenPage(setup)
        self.driver = setup
        self.fd = self.helper.openCurateFirstDraftGenPage(setup)
        # check if logo is displayed
        logo = self.fd.isLogoDisplayed()
        if logo:
            self.logger.info("**** Logo is Displayed ****")
            assert True
        else:
            self.logger.error("**** Logo is not Displayed ****")
            self.driver.save_screenshot(
                ".\\Screenshots\\" + "test_logoInCuratePage.png")
            assert False

        # check home tab text
        home_tab_text = self.fd.getTextHomeTab()
        if home_tab_text == 'Home':
            self.logger.info("**** Home Tab Text is Displayed ****")
            assert True
        else:
            self.logger.error("**** Home Tab Text is not Displayed ****")
            self.driver.save_screenshot(
                ".\\Screenshots\\" + "test_HomeTabText.png")
            assert False

        # check if home tab is selected
        home_tab_selected = self.fd.isHomeTabSelected()
        # home tab should not be selected it should select first draft gen tab
        if home_tab_selected == 'true':
            self.logger.error("**** Home Tab is Selected ****")
            self.driver.save_screenshot(
                ".\\Screenshots\\" + "test_homeTabSelected.png")
            assert False
        else:
            self.logger.info("**** Home Tab is not Selected ****")
            assert True

        # check first draft gen tab text
        first_draft_gen_tab_text = self.fd.getTextFirstDraftGenTab()
        if first_draft_gen_tab_text == 'First Draft Generator':
            self.logger.info(
                "**** First Draft Generator Tab Text is Displayed ****")
            assert True
        else:
            self.logger.error(
                "**** First Draft Generator Tab Text is not Displayed ****")
            self.driver.save_screenshot(
                ".\\Screenshots\\" + "test_FirstDraftGenTabText.png")
            assert False

        # check if first draft gen tab is selected
        first_draft_gen_tab_selected = self.fd.isFirstDraftGenTabSelected()
        if first_draft_gen_tab_selected == 'true':
            self.logger.info("**** First Draft Generator Tab is Selected ****")
            assert True
        else:
            self.logger.error(
                "**** First Draft Generator Tab is not Selected ****")
            self.driver.save_screenshot(
                ".\\Screenshots\\" + "test_FirstDraftGenTabSelected.png")
            assert False

        #  check rephraser tab text
        rephraser_tab_text = self.fd.getTextRephraserTab()
        if rephraser_tab_text == 'Rephraser':
            self.logger.info("**** Rephraser Tab Text is Displayed ****")
            assert True
        else:
            self.logger.error("**** Rephraser Tab Text is not Displayed ****")
            self.driver.save_screenshot(
                ".\\Screenshots\\" + "test_RephraserTabText.png")
            assert False

        # check if rephraser tab is selected
        rephraser_tab_selected = self.fd.isRephraserTabSelected()
        if rephraser_tab_selected == 'true':
            self.logger.error("**** Rephraser Tab is Selected ****")
            self.driver.save_screenshot(
                ".\\Screenshots\\" + "test_RephraserTabSelected.png")
            assert False
        else:
            self.logger.info("**** Rephraser Tab is not Selected ****")
            assert True

        # check header text of the page
        header_text = self.fd.getHeaderText()
        if header_text == 'Tell Grafi AI What Healthcare Topic You Want To Write About':
            self.logger.info("**** Header Text is Displayed ****")
            assert True
        else:
            self.logger.error("**** Header Text is not Displayed ****")
            self.driver.save_screenshot(
                ".\\Screenshots\\" + "test_HeaderText.png")
            assert False

        # check topic text
        topic_text = self.fd.getTextTopic()
        if topic_text == 'What topic do you want to write about? For the best results, please include at least one medical keyword - diabetes, multiple sclerosis, etc.':
            self.logger.info("**** Topic Text is Displayed ****")
            assert True
        else:
            self.logger.error("**** Topic Text is not Displayed ****")
            self.driver.save_screenshot(
                ".\\Screenshots\\" + "test_TopicText.png")
            assert False

        # check topic text box placeholder
        topic_placeholder = self.fd.getTopicPlaceholder()
        if topic_placeholder == 'How to treat an acute spinal cord injury with steroids':
            self.logger.info(
                "**** Topic Text Box Placeholder is Displayed ****")
            assert True
        else:
            self.logger.error(
                "**** Topic Text Box Placeholder is not Displayed ****")
            self.driver.save_screenshot(
                ".\\Screenshots\\" + "test_TopicPlaceholder.png")
            assert False

        # check tone text
        tone_text = self.fd.getTextTone()
        if tone_text == 'Tone':
            self.logger.info("**** Tone Text is Displayed ****")
            assert True
        else:
            self.logger.error("**** Tone Text is not Displayed ****")
            self.driver.save_screenshot(
                ".\\Screenshots\\" + "test_ToneText.png")
            assert False

        # check reading level text
        reading_level_text = self.fd.getTextReadingLevel()
        if reading_level_text == 'Reading Level':
            self.logger.info("**** Reading Level Text is Displayed ****")
            assert True
        else:
            self.logger.error("**** Reading Level Text is not Displayed ****")
            self.driver.save_screenshot(
                ".\\Screenshots\\" + "test_ReadingLevelText.png")
            assert False

        # check online sources text
        online_sources_text = self.fd.getTextOnlineSources()
        if "Online Sources" in online_sources_text:
            self.logger.info("**** Online Sources Text is Displayed ****")
            assert True
        else:
            self.logger.error("**** Online Sources Text is not Displayed ****")
            self.logger.info(online_sources_text)
            self.logger.info("""Online Sources 
            (Optional)""")
            self.driver.save_screenshot(
                ".\\Screenshots\\" + "test_OnlineSourcesText.png")
            assert False

        # check online sources text box placeholder
        online_sources_placeholder = self.fd.getOnlineSourcesPlaceholder()
        if online_sources_placeholder == 'storyset.com':
            self.logger.info(
                "**** Online Sources Text Box Placeholder is Displayed ****")
            assert True
        else:
            self.logger.error(
                "**** Online Sources Text Box Placeholder is not Displayed ****")
            self.driver.save_screenshot(
                ".\\Screenshots\\" + "test_onlineSourcesPlaceholder.png")
            assert False

        # check add url button text
        add_url_button_text = self.fd.getTextAddUrl()
        if add_url_button_text == 'Add URL':
            self.logger.info("**** Add URL Button Text is Displayed ****")
            assert True
        else:
            self.logger.error("**** Add URL Button Text is not Displayed ****")
            self.driver.save_screenshot(
                ".\\Screenshots\\" + "test_AddUrlButtonText.png")
            assert False

        # check uploadable sources text
        uploadable_sources_text = self.fd.getTextUploadableSources()
        if 'Uploadable Sources' in uploadable_sources_text:
            self.logger.info("**** Uploadable Sources Text is Displayed ****")
            assert True
        else:
            self.logger.error(
                "**** Uploadable Sources Text is not Displayed ****")
            self.driver.save_screenshot(
                ".\\Screenshots\\" + "test_UploadableSourcesText.png")
            assert False

        # check drag and drop text
        drag_and_drop_text = self.fd.getTextDragAndDrop()
        if drag_and_drop_text == 'Drag & Drop files here':
            self.logger.info("**** Drag & Drop Text is Displayed ****")
            assert True
        else:
            self.logger.error("**** Drag & Drop Text is not Displayed ****")
            self.logger.error(drag_and_drop_text)
            self.driver.save_screenshot(
                ".\\Screenshots\\" + "test_DragAndDropText.png")
            assert False

        # Check browse file button text
        browse_file_button_text = self.fd.getTextBrowseFile()
        if browse_file_button_text == 'Browse File':
            self.logger.info("**** Browse File Button Text is Displayed ****")
            assert True
        else:
            self.logger.error(
                "**** Browse File Button Text is not Displayed ****")
            self.logger.error(browse_file_button_text)
            self.driver.save_screenshot(
                ".\\Screenshots\\" + "test_BrowseFileButtonText.png")
            assert False

        # Check Next button text
        next_button_text = self.fd.getTextNextButton()
        if next_button_text == 'Next':
            self.logger.info("**** Next Button Text is Displayed ****")
            assert True
        else:
            self.logger.error("**** Next Button Text is not Displayed ****")
            self.driver.save_screenshot(
                ".\\Screenshots\\" + "test_NextButtonText.png")
            assert False

        # Check Topic Text Box is enabled or not
        topic_text_box_enabled = self.fd.isTopicTextBoxEnabled()
        # By default Topic Text Box is enabled
        if topic_text_box_enabled:
            self.logger.info("**** Topic Text Box is Enabled ****")
            assert True
        else:
            self.logger.error("**** Topic Text Box is not Enabled ****")
            self.driver.save_screenshot(
                ".\\Screenshots\\" + "test_TopicTextBox.png")
            assert False

        # Check Tone Drop Down is enabled or not
        tone_drop_down_enabled = self.fd.isToneDropDownEnabled()
        # By default Tone Drop Down is disabled
        if tone_drop_down_enabled == 'true':
            self.logger.info("**** Tone Drop Down is Disabled ****")
            assert True
        else:
            self.logger.error("**** Tone Drop Down is not Disabled ****")
            self.logger.error(tone_drop_down_enabled)
            self.driver.save_screenshot(
                ".\\Screenshots\\" + "test_ToneDropDown.png")
            assert False

        # Check Reading Level Drop Down is enabled or not
        reading_level_drop_down_enabled = self.fd.isReadingLevelDropDownEnabled()
        # By default Reading Level Drop Down is disabled
        if reading_level_drop_down_enabled == 'true':
            self.logger.info("**** Reading Level Drop Down is Disabled ****")
            assert True
        else:
            self.logger.error(
                "**** Reading Level Drop Down is not Disabled ****")
            self.driver.save_screenshot(
                ".\\Screenshots\\" + "test_ReadingLevelDropDown.png")
            assert False

        # Check Online Sources Text Box is enabled or not
        online_sources_text_box_enabled = self.fd.isOnlineSourcesTextBoxEnabled()
        # By default Online Sources Text Box is disabled
        if not online_sources_text_box_enabled:
            self.logger.info("**** Online Sources Text Box is Disabled ****")
            assert True
        else:
            self.logger.error(
                "**** Online Sources Text Box is not Disabled ****")
            self.driver.save_screenshot(
                ".\\Screenshots\\" + "test_OnlineSourcesTextBox.png")
            assert False

        # Check Add URL Button is enabled or not
        add_url_button_enabled = self.fd.isAddUrlButtonEnabled()
        # By default Add URL Button is disabled
        if not add_url_button_enabled:
            self.logger.info("**** Add URL Button is Disabled ****")
            assert True
        else:
            self.logger.error("**** Add URL Button is not Disabled ****")
            self.driver.save_screenshot(
                ".\\Screenshots\\" + "test_AddUrlButton.png")
            assert False

        # Check Browse File Button is enabled or not
        browse_file_button_enabled = self.fd.isBrowseFileButtonEnabled()
        # By default Browse File Button is disabled
        if browse_file_button_enabled == 'true':
            self.logger.info("**** Browse File Button is Disabled ****")
            assert True
        else:
            self.logger.error("**** Browse File Button is not Disabled ****")
            self.driver.save_screenshot(
                ".\\Screenshots\\" + "test_BrowseFileButtonEnabled.png")
            assert False

        # check drag and drop is enabled or not
        try:
            self.fd.performdragAndDropFiles(
                firstDraftGenPageData['drag_file_path'])
            self.logger.error("**** Drag and Drop is enabled ****")
            self.driver.save_screenshot(
                ".\\Screenshots\\" + "test_DragAndDropEnabled.png")
            assert False
        except Exception as e:
            self.logger.info("**** Drag and Drop is not enabled ****")
            assert True

        # Check Next Button is enabled or not
        next_button_enabled = self.fd.isNextButtonEnabled()
        # Next Button should be enabled when Topic entered and Tone is selected and Reading Level is selected
        if not next_button_enabled:
            self.logger.info("**** Next Button is not Enabled ****")
            assert True
        else:
            self.logger.error("**** Next Button is Enabled ****")
            self.driver.save_screenshot(
                ".\\Screenshots\\" + "test_NextButton.png")
            assert False

    @pytest.mark.regression
    def test_CuratePageElements(self, setup):
        self.logger.info(
            "**** Started Test_CuratePageElements Functionality ****")
        self.driver = setup
        self.fd = self.helper.openCurateFirstDraftGenPage(setup)

        # Tone dropdowm is only enabled when Topic is entered
        self.fd.setTopic(self.topic)
        self.logger.info("**** Entered Topic ****")
        # Check Tone Drop Down is enabled or not
        tone_drop_down_enabled = self.fd.isToneDropDownEnabled()
        # Tone Drop Down should be enabled
        if tone_drop_down_enabled != 'true':
            self.logger.info("**** Tone Drop Down is Enabled ****")
            assert True
        else:
            self.logger.error("**** Tone Drop Down is not Enabled ****")
            self.driver.save_screenshot(
                ".\\Screenshots\\" + "test_ToneDropDownOptions.png")
            assert False

        # click on the Tone Drop Down
        self.fd.clickTone()
        self.logger.info("**** Clicked Tone Drop Down ****")
        # Get the options from the Tone Drop Down
        tone_options = self.fd.getToneOptions()
        tone_options = [value for value in tone_options if value != '']
        self.logger.info("**** Tone Drop Down Options are ****")
        self.logger.info(tone_options)
        expected_tone_options = ['friendly',
                                 'professional', 'conversational', 'neutral']
        if tone_options == expected_tone_options:
            self.logger.info("**** Tone Drop Down Options are correct ****")
            assert True

        # Reading Level dropdowm is only enabled when Topic entered and Tone is selected
        self.fd.selectTone(self.tone)
        self.logger.info("**** Selected Tone ****")
        # Check Reading Level Drop Down is enabled or not
        reading_level_drop_down_enabled = self.fd.isReadingLevelDropDownEnabled()
        # Reading Level Drop Down should be enabled
        if reading_level_drop_down_enabled != 'true':
            self.logger.info("**** Reading Level Drop Down is Enabled ****")
            assert True
        else:
            self.logger.error(
                "**** Reading Level Drop Down is not Enabled ****")
            self.driver.save_screenshot(
                ".\\Screenshots\\" + "test_ReadingLevelDropDownOptions.png")
            assert False

        # click on the Reading Level Drop Down
        self.fd.clickReadingLevel()
        self.logger.info("**** Clicked Reading Level Drop Down ****")
        # Get the options from the Reading Level Drop Down
        reading_level_options = self.fd.getReadingLevelOptions()
        reading_level_options = [
            value for value in reading_level_options if value != '']
        self.logger.info("**** Reading Level Drop Down Options are ****")
        self.logger.info(reading_level_options)
        expected_reading_level_options = ['middleschool',
                                          'highschool', 'postgraduate']

        if reading_level_options == expected_reading_level_options:
            self.logger.info(
                "**** Reading Level Drop Down Options are correct ****")
            assert True
        else:
            self.logger.error(
                "**** Reading Level Drop Down Options are not correct ****")
            self.driver.save_screenshot(
                ".\\Screenshots\\" + "test_ReadingLevelDropDownOptions.png")
            assert False

        # Select Reading Level
        self.fd.selectReadingLevel(self.reading_level)

        # Check Online Sources Text Box is enabled or not
        online_sources_text_box_enabled = self.fd.isOnlineSourcesTextBoxEnabled()
        # Online Sources Text Box should be enabled when Topic entered and Tone is selected and Reading Level is selected
        if online_sources_text_box_enabled != 'true':
            self.logger.info("**** Online Sources Text Box is Enabled ****")
            assert True
        else:
            self.logger.error(
                "**** Online Sources Text Box is not Enabled ****")
            self.driver.save_screenshot(
                ".\\Screenshots\\" + "test_OnlineSourcesTextBox.png")
            assert False

        # Check Add URL Button is enabled or not
        add_url_button_enabled = self.fd.isAddUrlButtonEnabled()
        # Add URL Button should be disabled by default
        if add_url_button_enabled != 'true':
            self.logger.info("**** Add URL Button is Disabled ****")
            assert True
        else:
            self.logger.error("**** Add URL Button is not Disabled ****")
            self.driver.save_screenshot(
                ".\\Screenshots\\" + "test_AddUrlButton.png")
            assert False

        # Check Add URL Button is enabled or not after entering URL
        self.fd.setOnlineSource(self.online_source1)
        self.logger.info("**** Entered URL ****")
        # Add URL Button should be enabled when URL is entered
        add_url_button_enabled = self.fd.isAddUrlButtonEnabled()
        if add_url_button_enabled != 'true':
            self.logger.info("**** Add URL Button is Enabled ****")
            assert True
        else:
            self.logger.error("**** Add URL Button is not Enabled ****")
            self.driver.save_screenshot(
                ".\\Screenshots\\" + "test_AddUrlButton.png")
            assert False

        # Check Drag and Drop is enabled or not
        drag_and_drop_text_enabled = self.fd.isDragAndDropEnabled()
        # Drag and Drop should be enabled when Topic entered and Tone is selected and Reading Level is selected
        if drag_and_drop_text_enabled != 'true':
            self.logger.info("**** Drag and Drop is Enabled ****")
            assert True
        else:
            self.logger.error("**** Drag and Drop is not Enabled ****")
            self.driver.save_screenshot(
                ".\\Screenshots\\" + "test_DragAndDrop.png")
            assert False

        # Check Browse File Button is enabled or not
        browse_file_button_enabled = self.fd.isBrowseFileButtonEnabled()
        # Browse File Button should be enabled when Topic entered and Tone is selected and Reading Level is selected
        if browse_file_button_enabled != 'true':
            self.logger.info("**** Browse File Button is Enabled ****")
            assert True
        else:
            self.logger.error("**** Browse File Button is not Enabled ****")
            self.driver.save_screenshot(
                ".\\Screenshots\\" + "test_BrowseFileButton.png")
            assert False

        # Check Next Button is enabled or not
        next_button_enabled = self.fd.isNextButtonEnabled()
        # Next Button should be enabled when Topic entered and Tone is selected and Reading Level is selected
        if next_button_enabled:
            self.logger.info("**** Next Button is Enabled ****")
            assert True
        else:
            self.logger.error("**** Next Button is not Enabled ****")
            self.driver.save_screenshot(
                ".\\Screenshots\\" + "test_NextButton.png")
            assert False

    @pytest.mark.regression
    @pytest.mark.sanity
    def test_CuratePageNextButton(self, setup):
        self.logger.info(
            "**** Started Test_CuratePageNextButton Functionality ****")
        self.driver = setup
        self.fd = self.helper.openCurateFirstDraftGenPage(setup)

        TOPIC = self.topic
        TONE = self.tone
        READING_LEVEL = self.reading_level
        ONLINE_SOURCES = [self.online_source1, self.online_source2]
        FILE_PATHS = [self.file_path1, self.file_path2]

        # Enter All the details in the Curate Page and click on Next Button
        self.fd.enterCurateFirstDraftGenDetails(
            topic=TOPIC, tone=TONE, reading_level=READING_LEVEL, online_sources=ONLINE_SOURCES, file_paths=FILE_PATHS)
        self.logger.info(
            "**** Entered All the details in the Curate Page and clicked on Next Button ****")

        # Check if added sources and given online sources are same or different in count
        if ONLINE_SOURCES == []:
            self.logger.info("**** No urls are added in online sources ****")
        elif len(ONLINE_SOURCES) == len(self.fd.getOnlineSourceAddedUrl()):
            self.logger.info(" **** Urls added and given urls are same ****")
            self.logger.info(len(self.fd.getOnlineSourceAddedUrl()))
            assert True
        else:
            self.logger.error(
                "*** added urls are different in number of online sources given ****")
            self.logger.error(len(self.fd.getOnlineSourceAddedUrl()))
            assert False

        # # wait for craft page to load
        # self.fd.waitForCraftPageToLoad()
        # self.logger.info("**** Craft Page Loaded ****")
        # click next button
        self.fd.clickNext()
        # wait for craft page to load
        self.fd.waitForCraftFirstDraftGenPageToLoad()

        # Check if Craft Page url is correct or not
        actual_url = self.driver.current_url
        expected_url = self.baseURL + "inputContent/constructYourOutline"
        if actual_url == expected_url:
            self.logger.info(
                "**** Craft Page url is correct and craft page loaded ****")
            assert True
        else:
            self.logger.error("**** Craft Page url is incorrect ****")
            self.driver.save_screenshot(
                ".\\Screenshots\\" + "test_CraftPageUrl.png")
            assert False

    @pytest.mark.regression
    def test_CurateHomeTab(self, setup):
        self.logger.info("**** Started Test_CurateHomeTab Functionality ****")
        self.driver = setup
        self.fd = self.helper.openCurateFirstDraftGenPage(setup)
        # click on Home Tab in Curate Page
        self.fd.clickHomeTab()
        # wait for home page to load
        self.fd.waitForHomePageToLoad()
        # Check if Home Page url is correct or not
        actual_url = self.driver.current_url
        expected_url = self.baseURL + "home"
        if actual_url == expected_url:
            self.logger.info(
                "**** Home Page url is correct and home page loaded ****")
            assert True
        else:
            self.logger.error("**** Home Page url is incorrect ****")
            self.driver.save_screenshot(
                ".\\Screenshots\\" + "test_HomePageUrl.png")
            assert False

    @pytest.mark.regression
    def test_CurateRephraserTab(self, setup):
        self.logger.info("**** Started CurateRephraserTab Testing ****")
        self.driver = setup
        self.fd = self.helper.openCurateFirstDraftGenPage(setup)
        # click on Rephraser tab
        self.fd.clickRephraserTab()
        # wait for Rephraser page to load
        self.fd.waitForRephraserPageToLoad()
        # Check if Rephraser Page url is correct or not
        actual_url = self.driver.current_url
        expected_url = self.baseURL + "repurpose"
        if actual_url == expected_url:
            self.logger.info(
                "**** Rephraser Page url is correct and Rephraser page loaded ****")
            assert True
        else:
            self.logger.error("**** Rephraser Page url is incorrect ****")
            self.driver.save_screenshot(
                ".\\Screenshots\\" + "test_RephraserPageUrl.png")
            assert False

    @pytest.mark.regression
    def test_CurateFirstDraftGenPage(self, setup):
        self.logger.info(
            "**** Started test_CurateFirstDraftGenPage Testing ****")
        self.driver = setup
        self.fd = self.helper.openCurateFirstDraftGenPage(setup)
        # click on Curate tab
        self.fd.clickFirstDraftGenTab()
        # wait for Curate page to load
        self.fd.waitForCuratePageToLoad()
        # Check if Curate Page url is correct or not
        actual_url = self.driver.current_url
        expected_url = self.baseURL + "inputContent"
        if actual_url == expected_url:
            self.logger.info(
                "**** Curate Page url is correct and Curate page loaded ****")
            assert True
        else:
            self.logger.error("**** Curate Page url is incorrect ****")
            self.driver.save_screenshot(
                ".\\Screenshots\\" + "test_CuratePageUrl.png")
            assert False
