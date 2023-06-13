from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from pageObjects.HomePage import HomePage
from pageObjects.ProfileTab import ProfileTab
from pageObjects.MyAccountPage import MyAccount
from pageObjects.CurateFirstDraftGenPage import CurateFirstDraftGen
from pageObjects.RephraserPage import Rephraser
from pageObjects.ResultDraftRephraserPage import ResultDraftRephraser

import time
from TestData.testData import firstDraftGenPageData

class HelperFunctions():
    baseURL = ReadConfig.getApplicationURL()
    email = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()

    topic = firstDraftGenPageData["topic"]
    tone = firstDraftGenPageData["tone"]
    reading_level = firstDraftGenPageData["reading_level"]
    online_source1 = firstDraftGenPageData["online_source1"]
    online_source2 = firstDraftGenPageData["online_source2"]
    file_path1 = firstDraftGenPageData["file_path1"]
    file_path2 = firstDraftGenPageData["file_path2"]

    logger = LogGen.loggen()

    # Open Login Page
    def openLoginPage(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.logger.info("**** Application URL is Opened ****")
        self.lp = LoginPage(self.driver)
        # wait for login page to load
        self.lp.waitForLoginPageToLoad()
        return self.lp

    # Open Home Page
    def openHomePage(self, setup):
        self.lp = self.openLoginPage(setup)
        # login to the application
        self.lp.userLogin(self.email, self.password)
        time.sleep(5)
        self.logger.info(
            "**** Entered Email, Password and Clicked Login Button ****")
        # wait for home page to load
        self.lp.waitForHomePageToLoad()
        self.hp = HomePage(self.driver)

        return self.hp
    
    # Open Curate first draft generator page
    def openCurateFirstDraftGenPage(self, setup):
        self.hp = self.openHomePage(setup)
        self.logger.info("**************** wait for 5 seconds ****************")
        # click on the First Draft Gen button
        self.logger.info(
            "**** Clicked First Draft Gen Button In Home Page ****")
        self.hp.clickFirstDraftGen()
        time.sleep(5)
        self.logger.info("**************** clicked first draft gen  ****************")
        # wait for curate first draft gen page to load
        self.hp.waitForCurateFirstDraftGenPageToLoad()
        self.logger.info("**** First Draft Gen Page is Opened ****")
        # CurateFirstDraftGen
        self.fd = CurateFirstDraftGen(self.driver)
        return self.fd
    
    # Open Craft first draft generator page
    def openCraftFirstDraftGenPage(self, setup):
        # Open Curate first draft generator page
        self.fd = self.openCurateFirstDraftGenPage(setup)
        # Enter all the details in the Curate first draft generator page and click next button
        self.fd.enterCurateFirstDraftGenDetails(self.topic, self.tone, self.reading_level, online_source=[self.online_source1,self.online_source2], file_path=[self.file_path1,self.file_path2])
        self.logger.info("**** Entered Topic, Tone, Reading Level, Online Source and File Path and Clicked Next Button ****")
        # wait for craft first draft gen page to load
        self.fd.waitForCraftFirstDraftGenPageToLoad()

        return self.fd


    # Open Rephraser page
    def openRephraserPage(self, setup):
        self.hp = self.openHomePage(setup)
        # click on the Rephraser button
        self.logger.info("**** Clicked Rephraser Button In Home Page ****")
        self.hp.clickRephraser()
        # wait for rephraser page to load
        self.hp.waitForRephraserPageToLoad()
        self.logger.info("**** Rephraser Page is Opened ****")
        # Rephraser
        self.rp = Rephraser(self.driver)
        return self.rp
    
    # Open Result Draft Rephraser Page
    def openResultDraftRephraserPage(self, setup):
        # Open Home Page
        self.rp = self.openRephraserPage(setup)
        # Enter all the details in the Rephraser page and click next button
        self.rp.enterRephraserDetails(self.online_source1, self.tone, self.reading_level)
        self.logger.info("**** Entered Online Source, Tone, Reading Level and Clicked Next Button ****")
        # wait for result draft rephraser page to load
        self.rp.waitForResultDraftRephraserPageToLoad()
        # Result Draft Rephraser Page
        self.rdrp = ResultDraftRephraser(self.driver)
        return self.rdrp
    
    # Open Profile Tab
    def openProfileTab(self, setup):
        self.hp = self.openHomePage(setup)
        # click Profile dropdown button 
        self.pt = self.ProfileTab(self.driver)
        self.pt.clickProfileDropdown()
        self.logger.info("**** Profile Tab is Opened ****")
        return self.pt
    
    # Open My Account Page
    def openMyAccountPage(self, setup):
        self.pt = self.openProfileTab(setup)
        # click My Account button
        self.pt.clickMyAccount()
        # wait for my account page to load
        self.pt.waitForMyAccountPageToLoad()
        self.logger.info("**** My Account Page is Opened ****")
        # My Account Page
        self.ma = MyAccount(self.driver)
        return self.ma
