import pytest
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
import time


class Test_001_Login:
    baseURL = ReadConfig.getApplicationURL()
    email = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()
    logger.info("*************** Test_001_Login *****************")

    @pytest.mark.regression
    def test_LoginPage(self, setup):\
        # test login page all elements are present or not and display correct text or not 
        self.driver = setup
        self.driver.get(self.baseURL)
        time.sleep(2)
        act_title = self.driver.title

        # test login page title
        self.logger.info("****Started Login Page Title test ****")
        if act_title == "Grafi - Where AI Meets Writing":
            self.logger.info("**** Login Page Title test passed ****")
            assert True
        else:
            self.logger.error("**** Login page title test failed****")
            self.driver.save_screenshot(
                ".\\Screenshots\\"+"test_LoginPageTitle.png")
            assert False

        self.logger.info("****Login Header Test ****")
        self.lp = LoginPage(self.driver)

        # test login Header 
        login_label = self.lp.getLoginHeader()
        if login_label == "Login":
            self.logger.info("****Login Header Test Passed ****")
            assert True
        else:
            self.logger.error("****Login Header Test Failed ****")
            self.driver.save_screenshot(
                ".\\Screenshots\\"+"test_LoginHeader.png")
            assert False

        # test email label
        self.logger.info("****Email Label Test ****")
        email_label = self.lp.getEmailLabel()
        if email_label == "Email":
            self.logger.info("****Email Label Test Passed ****")
            assert True
        else:
            self.logger.error("****Email Label Test Failed ****")
            self.driver.save_screenshot(
                ".\\Screenshots\\"+"test_EmailLabel.png")
            assert False

        # test password label
        self.logger.info("****Password Label Test ****")
        password_label = self.lp.getPasswordLabel()
        if password_label == "Password":
            self.logger.info("****Password Label Test Passed ****")
            assert True
        else:
            self.logger.error("****Password Label Test Failed ****")
            self.driver.save_screenshot(
                ".\\Screenshots\\"+"test_PasswordLabel.png")
            assert False

        # test forgot password link text
        self.logger.info("****Forgot Password Link Text Test ****")
        forgot_password_text = self.lp.getForgotPasswordText()
        if forgot_password_text == "Forgot Password?":
            self.logger.info("****Forgot Password Link Text Test Passed ****")
            assert True
        else:
            self.logger.error("****Forgot Password Link Text Test Failed ****")
            self.driver.save_screenshot(
                ".\\Screenshots\\"+"test_ForgotPasswordText.png")
            assert False

        # test login button text
        self.logger.info("****Login Button Text Test ****")
        login_button_text = self.lp.getLoginButtonText()
        if login_button_text == "Login":
            self.logger.info("****Login Button Text Test Passed ****")
            assert True
        else:
            self.logger.error("****Login Button Text Test Failed ****")
            self.driver.save_screenshot(
                ".\\Screenshots\\"+"test_LoginButtonText.png")
            assert False

        # test new user text
        self.logger.info("****New User Text Test ****")
        new_user_text = self.lp.getNewUserText()
        if "New user?" in new_user_text:
            self.logger.info("****New User Text Test Passed ****")
            assert True
        else:
            self.logger.error("****New User Text Test Failed ****")
            self.driver.save_screenshot(
                ".\\Screenshots\\"+"test_NewUserText.png")
            assert False

        # test Register link text
        self.logger.info("****Register Link Text Test ****")
        register_link_text = self.lp.getRegisterLinkText()
        if register_link_text == "Register":
            self.logger.info("****Register Link Text Test Passed ****")
            assert True
        else:
            self.logger.error("****Register Link Text Test Failed ****")
            self.driver.save_screenshot(
                ".\\Screenshots\\"+"test_RegisterLinkText.png")
            assert False

        # test grafi logo is displayed or not
        self.logger.info("****Grafi Logo Display Test ****")
        isLogoDisplayed = self.lp.isLogoDisplayed()
        if isLogoDisplayed:
            self.logger.info("****Grafi Logo Display Test Passed ****")
            assert True
        else:
            self.logger.error("****Grafi Logo Display Test Failed ****")
            self.driver.save_screenshot(
                ".\\Screenshots\\"+"test_GrafiLogo.png")
            assert False

        # test logo text 
        self.logger.info("****Grafi Logo Text Test ****")
        logo_text = self.lp.getLogoText()
        if 'Convert your thoughts into words with AI' in logo_text and 'Generate high-quality content at a breathtaking pace' in logo_text:
            self.logger.info("****Grafi Logo Text Test Passed ****")
            assert True
        else:
            self.logger.error("****Grafi Logo Text Test Failed ****")
            self.driver.save_screenshot(
                ".\\Screenshots\\"+"test_GrafiLogoText.png")
            assert False

        # test email text box placeholder
        self.logger.info("****Email Text Box Placeholder Test ****")
        email_placeholder = self.lp.getEmailPlaceholder()
        if email_placeholder == "Email":
            self.logger.info("****Email Text Box Placeholder Test Passed ****")
            assert True
        else:
            self.logger.error("****Email Text Box Placeholder Test Failed ****")
            self.driver.save_screenshot(
                ".\\Screenshots\\"+"test_EmailPlaceholder.png")
            assert False

        # test password text box placeholder
        self.logger.info("****Password Text Box Placeholder Test ****")
        password_placeholder = self.lp.getPasswordPlaceholder()
        if password_placeholder == "Password":
            self.logger.info("****Password Text Box Placeholder Test Passed ****")
            assert True
        else:
            self.logger.error("****Password Text Box Placeholder Test Failed ****")
            self.driver.save_screenshot(
                ".\\Screenshots\\"+"test_PasswordPlaceholder.png")
            assert False

        # test login button is enabled or not
        self.logger.info("****Login Button Enabled Test ****")
        isLoginButtonEnabled = self.lp.isLoginButtonEnabled()
        if isLoginButtonEnabled:
            self.logger.info("****Login Button Enabled Test Passed ****")
            assert True
        else:
            self.logger.error("****Login Button Enabled Test Failed ****")
            self.driver.save_screenshot(
                ".\\Screenshots\\"+"test_LoginButtonEnabled.png")
            assert False

        # test login button is displayed or not
        self.logger.info("****Login Button Displayed Test ****")
        isLoginButtonDisplayed = self.lp.isLoginButtonDisplayed()
        if isLoginButtonDisplayed:
            self.logger.info("****Login Button Displayed Test Passed ****")
            assert True
        else:
            self.logger.error("****Login Button Displayed Test Failed ****")
            self.driver.save_screenshot(
                ".\\Screenshots\\"+"test_LoginButtonDisplayed.png")
            assert False

        # close browser
        self.driver.close()

    @pytest.mark.regression
    @pytest.mark.sanity
    def test_forgetPasswordLink(self, setup):
        ## test forgot password Link functionality
        self.logger.info("****Test Forgot Password Link Functionality ****")
        self.driver = setup
        self.driver.get(self.baseURL)

        self.lp = LoginPage(self.driver)

        # click forgot password link
        self.lp.clickForgotPassword()

        # check forgot password page is opened or not
        current_url = self.driver.current_url
        if 'reset-credentials' in current_url:
            self.logger.info("****Forgot Password Page is opened****")
            self.logger.info("****Forgot Password Link Functionality Passed ****")
            assert True
        else:
            self.logger.error("****Forgot Password Page is not opened****")
            self.driver.save_screenshot(
                ".\\Screenshots\\" + "test_ForgotPasswordPage.png")
            self.logger.info("****Forgot Password Link Functionality Failed and Screenshot Saved ****")
            assert False
        
        # close browser
        self.driver.close()


    @pytest.mark.regression
    @pytest.mark.sanity
    def test_registrationLink(self, setup):
        ## test registration Link functionality
        self.logger.info("****Test Registration Link Functionality ****")
        self.driver = setup
        self.driver.get(self.baseURL)
        
        self.lp = LoginPage(self.driver)

        # click registration link
        self.lp.clickRegister()

        # check registration page is opened or not
        current_url = self.driver.current_url
        if 'registration' in current_url:
            self.logger.info("****Registration Page is opened****")
            self.logger.info("****Registration Link Functionality Passed ****")
            assert True
        else:
            self.logger.error("****Registration Page is not opened****")
            self.driver.save_screenshot(
                ".\\Screenshots\\" + "test_RegistrationPage.png")
            self.logger.info("****Registration Link Functionality Failed and Screenshot Saved ****")
            assert False

        # close browser
        self.driver.close()

    @pytest.mark.regression
    @pytest.mark.sanity
    def test_login(self, setup):
        ## test login functionality
        self.logger.info("****Test Login Functionality ****")
        self.driver = setup
        self.driver.get(self.baseURL)

        self.lp = LoginPage(self.driver)

        # enter email and password
        self.lp.setEmail(self.email)
        self.lp.setPassword(self.password)

        # click login button
        self.lp.clickLogin()
        time.sleep(5) # wait for 5 seconds to load home page after login
        current_url = self.driver.current_url
        if current_url == self.baseURL + 'home':
            self.logger.info("****Home Page is opened****")
            self.logger.info("****Login test passed ****")
            assert True
        else:
            self.logger.error("**** Home Page is not opened ****")
            self.driver.save_screenshot(
                ".\\Screenshots\\" + "test_Login.png")
            self.logger.info("****Login test failed and Screenshot Saved ****")
            assert False