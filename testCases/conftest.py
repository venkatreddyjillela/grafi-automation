import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from utilities.customLogger import LogGen

logger = LogGen.loggen()

import os

location = os.getcwd() + "\\Downloads"

@pytest.fixture()
def setup(browser):
    if browser=='firefox':
        from selenium.webdriver.firefox.service import Service        
        from selenium.webdriver.firefox.options import Options
        firefox_options = webdriver.FirefoxOptions()
        firefox_options.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/msword")  # MIME type of the file you want to download (ms word is used here)
        firefox_options.set_preference("browser.download.manager.showWhenStarting", False)
        firefox_options.set_preference("browser.download.folderList", 2)
        firefox_options.set_preference("browser.download.dir", location)

        # Download the GeckoDriver executable using the WebDriver Manager
        executable_path = GeckoDriverManager().install()

        # Create a Service object
        service = Service(executable_path)

        # Create a Firefox webdriver instance with the Service object
        driver = webdriver.Firefox(service=service, options=firefox_options)
        logger.info("Launching firefox browser.........")
        print("Launching firefox browser.........")
        

    elif browser=='Edge':
        from selenium.webdriver.edge.service import Service
        from selenium.webdriver.edge.options import Options
        preferences = {"download.default_directory": location}
        edge_options = webdriver.EdgeOptions()
        edge_options.add_experimental_option("prefs", preferences)

        # Download the EdgeDriver executable using the WebDriver Manager
        executable_path = EdgeChromiumDriverManager().install()

        # Create a Service object
        service = Service(executable_path)

        # Create an Edge webdriver instance with the Service object
        driver = webdriver.Edge(service=service, options=edge_options)
        logger.info("Launching Edge browser.........")
        print("Launching Edge browser.........")

    else:
        from selenium.webdriver.chrome.options import Options
        from selenium.webdriver.chrome.service import Service
        preferences = {"download.default_directory": location, "plugins.always_open_pdf_externally": True}
        # Create Chrome options object
        chrome_options = Options()
        chrome_options.add_experimental_option("prefs", preferences)
        # chrome_options.add_argument('--headless')

        # Download the ChromeDriver executable using the WebDriver Manager
        executable_path = ChromeDriverManager().install()
       
        # Create a Service object
        service = Service(executable_path)

        # Create a Chrome webdriver instance with the Service object
        driver = webdriver.Chrome(service=service, options=chrome_options)
        logger.info("Launching default chrome browser.........")
        print("Launching default chrome browser.........")

    # implicit wait for 10 seconds
    driver.implicitly_wait(10)
    # maximize window
    driver.maximize_window()

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
@pytest.hookimpl(optionalhook=True)
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)
