import pytest
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from pageObjects.HomePage import HomePage
from pageObjects.CurateFirstDraftGenPage import CurateFirstDraftGen
import time
from TestData.testData import firstDraftGenPageData
from helper_functions import HelperFunctions


class Test_003_CurateFirstDraftGenPage:
    baseURL = ReadConfig.getApplicationURL()
    email = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()
    helper = HelperFunctions()


    logger.info(
        "*************** Test_003_CurateFirstDraftGenPage ***************")
    
    # def openCurateFirstDraftGenPage(self, setup):
    #     self.driver = setup
    #     self.driver.get(self.baseURL)
    #     self.lp = LoginPage(self.driver)
    #     # login to the application
    #     self.lp.userLogin(self.email, self.password)
    #     self.logger.info(
    #         "**** Entered Email, Password and Clicked Login Button ****")
    #     self.hp = HomePage(self.driver)
    #     # click on the First Draft Gen button
    #     self.logger.info(
    #         "**** Clicked First Draft Gen Button In Home Page ****")
    #     self.hp.clickFirstDraftGen()
    #     self.logger.info("**** First Draft Gen Page is Opened ****")
    #     # CurateFirstDraftGen
    #     self.fd = CurateFirstDraftGen(self.driver)
    #     return self.fd



    @pytest.mark.regression
    def test_CurateFirstDraftGenPage(self, setup):
        # test all the elements on the Curate First Draft Gen Page
        # self.fd = self.openCurateFirstDraftGenPage(setup)
        self.fd = self.helper.openCurateFirstDraftGenPage(setup)

        # check if logo is displayed
        logo = self.fd.isLogoDisplayed()
        if logo:
            self.logger.info("**** Logo is Displayed ****")
            assert True
        else:
            self.logger.error("**** Logo is not Displayed ****")
            self.driver.save_screenshot(
                ".\\Screenshots\\" + "test_CurateFirstDraftGenPage.png")
            assert False

        # check home tab text
        home_tab_text = self.fd.getTextHomeTab()
        if home_tab_text == 'Home':
            self.logger.info("**** Home Tab Text is Displayed ****")
            assert True
        else:
            self.logger.error("**** Home Tab Text is not Displayed ****")
            self.driver.save_screenshot(
                ".\\Screenshots\\" + "test_CurateFirstDraftGenPage.png")
            assert False

        # check if home tab is selected
        home_tab_selected = self.fd.isHomeTabSelected()
        # home tab should not be selected it should select first draft gen tab
        if home_tab_selected:
            self.logger.error("**** Home Tab is Selected ****")
            self.driver.save_screenshot(
                ".\\Screenshots\\" + "test_CurateFirstDraftGenPage.png")
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
                ".\\Screenshots\\" + "test_CurateFirstDraftGenPage.png")
            assert False

        # check if first draft gen tab is selected
        first_draft_gen_tab_selected = self.fd.isFirstDraftGenTabSelected()
        if first_draft_gen_tab_selected:
            self.logger.info("**** First Draft Generator Tab is Selected ****")
            assert True
        else:
            self.logger.error(
                "**** First Draft Generator Tab is not Selected ****")
            self.driver.save_screenshot(
                ".\\Screenshots\\" + "test_CurateFirstDraftGenPage.png")
            assert False

        #  check rephraser tab text
        rephraser_tab_text = self.fd.getTextRephraserTab()
        if rephraser_tab_text == 'Rephraser':
            self.logger.info("**** Rephraser Tab Text is Displayed ****")
            assert True
        else:
            self.logger.error("**** Rephraser Tab Text is not Displayed ****")
            self.driver.save_screenshot(
                ".\\Screenshots\\" + "test_CurateFirstDraftGenPage.png")
            assert False

        # check if rephraser tab is selected
        rephraser_tab_selected = self.fd.isRephraserTabSelected()
        if rephraser_tab_selected:
            self.logger.error("**** Rephraser Tab is Selected ****")
            self.driver.save_screenshot(
                ".\\Screenshots\\" + "test_CurateFirstDraftGenPage.png")
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
                ".\\Screenshots\\" + "test_CurateFirstDraftGenPage.png")
            assert False

        # check topic text
        topic_text = self.fd.getTextTopic()
        if topic_text == 'What topic do you want to write about? For the best results, please include at least one medical keyword - diabetes, multiple sclerosis, etc.':
            self.logger.info("**** Topic Text is Displayed ****")
            assert True
        else:
            self.logger.error("**** Topic Text is not Displayed ****")
            self.driver.save_screenshot(
                ".\\Screenshots\\" + "test_CurateFirstDraftGenPage.png")
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
                ".\\Screenshots\\" + "test_CurateFirstDraftGenPage.png")
            assert False

        # check tone text
        tone_text = self.fd.getTextTone()
        if tone_text == 'Tone':
            self.logger.info("**** Tone Text is Displayed ****")
            assert True
        else:
            self.logger.error("**** Tone Text is not Displayed ****")
            self.driver.save_screenshot(
                ".\\Screenshots\\" + "test_CurateFirstDraftGenPage.png")
            assert False

        # check reading level text
        reading_level_text = self.fd.getTextReadingLevel()
        if reading_level_text == 'Reading Level':
            self.logger.info("**** Reading Level Text is Displayed ****")
            assert True
        else:
            self.logger.error("**** Reading Level Text is not Displayed ****")
            self.driver.save_screenshot(
                ".\\Screenshots\\" + "test_CurateFirstDraftGenPage.png")
            assert False

        # check online sources text
        online_sources_text = self.fd.getTextOnlineSources()
        if online_sources_text == 'Online Sources(Optional)':
            self.logger.info("**** Online Sources Text is Displayed ****")
            assert True
        else:
            self.logger.error("**** Online Sources Text is not Displayed ****")
            self.driver.save_screenshot(
                ".\\Screenshots\\" + "test_CurateFirstDraftGenPage.png")
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
                ".\\Screenshots\\" + "test_CurateFirstDraftGenPage.png")
            assert False

        # check add url button text
        add_url_button_text = self.fd.getTextAddUrl()
        if add_url_button_text == 'Add URL':
            self.logger.info("**** Add URL Button Text is Displayed ****")
            assert True
        else:
            self.logger.error("**** Add URL Button Text is not Displayed ****")
            self.driver.save_screenshot(
                ".\\Screenshots\\" + "test_CurateFirstDraftGenPage.png")
            assert False

        # check uploadable sources text
        uploadable_sources_text = self.fd.getTextUploadableSources()
        if uploadable_sources_text == 'Uploadable Sources(Optional)':
            self.logger.info("**** Uploadable Sources Text is Displayed ****")
            assert True
        else:
            self.logger.error(
                "**** Uploadable Sources Text is not Displayed ****")
            self.driver.save_screenshot(
                ".\\Screenshots\\" + "test_CurateFirstDraftGenPage.png")
            assert False

        # check drag and drop text
        drag_and_drop_text = self.fd.getTextDragAndDrop()
        if drag_and_drop_text == ' Drag & Drop files here':
            self.logger.info("**** Drag & Drop Text is Displayed ****")
            assert True
        else:
            self.logger.error("**** Drag & Drop Text is not Displayed ****")
            self.driver.save_screenshot(
                ".\\Screenshots\\" + "test_CurateFirstDraftGenPage.png")
            assert False

        # Check browse file button text
        browse_file_button_text = self.fd.getTextBrowseFile()
        if browse_file_button_text == 'Browse File':
            self.logger.info("**** Browse File Button Text is Displayed ****")
            assert True
        else:
            self.logger.error(
                "**** Browse File Button Text is not Displayed ****")
            self.driver.save_screenshot(
                ".\\Screenshots\\" + "test_CurateFirstDraftGenPage.png")
            assert False

        # Check Next button text
        next_button_text = self.fd.getTextNextButton()
        if next_button_text == 'Next':
            self.logger.info("**** Next Button Text is Displayed ****")
            assert True
        else:
            self.logger.error("**** Next Button Text is not Displayed ****")
            self.driver.save_screenshot(
                ".\\Screenshots\\" + "test_CurateFirstDraftGenPage.png")
            assert False

        # Check Next button is enabled or not
        next_button_enabled = self.fd.isNextButtonEnabled()
        # By default Next button is disabled
        if next_button_enabled == False:
            self.logger.info("**** Next Button is Disabled ****")
            assert True
        else:
            self.logger.error("**** Next Button is not Disabled ****")
            self.driver.save_screenshot(
                ".\\Screenshots\\" + "test_CurateFirstDraftGenPage.png")
            assert False

        # Check Topic Text Box is enabled or not
        topic_text_box_enabled = self.fd.isTopicTextBoxEnabled()
        # By default Topic Text Box is enabled
        if topic_text_box_enabled == True:
            self.logger.info("**** Topic Text Box is Enabled ****")
            assert True
        else:
            self.logger.error("**** Topic Text Box is not Enabled ****")
            self.driver.save_screenshot(
                ".\\Screenshots\\" + "test_CurateFirstDraftGenPage.png")
            assert False

        # Check Tone Drop Down is enabled or not
        tone_drop_down_enabled = self.fd.isToneDropDownEnabled()
        # By default Tone Drop Down is disabled
        if tone_drop_down_enabled == False:
            self.logger.info("**** Tone Drop Down is Disabled ****")
            assert True
        else:
            self.logger.error("**** Tone Drop Down is not Disabled ****")
            self.driver.save_screenshot(
                ".\\Screenshots\\" + "test_CurateFirstDraftGenPage.png")
            assert False

        # Check Reading Level Drop Down is enabled or not
        reading_level_drop_down_enabled = self.fd.isReadingLevelDropDownEnabled()
        # By default Reading Level Drop Down is disabled
        if reading_level_drop_down_enabled == False:
            self.logger.info("**** Reading Level Drop Down is Disabled ****")
            assert True
        else:
            self.logger.error(
                "**** Reading Level Drop Down is not Disabled ****")
            self.driver.save_screenshot(
                ".\\Screenshots\\" + "test_CurateFirstDraftGenPage.png")
            assert False

        # Check Online Sources Text Box is enabled or not
        online_sources_text_box_enabled = self.fd.isOnlineSourcesTextBoxEnabled()
        # By default Online Sources Text Box is disabled
        if online_sources_text_box_enabled == False:
            self.logger.info("**** Online Sources Text Box is Disabled ****")
            assert True
        else:
            self.logger.error(
                "**** Online Sources Text Box is not Disabled ****")
            self.driver.save_screenshot(
                ".\\Screenshots\\" + "test_CurateFirstDraftGenPage.png")
            assert False

        # Check Add URL Button is enabled or not
        add_url_button_enabled = self.fd.isAddUrlButtonEnabled()
        # By default Add URL Button is disabled
        if add_url_button_enabled == False:
            self.logger.info("**** Add URL Button is Disabled ****")
            assert True
        else:
            self.logger.error("**** Add URL Button is not Disabled ****")
            self.driver.save_screenshot(
                ".\\Screenshots\\" + "test_CurateFirstDraftGenPage.png")
            assert False

        # Check Drag and Drop is enabled or not
        drag_and_drop_text_enabled = self.fd.isDragAndDropEnabled()
        # By default Drag and Drop is disabled
        if drag_and_drop_text_enabled == False:
            self.logger.info("**** Drag and Drop is Disabled ****")
            assert True
        else:
            self.logger.error("**** Drag and Drop is not Disabled ****")
            self.driver.save_screenshot(
                ".\\Screenshots\\" + "test_CurateFirstDraftGenPage.png")
            assert False

        # Check Browse File Button is enabled or not
        browse_file_button_enabled = self.fd.isBrowseFileButtonEnabled()
        # By default Browse File Button is disabled
        if browse_file_button_enabled == False:
            self.logger.info("**** Browse File Button is Disabled ****")
            assert True
        else:
            self.logger.error("**** Browse File Button is not Disabled ****")
            self.driver.save_screenshot(
                ".\\Screenshots\\" + "test_CurateFirstDraftGenPage.png")
            assert False

    def test_CuratePageElements(self, setup):
        self.logger.info("**** Started Test_CuratePageElements Functionality ****")

        self.fd = self.helper.openCurateFirstDraftGenPage(setup)

        # Tone dropdowm is only enabled when Topic is entered
        self.fd.setTopic("Test")
        self.logger.info("**** Entered Topic ****")
        # Check Tone Drop Down is enabled or not
        tone_drop_down_enabled = self.fd.isToneDropDownEnabled()
        # Tone Drop Down should be enabled
        if tone_drop_down_enabled == True:
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
        self.logger.info("**** Tone Drop Down Options are ****")
        self.logger.info(tone_options)
        expected_tone_options = ['friendly',
                                 'professional', 'conversational', 'neutral']
        if tone_options == expected_tone_options:
            self.logger.info("**** Tone Drop Down Options are correct ****")
            assert True

        # Reading Level dropdowm is only enabled when Topic entered and Tone is selected
        self.fd.selectTone("professional")
        self.logger.info("**** Selected Tone ****")
        # Check Reading Level Drop Down is enabled or not
        reading_level_drop_down_enabled = self.fd.isReadingLevelDropDownEnabled()
        # Reading Level Drop Down should be enabled
        if reading_level_drop_down_enabled == True:
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
        self.logger.info("**** Reading Level Drop Down Options are ****")
        self.logger.info(reading_level_options)
        expected_reading_level_options = ['middleschool',
                                            'highschool', 'postgraduate']
        
        if reading_level_options == expected_reading_level_options:
            self.logger.info("**** Reading Level Drop Down Options are correct ****")
            assert True
        else:
            self.logger.error("**** Reading Level Drop Down Options are not correct ****")
            self.driver.save_screenshot(
                ".\\Screenshots\\" + "test_ReadingLevelDropDownOptions.png")
            assert False

        # Select Reading Level 
        self.fd.selectReadingLevel("postgraduate")

        # Check Online Sources Text Box is enabled or not
        online_sources_text_box_enabled = self.fd.isOnlineSourcesTextBoxEnabled()
        # Online Sources Text Box should be enabled when Topic entered and Tone is selected and Reading Level is selected
        if online_sources_text_box_enabled == True:
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
        # Add URL Button should be enabled when Topic entered and Tone is selected and Reading Level is selected
        if add_url_button_enabled == True:
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
        if drag_and_drop_text_enabled == True:
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
        if browse_file_button_enabled == True:
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
        if next_button_enabled == True:
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
        self.logger.info("**** Started Test_CuratePageNextButton Functionality ****")

        self.fd = self.helper.openCurateFirstDraftGenPage(setup)

        TOPIC = firstDraftGenPageData['topic']
        TONE = firstDraftGenPageData['tone']
        READING_LEVEL = firstDraftGenPageData['reading_level']
        ONLINE_SOURCES = firstDraftGenPageData['online_sources1']
        FILE_PATHS = firstDraftGenPageData['file_path1']

        # Enter All the details in the Curate Page and click on Next Button
        self.fd.enterCurateFirstDraftGenDetails(topic= TOPIC,tone = TONE, reading_level = READING_LEVEL, online_sources = ONLINE_SOURCES, file_paths = FILE_PATHS)
        self.logger.info("**** Entered All the details in the Curate Page and clicked on Next Button ****")