import pytest
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities.helperFunctions import HelperFunctions
from utilities import XLUtils
import time


class Test_002_DDT_Login():
    baseURL = ReadConfig.getApplicationURL()
    path = ".//TestData/LoginData.xlsx"
    logger = LogGen.loggen() 
    helper = HelperFunctions()

    @pytest.mark.regression
    def test_login_ddt(self, setup):
        self.driver = setup
        self.logger.info("******* Starting Test_002_DDT_Login Test **********")
        self.logger.info("******* Starting Login DDT Test **********")

        self.rows = XLUtils.getRowCount(self.path, 'Sheet1')
        self.logger.info('Number of rows = ' +  str(self.rows))
        self.logger.info('Number of credentials login is verfied : ' +  str(self.rows-1))
        lst_status = []

        for r in range(2, self.rows):
            self.email = XLUtils.readData(self.path, 'Sheet1', r, 1)
            self.password = XLUtils.readData(self.path, 'Sheet1', r, 2)
            self.exp = XLUtils.readData(self.path, 'Sheet1', r, 3)
            self.lp = self.helper.openLoginPage(setup)
            # wait for login page to load
            self.lp.waitForLoginPageToLoad()

            if self.email:
                self.lp.setEmail(self.email)
            if self.password:
                self.lp.setPassword(self.password)
            self.lp.clickLogin()
            try :
                # wait for home page to load
                self.lp.waitForHomePageToLoad()
            except:
                pass

            current_url = self.driver.current_url
            expected_url = self.baseURL+'home'

            error_message = 'Invalid username or password.'

            if current_url == expected_url:
                if self.exp == 'Pass':
                    self.logger.info("**** passed ****")
                    self.logger.info("**** Home Page is Opened ****")
                    lst_status.append("Pass")

                elif self.exp == 'Fail':
                    self.logger.error("**** failed ****")
                    lst_status.append("Fail")

                try :
                    if self.lp.getErrorMessage() == error_message:
                        self.logger.error("**** Error message is displayed for successful login ****")
                        assert False
                except :
                    self.logger.info("**** Error message is not displayed ****")
                    assert True

            elif current_url != expected_url:
                if self.exp == 'Pass':
                    self.logger.info("**** failed ****")
                    lst_status.append("Fail")
                elif self.exp == 'Fail':
                    self.logger.info("**** passed ****")
                    lst_status.append("Pass")

                if self.lp.getErrorMessage() == error_message:
                    self.logger.info("**** Error message is displayed ****")
                    assert True
                else :
                    self.logger.error("**** Error message is not displayed for login failure ****")
                    assert False

            self.logger.info(lst_status)

        if "Fail" not in lst_status:
            self.logger.info("******* DDT Login test passed **********")
            self.driver.close()
            assert True
        else:
            self.logger.error("******* DDT Login test failed **********")
            self.driver.close()
            assert False

        self.logger.info("******* End of Login DDT Test **********")
        self.logger.info(
            "**************** Completed  TC_LoginDDT_002 ************* ")
        
        self.logger.info("** Closing browser **")
        # close browser 
        self.driver.close()
