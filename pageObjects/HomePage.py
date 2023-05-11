from selenium.webdriver.common.by import By

class HomePage:
    # Home Page
    # button_first_draft_gen_xpath = '//h6[normalize-space()="First Draft Generator"]'
    button_first_draft_gen_xpath = '//div[@class="MuiGrid-root MuiGrid-container MuiGrid-item MuiGrid-grid-xs-6 dashboardLeftContent css-sor6pw"]//div[1]//a[1]'

    # button_rephraser_xpath = '//h6[normalize-space()="Rephraser"]'
    button_rephraser_xpath = '//div[contains(@class,"MuiGrid-root MuiGrid-container MuiGrid-item MuiGrid-spacing-xs-4 css-h3jb2m")]//div[2]//a[1]'
    
    # link_first_draft_gen_xpath = '//a[normalize-space()="First Draft Generator"]'
    # link_rephraser_xpath = '//a[normalize-space()="Rephraser"]'
    # link_home_xpath = '//a[normalize-space()="Home"]'
    
    


    def __init__(self, driver):
        self.driver = driver

    def clickFirstDraftGen(self):
        self.driver.find_element(By.XPATH, self.button_first_draft_gen_xpath).click()

    def clickRephraser(self):
        self.driver.find_element(By.XPATH, self.button_rephraser_xpath).click()

    # def get_first_draft_gen_link_text(self):
    #     return self.driver.find_element(By.XPATH, self.link_first_draft_gen_xpath).text
    
    # def get_rephraser_link_text(self):
    #     return self.driver.find_element(By.XPATH, self.link_rephraser_xpath).text
    
    # def get_home_link_text(self):
    #     return self.driver.find_element(By.XPATH, self.link_home_xpath).text
    

    
