from selenium.webdriver.common.by import By
class FirstDraftGenCurate:
    
    # First Draft Curate Page
    txt_header_xpath = '//span[@class="fontWeight-700"]'
    textbox_topic_xpath = '(//input[@id="textBoxMedium"])[1]'

    drp_tone_xpath = '//div[@id="mui-component-select-tone"]'
    select_tone_xpath = '//ul[@role="listbox"]/li'
    
    drp_reading_level_xpath = '//div[@id="mui-component-select-readinglevel"]'
    select_reading_level_xpath = '//ul[@role="listbox"]/li'

    textbox_online_source_xpath = '(//input[@id="textBoxMedium"])[2]'
    button_add_url_xpath = '//button[normalize-space()="Add URL"]'
    button_browse_file_xpath = '//input[@accept=".pdf"]'
    
    button_next_xpath = '//button[normalize-space()="Next"]'
    # link_url_xpath = '(//p[@class="MuiTypography-root MuiTypography-body1 urlDataText FirstDraftGenerator-urlLink css-9l3uo3"])[2]'
    


    def __init__(self, driver):
        self.driver = driver

    def getHeader(self):
        return self.driver.find_element(By.XPATH, self.txt_header_xpath).text

    def setTopic(self, topic):
        topic_element = self.driver.find_element(By.XPATH, self.textbox_topic_xpath)
        topic_element.clear()
        topic_element.send_keys(topic)

    def clickTone(self):
        self.driver.find_element(By.XPATH, self.drp_tone_xpath).click()

    def selectTone(self, tone):
        tone_elements = self.driver.find_elements(By.XPATH, self.select_tone_xpath)
        for tone_element in tone_elements:
            if tone_element.get_attribute("data-value") == tone:
                tone_element.click()
                break

    def clickReadingLevel(self):
        self.driver.find_element(By.XPATH, self.drp_reading_level_xpath).click()

    def selectReadingLevel(self, reading_level):
        reading_level_elements = self.driver.find_elements(By.XPATH, self.select_reading_level_xpath)
        for reading_level_element in reading_level_elements:
            if reading_level_element.get_attribute("data-value") == reading_level:
                reading_level_element.click()
                break

    def setOnlineSource(self, online_source):
        online_source_element = self.driver.find_element(By.XPATH, self.textbox_online_source_xpath)
        online_source_element.clear()
        online_source_element.send_keys(online_source)

    def clickAddUrl(self):
        self.driver.find_element(By.XPATH, self.button_add_url_xpath).click()

    def addBrowseFiles(self, file_path):
        self.driver.find_element(By.XPATH, self.button_browse_file_xpath).send_keys(file_path)

    def clickNext(self):
        self.driver.find_element(By.XPATH, self.button_next_xpath).click()



