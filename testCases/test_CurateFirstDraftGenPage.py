import pytest
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from pageObjects.HomePage import HomePage
from pageObjects.CurateFirstDraftGenPage import FirstDraftGenCurate
import time
from TestData.testData import firstDraftGenPageData


class Test_003_FirstDraftGenCurate:
    baseURL = ReadConfig.getApplicationURL()
    email = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_FirstDraftGenCurateHeader(self, setup):
        self.logger.info(
            "*************** Test_003_FirstDraftGenCurate *****************")
        self.logger.info(
            "****Started First Draft Gen Curate Page header test ****")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.setEmail(self.email)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        time.sleep(5)
        self.hp = HomePage(self.driver)
        self.hp.clickFirstDraftGen()
        self.logger.info("****First Draft Gen button is Clicked****")
        self.fd = FirstDraftGenCurate(self.driver)
        header_text = self.fd.getHeader()
        if header_text == 'Tell Grafi AI What Healthcare Topic You Want To Write About':
            self.logger.info(
                "****First Draft Gen Curate Page header test passed ****")
            self.driver.close()
            assert True

        else:
            self.logger.error(
                "****First Draft Gen Curate Page header test failed****")
            self.driver.save_screenshot(
                ".\\Screenshots\\"+"test_FirstDraftGenCurateHeader.png")
            self.driver.close()
            assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_FirstDraftCurateNextClick(self, setup):
        self.logger.info(
            "*************** Test_003_FirstDraftGenCurate *****************")
        self.logger.info("****Started First Draft Curate Next Click Test****")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.setEmail(self.email)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        time.sleep(5)
        self.logger.info("****Home Page is Opended****")
        self.hp = HomePage(self.driver)
        self.logger.info("****Click first Draft Gen Button****")
        self.hp.clickFirstDraftGen()
        self.logger.info("****First Draft Gen Page is Opened****")
        self.fd = FirstDraftGenCurate(self.driver)
        self.fd.setTopic(firstDraftGenPageData['topic'])
        self.logger.info("****Topic Entered****")
        self.fd.clickTone()
        self.logger.info("****Tone dropdown Clicked****")
        # time.sleep(2)
        self.fd.selectTone(firstDraftGenPageData['tone'])
        self.logger.info("****Tone Selected****")
        self.fd.clickReadingLevel()
        self.logger.info("****Reading Level dropdown Clicked****")
        # time.sleep(2)

        self.fd.selectReadingLevel(firstDraftGenPageData['reading_level'])
        self.logger.info("****Reading Level Selected****")
        # time.sleep(2)
        self.fd.setOnlineSource(firstDraftGenPageData['online_source1'])
        # time.sleep(2)
        self.fd.clickAddUrl()
        time.sleep(2)
        self.logger.info("****First Online Source URL is added****")
        self.fd.setOnlineSource(firstDraftGenPageData['online_source2'])
        self.fd.clickAddUrl()
        time.sleep(2)
        self.logger.info("****Second Online Source URL is added****")
        time.sleep(2)
        self.fd.addBrowseFiles(firstDraftGenPageData['file_path1'])
        time.sleep(2)
        self.logger.info("****First File is added****")
        self.fd.addBrowseFiles(firstDraftGenPageData['file_path2'])
        time.sleep(2)
        self.logger.info("****Second File is added****")
        time.sleep(2)
        self.fd.clickNext()
        self.logger.info("****Next Button is Clicked****")
        self.logger.info(
            "**** Waiting for 30 Seconds after clicking Next button ****")

        time.sleep(60)

        current_url = self.driver.current_url

        if current_url == self.baseURL + 'inputContent/constructYourOutline':
            self.logger.info(
                "****First Draft Curate Next Click Test Passed****")
            self.logger.info("****First Draft Craft Page is Opened****")
            self.driver.close()
            assert True

        else:
            self.logger.error(
                "****First Draft Curate Next Click Test Failed****")
            self.driver.save_screenshot(
                ".\\Screenshots\\" + "test_FirstDraftCurateNextClick.png")
            self.driver.close()
            assert False
