import pytest
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from pageObjects.HomePage import HomePage
from pageObjects.FirstDraftGenCuratePage import FirstDraftGenCuratePage

class Test_002_FirstDraftGenCurate:
    baseURL = ReadConfig.getApplicationURL()
    email = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger=LogGen.loggen()

    @pytest.mark.regression
    def test_FirstDraftGenCurateHeader(self,setup):
        self.logger.info("*************** Test_002_FirstDraftGenCurate *****************")
        self.logger.info("****Started First Draft Gen Curate Page header test ****")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp=LoginPage(self.driver)
        self.lp.setEmail(self.email)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.hp=HomePage(self.driver)
        self.hp.click_first_draft_gen()
        self.fd=FirstDraftGenCuratePage(self.driver)
        header_text=self.fd.get_header()
        if header_text == 'Tell Grafi AI What Healthcare Topic You Want To Write About':
            self.logger.info("****First Draft Gen Curate Page header test passed ****")
            self.driver.close()
            assert True

        else:
            self.logger.error("****First Draft Gen Curate Page header test failed****")
            self.driver.save_screenshot(".\\Screenshots\\"+"test_FirstDraftGenCurateHeader.png")
            self.driver.close()
            assert False



        
        

        




        

