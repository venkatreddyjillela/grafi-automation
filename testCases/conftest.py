import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.options import Options
import os

location = os.getcwd() + "\\Downloads"

@pytest.fixture()
def setup(browser):
    if browser=='firefox':
        firefox_options = webdriver.FirefoxOptions()
        firefox_options.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/msword")  # MIME type of the file you want to download (ms word is used here)
        firefox_options.set_preference("browser.download.manager.showWhenStarting", False)
        firefox_options.set_preference("browser.download.folderList", 2)
        firefox_options.set_preference("browser.download.dir", location)
        # set up the Firefox WebDriver using the driver manager
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install(), options=firefox_options)
        print("Launching firefox browser.........")

    elif browser=='Edge':
        preferences = {"download.default_directory": location}
        edge_options = webdriver.EdgeOptions()
        edge_options.add_experimental_option("prefs", preferences)
        # set up the Edge WebDriver using the driver manager
        driver = webdriver.Edge(EdgeChromiumDriverManager().install(), options=edge_options)
        print("Launching Edge browser.........")

    else:
        preferences = {"download.default_directory": location, "plugins.always_open_pdf_externally": True}
        # Create Chrome options object
        chrome_options = Options()
        chrome_options.add_experimental_option("prefs", preferences)
        # chrome_options.add_argument('--headless')

        # Create driver object with the ChromeDriverManager and the options object
        driver = webdriver.Chrome(
            ChromeDriverManager().install(), options=chrome_options)
        print("Launching default chrome browser.........")

    # implicit wait
    driver.implicitly_wait(10)
    # maximize window
    driver.maximize_window()
    print("Maximizing window.............")

    return driver

def pytest_addoption(parser):    # This will get the value from CLI /hooks
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):  # This will return the Browser value to setup method
    return request.config.getoption("--browser")

########### pytest HTML Report ################

# It is hook for Adding Environment info to HTML Report
def pytest_configure(config):
    config._metadata['Project Name'] = 'Grafi'
    config._metadata['Tester'] = 'Venkata Reddy'
    config._metadata['Browser'] = browser

# It is hook for delete/Modify Environment info to HTML Report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)
