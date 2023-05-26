from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from pageObjects.HomePage import HomePage
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

    # Open Home Page
    def openHomePage(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        # login to the application
        self.lp.userLogin(self.email, self.password)
        self.logger.info(
            "**** Entered Email, Password and Clicked Login Button ****")
        self.hp = HomePage(self.driver)
        return self.hp
    
    # Open Curate first draft generator page
    def openCurateFirstDraftGenPage(self, setup):
        self.hp = self.openHomePage(setup)
        # click on the First Draft Gen button
        self.logger.info(
            "**** Clicked First Draft Gen Button In Home Page ****")
        self.hp.clickFirstDraftGen()
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

        return self.fd


    # Open Rephraser page
    def openRephraserPage(self, setup):
        self.hp = self.openHomePage(setup)
        # click on the Rephraser button
        self.logger.info("**** Clicked Rephraser Button In Home Page ****")
        self.hp.clickRephraser()
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
        # Result Draft Rephraser Page
        self.rdrp = ResultDraftRephraser(self.driver)
        return self.rdrp
    
    


