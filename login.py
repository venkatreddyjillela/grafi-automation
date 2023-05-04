from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.opera import OperaDriverManager

# set up the Chrome WebDriver using the driver manager
driver = webdriver.Chrome(ChromeDriverManager().install())

# set up the Edge WebDriver using the driver manager
# driver = webdriver.Edge(EdgeChromiumDriverManager().install())

# set up the Firefox WebDriver using the driver manager
# driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())

# set up the Opera WebDriver using the driver manager
# driver = webdriver.Opera(executable_path=OperaDriverManager().install())

# open grafi website
driver.get('https://stg.graficompose.com/')



# wait for 5 seconds
driver.implicitly_wait(5)

# close the browser window
driver.quit()

