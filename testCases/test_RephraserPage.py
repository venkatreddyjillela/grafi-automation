import pytest
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from pageObjects.HomePage import HomePage
from pageObjects.CurateFirstDraftGenPage import CurateFirstDraftGen
import time
from TestData.testData import rephraserPageData
from utilities.helperFunctions import HelperFunctions


class Test_004_RephraserPage:
    baseURL = ReadConfig.getApplicationURL()
    email = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()
    helper = HelperFunctions()

    logger.info("**************** Test_004_RephraserPage *********************")

    @pytest.mark.regression
    def test_RephraserPage(self, setup):
        self.driver = setup
        self.rp = self.helper.openRephraserPage(setup)

        # check if logo is displayed
        logo = self.rp.isLogoDisplayed()
        if logo:
            self.logger.info("**** Logo is Displayed ****")
            assert True
        else:
            self.logger.error("**** Logo is not Displayed ****")
            self.driver.save_screenshot(
                ".\\Screenshots\\" + "test_logoInCuratePage.png")
            assert False

        # check home tab text
        home_tab_text = self.rp.getTextHomeTab()
        if home_tab_text == 'Home':
            self.logger.info("**** Home Tab Text is Displayed ****")
            assert True
        else:
            self.logger.error("**** Home Tab Text is not Displayed ****")
            self.driver.save_screenshot(
                ".\\Screenshots\\" + "test_HomeTabText.png")
            assert False

        # check if home tab is selected
        home_tab_selected = self.rp.isHomeTabSelected()
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
        first_draft_gen_tab_text = self.rp.getTextFirstDraftGenTab()
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
        first_draft_gen_tab_selected = self.rp.isFirstDraftGenTabSelected()
        if first_draft_gen_tab_selected == 'true':
            self.logger.error(
                "**** First Draft Generator Tab is Selected ****")
            self.driver.save_screenshot(
                ".\\Screenshots\\" + "test_FirstDraftGenTabSelected.png")
            assert False

        else:
            self.logger.info("**** First Draft Generator Tab is Selected ****")
            assert True

        #  check rephraser tab text
        rephraser_tab_text = self.rp.getTextRephraserTab()
        if rephraser_tab_text == 'Rephraser':
            self.logger.info("**** Rephraser Tab Text is Displayed ****")
            assert True
        else:
            self.logger.error("**** Rephraser Tab Text is not Displayed ****")
            self.driver.save_screenshot(
                ".\\Screenshots\\" + "test_RephraserTabText.png")
            assert False

        # check if rephraser tab is selected
        rephraser_tab_selected = self.rp.isRephraserTabSelected()
        if rephraser_tab_selected == 'true':
            self.logger.info("**** Rephraser Tab is Selected ****")
            assert True
        else:
            self.logger.error("**** Rephraser Tab is not Selected ****")
            self.driver.save_screenshot(
                ".\\Screenshots\\" + "test_RephraserTabSelected.png")
            assert False

        # check header text of the page
        header_text = self.rp.getHeaderText()
        if "Generate ideas and content" in header_text and "using personalised AI assistance" in header_text:
            self.logger.info("**** Header Text is Displayed ****")
            assert True
        else:
            self.logger.error("**** Header Text is not Displayed ****")
            self.logger.error(header_text)
            self.driver.save_screenshot(
                ".\\Screenshots\\" + "test_HeaderText.png")
            assert False

        # check upload url text
        url_text = self.rp.getUploadUrlText()
        if url_text == 'Upload a URL and Grafi will craft a reworded version of the content!':
            self.logger.info("**** URL Text is Displayed ****")
            assert True
        else:
            self.logger.error("**** URL Text is not Displayed ****")
            self.driver.save_screenshot(
                ".\\Screenshots\\" + "test_URLText.png")
            assert False

        # check upload url text box placeholder
        url_placeholder = self.rp.getUploadUrlTextBoxPlaceholder()
        if url_placeholder == 'https://www.teachervision.com/user/register?eachervisieachervisi//dns':
            self.logger.info(
                "**** URL Text Box Placeholder is Displayed ****")
            assert True
        else:
            self.logger.error(
                "**** URL Text Box Placeholder is not Displayed ****")
            self.driver.save_screenshot(
                ".\\Screenshots\\" + "test_URLPlaceholder.png")
            assert False

        # check tone text
        tone_text = self.rp.getTextTone()
        if tone_text == 'Tone Enter a custom tone or choose a preset tone':
            self.logger.info("**** Tone Text is Displayed ****")
            assert True
        else:
            self.logger.error("**** Tone Text is not Displayed ****")
            self.driver.save_screenshot(
                ".\\Screenshots\\" + "test_ToneText.png")
            assert False

        # check reading level text
        reading_level_text = self.rp.getTextReadingLevel()
        if reading_level_text == 'Reading Levels Please choose a preset Level':
            self.logger.info("**** Reading Level Text is Displayed ****")
            assert True
        else:
            self.logger.error("**** Reading Level Text is not Displayed ****")
            self.driver.save_screenshot(
                ".\\Screenshots\\" + "test_ReadingLevelText.png")
            assert False

        # Check Submit button text
        Submit_button_text = self.rp.getTextSubmitButton()
        if Submit_button_text == 'Submit':
            self.logger.info("**** Submit Button Text is Displayed ****")
            assert True
        else:
            self.logger.error("**** Submit Button Text is not Displayed ****")
            self.driver.save_screenshot(
                ".\\Screenshots\\" + "test_SubmitButtonText.png")
            assert False

        # Check Url Text Box is enabled or not
        URL_text_box_enabled = self.rp.isUploadUrlTextBoxEnabled()
        # By default URL Text Box is enabled
        if URL_text_box_enabled:
            self.logger.info("**** URL Text Box is Enabled ****")
            assert True
        else:
            self.logger.error("**** URL Text Box is not Enabled ****")
            self.driver.save_screenshot(
                ".\\Screenshots\\" + "test_URLTextBox.png")
            assert False

        # Check Tone Drop Down is enabled or not
        tone_drop_down_enabled = self.rp.isToneDropDownEnabled()
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
        reading_level_drop_down_enabled = self.rp.isReadingLevelDropDownEnabled()
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

        # Check Submit button is enabled or not
        Submit_button_enabled = self.rp.isSubmitButtonEnabled()
        # By default Submit button is disabled
        if not Submit_button_enabled:
            self.logger.info("**** Submit Button is Disabled ****")
            assert True
        else:
            self.logger.error("**** Submit Button is not Disabled ****")
            self.driver.save_screenshot(
                ".\\Screenshots\\" + "test_SubmitButton.png")
            assert False

    @pytest.mark.regression
    def test_RephraserPageElements(self, setup):
        self.logger.info("**** Test Rephraser Page Elements ****")
        self.driver = setup
        self.rp = self.helper.openRephraserPage(setup)

        # Tone dropdowm is only enabled when URL is entered
        self.rp.setUploadUrl(
            "https://www.mayoclinic.org/diseases-conditions/diabetes/symptoms-causes/syc-20371444")
        self.logger.info("**** Entered URL ****")
        # Check Tone Drop Down is enabled or not
        tone_drop_down_enabled = self.rp.isToneDropDownEnabled()
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
        self.rp.clickTone()
        self.logger.info("**** Clicked Tone Drop Down ****")
        # Get the options from the Tone Drop Down
        tone_options = self.rp.getToneOptions()
        tone_options = [value for value in tone_options if value != '']
        self.logger.info("**** Tone Drop Down Options are ****")
        self.logger.info(tone_options)
        expected_tone_options = ['friendly',
                                 'professional', 'conversational', 'neutral']
        if tone_options == expected_tone_options:
            self.logger.info("**** Tone Drop Down Options are correct ****")
            assert True

        # Reading Level dropdowm is only enabled when Topic entered and Tone is selected
        self.rp.selectTone("professional")
        self.logger.info("**** Selected Tone ****")
        # Check Reading Level Drop Down is enabled or not
        reading_level_drop_down_enabled = self.rp.isReadingLevelDropDownEnabled()
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
        self.rp.clickReadingLevel()
        self.logger.info("**** Clicked Reading Level Drop Down ****")
        # Get the options from the Reading Level Drop Down
        reading_level_options = self.rp.getReadingLevelOptions()
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
        self.rp.selectReadingLevel("postgraduate")

        # Check submit Button is enabled or not
        Submit_button_enabled = self.rp.isSubmitButtonEnabled()
        # Submit Button should be enabled when url entered and Tone is selected and Reading Level is selected
        if Submit_button_enabled:
            self.logger.info("**** Submit Button is Enabled ****")
            assert True
        else:
            self.logger.error("**** Submit Button is not Enabled ****")
            self.driver.save_screenshot(
                ".\\Screenshots\\" + "test_SubmitButton.png")
            assert False

    @pytest.mark.regression
    @pytest.mark.sanity
    def test_RephraserSubmitButton(self, setup):
        self.logger.info(
            "**** Started Test Submit Buttoni in Rephraser Page ****")
        self.driver = setup
        self.rp = self.helper.openRephraserPage(setup)

        # rephraserPageData

        UPLOAD_URL = rephraserPageData["upload_url"]
        TONE = rephraserPageData["tone"]
        READING_LEVEL = rephraserPageData['reading_level']

        # Enter All the details in the Rephraser Page and click on Submit Button
        self.rp.enterRephraserDetails(
            uploadUrl=UPLOAD_URL, tone=TONE, reading_level=READING_LEVEL)
        self.logger.info(
            "**** Entered All the details in the Rephraser Page and clicked on Submit Button ****")

        # Clicking on Submit Button after entering the Rephraser Details
        self.rp.clickSubmit()

        # wait for the rephraser result draft page to appear
        self.rp.waitForResultDraftRephraserPageToLoad()

        # Check if Result draft Page url is correct or not
        actual_url = self.driver.current_url
        expected_url = self.baseURL + "repurpose/Draft"
        if actual_url == expected_url:
            self.logger.info(
                "**** Rephraser Result draft Page url is correct and page loaded ****")
            assert True
        else:
            self.logger.error(
                "**** Rephraser Result draft Page url is incorrect ****")
            self.driver.save_screenshot(
                ".\\Screenshots\\" + "test_RephraserResultdraftPageUrl.png")
            assert False
