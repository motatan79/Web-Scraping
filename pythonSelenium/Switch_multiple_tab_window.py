from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path=
                          'C:\\Users\m.pirela.escobar\OneDrive - Accenture\Documents\Courses\Selenium'
                          '\Chrome\chromedriver.exe')

# Connect to url webpage
driver.get("https://the-internet.herokuapp.com/windows")

# Click on Another New Tab
driver.find_element(By.CSS_SELECTOR, value="a[href='/windows/new']").click()

# Asking Selenium taking control of any page that will open on this automation process
child_window = driver.window_handles[1]
# ["parentid", "child_id"]

# Asking Selenium considering this new child web page as main web page
driver.switch_to.window(child_window)

# Proving we are on new page
print(driver.find_element(By.TAG_NAME, value='h3').text)
# close child window
driver.close()
# Comeback to window parent
parent_window = driver.window_handles[0]

driver.switch_to.window(parent_window)

assert "Opening a new window" == driver.find_element(By.TAG_NAME, value='h3').text

