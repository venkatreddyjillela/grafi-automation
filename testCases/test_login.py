import pytest
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

class Test_001_Login:
    baseURL = ReadConfig.getApplicationURL()
    email = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger=LogGen.loggen()

    @pytest.mark.regression
    def test_LoginPageTitle(self,setup):
        self.logger.info("*************** Test_001_Login *****************")
        self.logger.info("****Started Login Page Title test ****")
        self.driver = setup
        self.logger.info("****Opening URL****")
        self.driver.get(self.baseURL)
        act_title=self.driver.title

        if act_title=="Grafi - Where AI Meets Writing":
            self.logger.info("**** Login Page Title test passed ****")
            self.driver.close()
            assert True
        else:
            self.logger.error("**** Login page title test failed****")
            self.driver.save_screenshot(".\\Screenshots\\"+"test_LoginPageTitle.png")
            self.driver.close()
            assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_login(self,setup):
        self.logger.info("****Started Login Test****")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp=LoginPage(self.driver)
        self.lp.setEmail(self.email)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        act_title=self.driver.title
        if act_title == "Grafi":
            self.logger.info("****Login test passed ****")
            self.driver.close()
            assert True
        else:
            self.logger.error("****Login test failed ****")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_homePageTitle.png")
            self.driver.close()
            assert False





