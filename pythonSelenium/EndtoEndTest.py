from selenium import webdriver
from selenium.webdriver.common.by import By

# Invoking Chrome with specific options
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

chrome_options = webdriver.ChromeOptions()
# Starting browser in maximize mode
chrome_options.add_argument("--start-maximized")


driver = webdriver.Chrome(executable_path=
                          'C:\\Users\m.pirela.escobar\OneDrive - Accenture\Documents\Courses\Selenium'
                          '\Chrome\chromedriver.exe')

driver.get("https://rahulshettyacademy.com/angularpractice/")

# Completing name field
driver.find_element(By.XPATH, value="//input[@name='name']").send_keys("Moises")

# Selecting shop element
driver.find_element(By.CSS_SELECTOR, value="a[href*='shop']").click()

# On shop page, first we selected all products to create a list, after that we choose Blackberry element
products = driver.find_elements(By.XPATH, value="//div[@class='card h-100']")
for product in products:
    if product.find_element(By.XPATH, value="div/h4/a").text == 'Blackberry':
        product.find_element(By.XPATH, value="div/button").click()

# Checkout product
driver.find_element(By.XPATH, value="//*[contains(@class,'navbar-nav ml-auto')]").click()

# Chechout product
driver.find_element(By.CSS_SELECTOR, value="div button[class*='btn-success']").click()

# Writing on white space
driver.find_element(By.ID, value="country").send_keys("ind")

# Explicit Wait Time
wait = WebDriverWait(driver, 7)
wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, 'India')))
driver.find_element(By.LINK_TEXT,value="India").click()

# Select Agree condition
driver.find_element(By.CSS_SELECTOR, value="div[class*='checkbox']").click()

# Click Purchase bottom
driver.find_element(By.CSS_SELECTOR,value="[value='Purchase']").click()

# Evaluation for final message
message = driver.find_element(By.CSS_SELECTOR,value="[class*='alert-dismissible']").text

print(message)

assert "Success" in message

# Take screenshot for last page previous to close it
driver.get_screenshot_as_file("screen.png")

driver.close()


