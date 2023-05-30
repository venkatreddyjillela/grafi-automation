from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class HomePage:
    # Home Page
    
    # button_firstdraftGen_xpath = '//h6[normalize-space()="First Draft Generator"]'
    button_firstdraftGen_xpath = '//div/a[@href="/inputContent"]'
    # button_firstdraftGen_xpath = '//div[@class="MuiGrid-root MuiGrid-container MuiGrid-item MuiGrid-grid-xs-6 dashboardLeftContent css-sor6pw"]//div[1]//a[1]'

    button_rephraser_xpath = '//h6[normalize-space()="Rephraser"]'
    # button_rephraser_xpath = '//div[contains(@class,"MuiGrid-root MuiGrid-container MuiGrid-item MuiGrid-spacing-xs-4 css-h3jb2m")]//div[2]//a[1]'

    # link_first_draft_gen_xpath = '//a[normalize-space()="First Draft Generator"]'
    # link_rephraser_xpath = '//a[normalize-space()="Rephraser"]'
    # link_home_xpath = '//a[normalize-space()="Home"]'

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def clickFirstDraftGen(self):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, self.button_firstdraftGen_xpath))).click()

    def clickRephraser(self):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, self.button_rephraser_xpath))).click()

    # wait for curate first draft gen page to load
    def waitForCurateFirstDraftGenPageToLoad(self):
        self.wait.until(EC.url_contains("inputContent"))

    # wait for rephraser page to load
    def waitForRephraserPageToLoad(self):
        self.wait.until(EC.url_contains("repurpose"))


    # def get_first_draft_gen_link_text(self):
    #     return self.driver.find_element(By.XPATH, self.link_first_draft_gen_xpath).text

    # def get_rephraser_link_text(self):
    #     return self.driver.find_element(By.XPATH, self.link_rephraser_xpath).text

    # def get_home_link_text(self):
    #     return self.driver.find_element(By.XPATH, self.link_home_xpath).text
