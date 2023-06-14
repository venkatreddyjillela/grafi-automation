import pytest
from utilities.customLogger import LogGen
from utilities.helperFunctions import HelperFunctions
from utilities.readProperties import ReadConfig


class Test_MyAccountPage:
    baseURL = ReadConfig.getApplicationURL()
    logger = LogGen.loggen()
    helper = HelperFunctions()

    logger.info("*************** Test_MyAccountPage ***************")

    @pytest.mark.regression
    def test_MyAccountPageElements(self, setup):
        self.logger.info(
            "*************** Verifying My Account Page Elements ***************")
        self.driver = setup
        # open my account page
        self.ma = self.helper.openMyAccountPage(self.driver)
        self.logger.info("** checking logo **")
        # Check if logo is displayed
        assert self.ma.isLogoDisplayed() == True

        self.logger.info("** Checking Personal Info label **")
        assert self.ma.getPersonalDetailsText() == "My Personal Details"

        self.logger.info("** Checking User Name label **")
        assert self.ma.getUserNameText() == "User Name"

        self.logger.info("** Checking First Name label **")
        assert self.ma.getFirstNameText() == "First Name"

        self.logger.info("** Checking Last Name label **")
        assert self.ma.getLastNameText() == "Last Name"

        self.logger.info("** Checking Email Address label **")
        assert self.ma.getEmailAddressText() == "Email Address"

        self.logger.info("** Checking User Name textbox Value is displayed**")
        assert self.ma.getUserNameTextBoxValue() != ""

        self.logger.info("** Checking First Name textbox Value is displayed**")
        assert self.ma.getFirstNameTextBoxValue() != ""

        self.logger.info("** Checking Last Name textbox Value is displayed**")
        assert self.ma.getLastNameTextBoxValue() != ""

        self.logger.info(
            "** Checking Email Address textbox Value is displayed**")
        assert self.ma.getEmailAddressTextBoxValue() != ""

        self.logger.info("** Checking User Name textbox is disabled **")
        assert self.ma.isUserNameTextBoxEnabled() == False

        self.logger.info("** Checking First Name textBox is disabled **")
        assert self.ma.isFirstNameTextBoxEnabled() == False

        self.logger.info("** Checking Last Name textbox is disabled **")
        assert self.ma.isLastNameTextBoxEnabled() == False

        self.logger.info("** Checking Email Address textbox is disabled **")
        assert self.ma.isEmailTextBoxEnabled() == False

        self.logger.info("** Checking My Account button text **")
        assert self.ma.getMyAccountButtonText() == "My Account"

        self.logger.info("** Checking Subscription button text **")
        assert self.ma.getSubscriptionButtonText() == "Subscription"

        # By default Personal Details dropdown should be expanded
        self.logger.info(
            "** Checking Personal Details dropdown is expanded **")
        assert self.ma.isPersonalDetailsDropdownExpanded() == True

        # Click on Personal Details dropdown to collapse
        self.logger.info("** Clicking Personal Details dropdown **")
        self.ma.clickPersonalDetailsDropdown()

        self.logger.info(
            "** Checking Personal Details dropdown is collapsed **")
        assert self.ma.isPersonalDetailsDropdownExpanded() == False

    @pytest.mark.regression
    def test_AccountHomeTab(self, setup):
        self.logger.info(
            "*************** Verifying Account Home Tab ***************")
        self.driver = setup
        # open my account page
        self.ma = self.helper.openMyAccountPage(self.driver)
        # Click on Home Tab
        self.logger.info("** Clicking on Home Tab **")
        self.ma.clickHomeTab()
        # wait for home page to load
        self.ma.waitForHomePageToLoad()
        # Check if Home Tab is opened
        self.logger.info("** Checking if Home Tab is opened **")

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
    def test_AccountFirstDraftGenTab(self, setup):
        self.logger.info(
            "*************** Verifying Account First Draft Gen Tab ***************")
        self.driver = setup
        # open my account page
        self.ma = self.helper.openMyAccountPage(self.driver)
        # Click on First Draft Gen Tab
        self.logger.info("** Clicking on First Draft Gen Tab **")
        self.ma.clickFirstDraftGenTab()
        # wait for First Draft Gen page to load
        self.ma.waitForCuratePageToLoad()
        # Check if First Draft Gen Tab is opened
        self.logger.info("** Checking if First Draft Gen Tab is opened **")

        actual_url = self.driver.current_url
        expected_url = self.baseURL + "inputContent"
        if actual_url == expected_url:
            self.logger.info(
                "**** First Draft Gen Page url is correct and First Draft Gen page loaded ****")
            assert True
        else:
            self.logger.error(
                "**** First Draft Gen Page url is incorrect ****")
            self.driver.save_screenshot(
                ".\\Screenshots\\" + "test_FirstDraftGenPageUrl.png")
            assert False

    @pytest.mark.regression
    def test_AccountRephraserTab(self, setup):
        self.logger.info(
            "*************** Verifying Account Rephraser Tab ***************")
        self.driver = setup
        # open my account page
        self.ma = self.helper.openMyAccountPage(self.driver)
        # Click on Rephraser Tab
        self.logger.info("** Clicking on Rephraser Tab **")
        self.ma.clickRephraserTab()
        # wait for Rephraser page to load
        self.ma.waitForRephraserPageToLoad()
        # Check if Rephraser Tab is opened
        self.logger.info("** Checking if Rephraser Tab is opened **")

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
    def test_MyAccountButton(self, setup):
        self.logger.info(
            "*************** Verifying My Account Button ***************")
        self.driver = setup
        # open my account page
        self.ma = self.helper.openMyAccountPage(self.driver)
        # Click on My Account Button
        self.logger.info("** Clicking on My Account Button **")
        self.ma.clickMyAccountButton()
        # Check if My Account Button is opened
        self.logger.info("** Checking if My Account Page is opened **")

        actual_url = self.driver.current_url
        expected_url = self.baseURL + "myAccount"
        if actual_url == expected_url:
            self.logger.info(
                "**** My Account Page url is correct and My Account page loaded ****")
            assert True
        else:
            self.logger.error("**** My Account Page url is incorrect ****")
            self.driver.save_screenshot(
                ".\\Screenshots\\" + "test_MyAccountPageUrl.png")
            assert False

    @pytest.mark.regression
    def test_SubscriptionButton(self, setup):
        self.logger.info(
            "*************** Verifying Subscription Button ***************")
        self.driver = setup
        # open my account page
        self.ma = self.helper.openMyAccountPage(self.driver)
        # Click on Subscription Button
        self.logger.info("** Clicking on Subscription Button **")
        self.ma.clickSubscriptionButton()
        # wait for Subscription page to load
        self.ma.waitForSubscriptionPageToLoad()

        # Check if Subscription Button is opened
        self.logger.info("** Checking if Subscription Page is opened **")

        actual_url = self.driver.current_url
        expected_url = self.baseURL + "subscription"
        if actual_url == expected_url:
            self.logger.info(
                "**** Subscription Page url is correct and Subscription page loaded ****")
            assert True
        else:
            self.logger.error("**** Subscription Page url is incorrect ****")
            self.driver.save_screenshot(
                ".\\Screenshots\\" + "test_SubscriptionPageUrl.png")
            assert False
