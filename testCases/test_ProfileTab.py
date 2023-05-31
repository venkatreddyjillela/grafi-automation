import pytest
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities.helperFunctions import HelperFunctions

class Test_ProfileTab:
    baseURL = ReadConfig.getApplicationURL()
    logger = LogGen.loggen()
    helper = HelperFunctions()

    logger.info("*************** Test_ProfileTab ***************")

    @pytest.mark.regression
    def test_profileTabElements(self, setup):
        self.logger.info("*************** test_profileTabElements ***************")
        self.driver = setup
        # Open Home Page
        self.hp = self.helper.openHomePage(setup)
        # Click on Profile dropdown
        self.hp.clickProfileDropdown()
        self.logger.info("*************** Click Profile dropdown ***************")

        # Verify My Account link text
        self.logger.info("*************** Verify My Account link text ***************")
        assert self.hp.getMyAccountLinkText() == "My Account"
        self.logger.info("*************** My Account link text is correct ***************")

        # Verify Subscription link text
        self.logger.info("*************** Verify Subscription link text ***************")
        assert self.hp.getSubscriptionLinkText() == "Subscription"
        self.logger.info("*************** Subscription link text is correct ***************")

        # Verify Sign Out button text
        self.logger.info("*************** Verify Sign Out button text ***************")
        assert self.hp.getSignOutButtonText() == "Sign Out"
        self.logger.info("*************** Sign Out button text is correct ***************")

        # Verify Sign Out button is enabled
        self.logger.info("*************** Verify Sign Out button is enabled ***************")
        assert self.hp.isSignOutButtonEnabled() == True
        self.logger.info("*************** Sign Out button is enabled ***************")

        # Verify Sign Out button is displayed
        self.logger.info("*************** Verify Sign Out button is displayed ***************")
        assert self.hp.isSignOutButtonDisplayed() == True
        self.logger.info("*************** Sign Out button is displayed ***************")

        # Verify Profile title is displayed
        self.logger.info("*************** Verify Profile title is displayed ***************")
        assert self.hp.isProfileTitleDisplayed() == True
        self.logger.info("*************** Profile title is displayed ***************")

        # close browser
        self.driver.close()

    @pytest.mark.regression
    @pytest.mark.sanity
    def test_myAccountLink(self, setup):
        self.logger.info("*************** test_myAccountLink ***************")
        self.driver = setup
        # Open Home Page
        self.hp = self.helper.openHomePage(setup)
        # Click on Profile dropdown
        self.hp.clickProfileDropdown()
        self.logger.info("*************** Click Profile dropdown ***************")
        # Click on My Account
        self.hp.clickMyAccount()
        self.logger.info("*************** Click My Account ***************")
        # Wait for My Account page to load
        self.hp.waitForMyAccountPageToLoad()
        self.logger.info("*************** My Account page loaded ***************")
        # Verify My Account page URL
        self.logger.info("*************** Verify My Account page URL ***************")
        actual_url = self.driver.current_url
        expected_url = self.baseURL + "myAccount"
        if actual_url == expected_url:
            self.logger.info("**** myAccount Page url is correct and myAccount page loaded ****")
            assert True
        else:
            self.logger.error("**** myAccount Page url is incorrect ****")
            self.driver.save_screenshot(
                ".\\Screenshots\\" + "test_myAccountPageUrl.png")
            assert False

        # close browser
        self.driver.close()

    @pytest.mark.regression
    @pytest.mark.sanity
    def test_subscriptionLink(self, setup):
        self.logger.info("*************** test_subscriptionLink ***************")
        self.driver = setup
        # Open Home Page
        self.hp = self.helper.openHomePage(setup)
        # Click on Profile dropdown
        self.hp.clickProfileDropdown()
        self.logger.info("*************** Click Profile dropdown ***************")
        # Click on Subscription
        self.hp.clickSubscription()
        self.logger.info("*************** Click Subscription ***************")
        # Wait for Subscription page to load
        self.hp.waitForSubscriptionPageToLoad()
        self.logger.info("*************** Subscription page loaded ***************")
        # Verify Subscription page URL
        self.logger.info("*************** Verify Subscription page URL ***************")
        actual_url = self.driver.current_url
        expected_url = self.baseURL + "subscription"
        if actual_url == expected_url:
            self.logger.info("**** Subscription Page url is correct and Subscription page loaded ****")
            assert True
        else:
            self.logger.error("**** Subscription Page url is incorrect ****")
            self.driver.save_screenshot(
                ".\\Screenshots\\" + "test_subscriptionPageUrl.png")
            assert False

        # close browser
        self.driver.close()

    @pytest.mark.regression
    @pytest.mark.sanity
    def test_signOutButton(self, setup):
        self.logger.info("*************** test_signOutButton ***************")
        self.driver = setup
        # Open Home Page
        self.hp = self.helper.openHomePage(setup)
        # Click on Profile dropdown
        self.hp.clickProfileDropdown()
        self.logger.info("*************** Click Profile dropdown ***************")
        # Click on Sign Out button
        self.hp.clickSignOutButton()
        self.logger.info("*************** Click Sign Out button ***************")
        # Wait for Login In page to load
        self.hp.waitForLoginPageToLoad()
        self.logger.info("*************** Login In page loaded ***************")
        # Verify Login In page URL
        self.logger.info("*************** Verify Login In page URL ***************")
        actual_url = self.driver.current_url
        if "openid-connect" in actual_url:
            self.logger.info("**** Login In Page url is correct and Login In page loaded ****")
            assert True
        else:
            self.logger.error("**** Login In Page url is incorrect ****")
            self.driver.save_screenshot(
                ".\\Screenshots\\" + "test_LoginInPageUrl.png")
            assert False

        # close browser
        self.driver.close()



        