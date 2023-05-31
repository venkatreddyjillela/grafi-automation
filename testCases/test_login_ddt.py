import pytest
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities import XLUtils
import time


class Test_002_DDT_Login():
    baseURL = ReadConfig.getApplicationURL()
    path = ".//TestData/LoginData.xlsx"
    logger = LogGen.loggen()  # Logger

    @pytest.mark.regression
    def test_login_ddt(self, setup):
        self.logger.info("******* Starting Test_002_DDT_Login Test **********")
        self.logger.info("******* Starting Login DDT Test **********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.lp = LoginPage(self.driver)

        self.rows = XLUtils.getRowCount(self.path, 'Sheet1')
        self.logger.info('Number of rows...', self.rows)
        lst_status = []

        for r in range(2, self.rows+1):
            self.email = XLUtils.readData(self.path, 'Sheet1', r, 1)
            self.password = XLUtils.readData(self.path, 'Sheet1', r, 2)
            self.exp = XLUtils.readData(self.path, 'Sheet1', r, 3)

            self.lp.setEmail(self.email)
            self.lp.setPassword(self.password)
            self.lp.clickLogin()
            time.sleep(5)

            current_url = self.driver.current_url
            expected_url = self.baseURL+'home'

            if current_url == expected_url:
                if self.exp == 'Pass':
                    self.logger.info("**** passed ****")
                    self.logger.info("**** Home Page is Opened ****")
                    self.lp.clickSignoutDropdown()
                    self.logger.info("**** Drop down is clicked ****")
                    self.lp.clickSignout()
                    self.logger.info("**** Click signout ****")
                    lst_status.append("Pass")
                elif self.exp == 'Fail':
                    self.logger.info("**** failed ****")
                    lst_status.append("Fail")

            elif current_url != expected_url:
                if self.exp == 'Pass':
                    self.logger.info("**** failed ****")
                    lst_status.append("Fail")
                elif self.exp == 'Fail':
                    self.logger.info("**** passed ****")
                    lst_status.append("Pass")
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
