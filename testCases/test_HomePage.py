import pytest
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from pageObjects.HomePage import HomePage
from utilities.helperFunctions import HelperFunctions
import time


class Test_002_HomePage:
    baseURL = ReadConfig.getApplicationURL()
    email = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()
    helper = HelperFunctions()

    @pytest.mark.regression
    @pytest.mark.sanity
    def test_homePage(self, setup):
        self.logger.info(
            "*************** Started Testing Home Page ***********")
        # openHomePage
        self.hp = self.helper.openHomePage(setup)
        self.driver = setup
        current_url = self.driver.current_url
        if current_url == self.baseURL + 'home':
            self.logger.info("****Home Page test passed ****")
            self.logger.info("****Home Page Open ****")
            assert True
        else:
            self.logger.error("****Home page is not open & test failed****")
            self.driver.save_screenshot(".\\Screenshots\\"+"test_homePage.png")
            assert False
        # close browser
        self.driver.close()

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_clickFirstDraftGen(self, setup):
        self.logger.info("****Started Click First Draft Gen Test****")
        # openHomePage
        self.hp = self.helper.openHomePage(setup)
        self.driver = setup
        # click on the First Draft Gen button
        self.logger.info(
            "**** Clicked First Draft Gen Button In Home Page ****")
        self.hp.clickFirstDraftGen()
        # wait for curate page to load
        self.hp.waitForCurateFirstDraftGenPageToLoad()
        current_url = self.driver.current_url
        if current_url == self.baseURL + 'inputContent':
            self.logger.info("****Click First Draft Gen test passed ****")
            self.logger.info("**** First Draft Gen Page Open ****")
            assert True
        else:
            self.logger.error("****Click First Draft Gen test failed ****")
            self.driver.save_screenshot(
                ".\\Screenshots\\" + "test_clickFirstDraftGen.png")
            assert False

        # close browser
        self.driver.close()

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_clickRephraser(self, setup):
        self.logger.info("****Started Click Rephraser Test****")
        # openHomePage
        self.hp = self.helper.openHomePage(setup)
        self.driver = setup
        # click on the Rephraser button
        self.logger.info("**** Clicked Rephraser Button In Home Page ****")

        self.hp.clickRephraser()
        # wait for rephraser page to load
        self.hp.waitForRephraserPageToLoad()

        current_url = self.driver.current_url
        if current_url == self.baseURL + 'repurpose':
            self.logger.info("****Click Rephraser test passed ****")
            self.logger.info("**** Rephraser Page Open ****")
            assert True
        else:
            self.logger.error("****Click Rephraser test failed ****")
            self.driver.save_screenshot(
                ".\\Screenshots\\" + "test_clickRephraser.png")
            assert False

        # close browser
        self.driver.close()
