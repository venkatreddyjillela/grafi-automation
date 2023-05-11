from selenium.webdriver.common.by import By

class HomePage:
    # Home Page
    button_first_draft_gen_xpath = '//h6[normalize-space()="First Draft Generator"]'
    button_rephraser_xpath = '//h6[normalize-space()="Rephraser"]'
    # link_first_draft_gen_xpath = '//a[normalize-space()="First Draft Generator"]'
    # link_rephraser_xpath = '//a[normalize-space()="Rephraser"]'
    # link_home_xpath = '//a[normalize-space()="Home"]'
    
    


    def __init__(self, driver):
        self.driver = driver

    def click_first_draft_gen(self):
        self.driver.find_element(By.XPATH, self.button_first_draft_gen_xpath).click()

    def click_rephraser(self):
        self.driver.find_element(By.XPATH, self.button_rephraser_xpath).click()

    # def get_first_draft_gen_link_text(self):
    #     return self.driver.find_element(By.XPATH, self.link_first_draft_gen_xpath).text
    
    # def get_rephraser_link_text(self):
    #     return self.driver.find_element(By.XPATH, self.link_rephraser_xpath).text
    
    # def get_home_link_text(self):
    #     return self.driver.find_element(By.XPATH, self.link_home_xpath).text
    

    
