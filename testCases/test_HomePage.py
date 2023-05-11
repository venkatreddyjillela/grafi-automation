import pytest
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from pageObjects.HomePage import HomePage
import time

class Test_002_HomePage:
    baseURL = ReadConfig.getApplicationURL()
    email = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger=LogGen.loggen()

    @pytest.mark.regression
    def test_homePage(self,setup):
        self.logger.info("*************** Test_002_HomePage *****************")
        self.logger.info("****Started Home Page Title test ****")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp=LoginPage(self.driver)
        self.lp.setEmail(self.email)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        time.sleep(5)
        current_url=self.driver.current_url
        if current_url == self.baseURL + 'home':
            self.logger.info("****Home Page test passed ****")
            self.driver.close()
            assert True
        else:
            self.logger.error("****Home page test failed****")
            self.driver.save_screenshot(".\\Screenshots\\"+"test_homePage.png")
            self.driver.close()
            assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_clickFirstDraftGen(self,setup):
        self.logger.info("****Started Click First Draft Gen Test****")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp=LoginPage(self.driver)
        self.lp.setEmail(self.email)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.hp=HomePage(self.driver)
        self.hp.clickFirstDraftGen()
        current_url=self.driver.current_url
        if current_url == self.baseURL + 'inputContent':
            self.logger.info("****Click First Draft Gen test passed ****")
            self.driver.close()
            assert True
        else:
            self.logger.error("****Click First Draft Gen test failed ****")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_clickFirstDraftGen.png")
            self.driver.close()
            assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_clickRephraser(self, setup):
        self.logger.info("****Started Click Rephraser Test****")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.setEmail(self.email)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.hp = HomePage(self.driver)
        self.hp.clickRephraser()
        current_url = self.driver.current_url
        if current_url == self.baseURL + 'repurpose':
            self.logger.info("****Click Rephraser test passed ****")
            self.driver.close()
            assert True
        else:
            self.logger.error("****Click Rephraser test failed ****")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_clickRephraser.png")
            self.driver.close()
            assert False
        
