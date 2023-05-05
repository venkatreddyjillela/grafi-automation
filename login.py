from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.opera import OperaDriverManager

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import logging

# Set the logging level to CRITICAL
logging.basicConfig(level=logging.CRITICAL)

# Create Chrome options object
chrome_options = Options()
# chrome_options.add_argument('--headless')

# Create driver object with the ChromeDriverManager and the options object
driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)

# set up the Edge WebDriver using the driver manager
# driver = webdriver.Edge(EdgeChromiumDriverManager().install())

# set up the Firefox WebDriver using the driver manager
# driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())

# set up the Opera WebDriver using the driver manager
# driver = webdriver.Opera(executable_path=OperaDriverManager().install())

# explicitly wait for 10 seconds when performing a find_element operation
wait = WebDriverWait(driver, 10)

def test_login_page(email, password):
    # open grafi website login page
    driver.get('https://stg.graficompose.com/')

    # email field element
    email_field = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@id="username"]')))
    # password field element
    password_field = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@id="password"]')))

    # login button element
    login_button = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@type="submit"]')))

    # enter email and password and click on login button
    email_field.send_keys(email)
    password_field.send_keys(password)
    login_button.click()

    try:
        # Check error message for invalid email or password scenario
        if 'Invalid username or password.' not in driver.page_source:
            # Explicit wait for the page to load after successful login
            wait.until(EC.url_contains('home'))
    except:
        pass

    # Check if login was successful or not
    if "authenticate" in driver.current_url.lower():
        # Invalid email or password scenario
        assert 'Invalid username or password.' in driver.page_source
    elif "home" in driver.current_url.lower():
        # Valid email and password scenario
        assert 'Get Started Here' in driver.page_source
    else:
        # Unexpected scenario
        assert False, "Unexpected scenario occurred."


# valid email and password
valid_email = "venkatjillela2210@gmail.com"
valid_password = "Venky@1234"

# invalid email and password
invalid_email = "invalid_user@example.com"
invalid_password = "invalid_password"



# Test invalid email and password
test_login_page(invalid_email, invalid_password)

# Test invalid email and valid password
test_login_page(invalid_email, valid_password)

# Test valid email and invalid password
test_login_page(valid_email, invalid_password)

# Test valid email and password
test_login_page(valid_email, valid_password)









# close the browser window
driver.quit()
