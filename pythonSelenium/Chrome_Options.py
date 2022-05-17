from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

# Invoking Chrome with specific options
chrome_options = webdriver.ChromeOptions()
# Starting browser in maximize mode
chrome_options.add_argument("--start-maximized")
# Headless , so this way you can't see the execution behind , you only see the front end and the result
# and this option is more famous because it's time less consuming
#chrome_options.add_argument("headless")
# Ignoring Certification Errors
chrome_options.add_argument("--ignore-certificate-error")

driver = webdriver.Chrome(executable_path=
                          'C:\\Users\m.pirela.escobar\OneDrive - Accenture\Documents\Courses\Selenium'
                          '\Chrome\chromedriver.exe', options=chrome_options)

driver.get("https://rahulshettyacademy.com/angularpractice/")

# Print title of the page
print(driver.title)

