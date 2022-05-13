import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path=
                          'C:\\Users\m.pirela.escobar\OneDrive - Accenture\Documents\Courses\Selenium'
                          '\Chrome\chromedriver.exe')

#implicit Wait time
driver.implicitly_wait(5)


# Connect to url
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")

# Writing an information in box
driver.find_element(By.CSS_SELECTOR, value="input.search-keyword").send_keys("ber")
time.sleep(4)

driver.find_elements(By.XPATH, value="//div[@class='products']/div")
print(len(driver.find_elements(By.XPATH, value="//div[@class='products']/div")))

# Para Seleccionar los productos
products = driver.find_elements(By.CSS_SELECTOR, value="div[class='product-action']")

for product in products:
    product.click()

driver.find_element(By.CSS_SELECTOR, value="img[alt='Cart']").click()

# Para seleccionar el botón de Proceed to Checkout
driver.find_element(By.XPATH, value="//button[text()='PROCEED TO CHECKOUT']").click()

# para ingresar el cupón descuento
driver.find_element(By.XPATH, value="//input[@class='promoCode']").send_keys("rahulshettyacademy")

# Para presionar promo button
driver.find_element(By.CSS_SELECTOR, value='.promoBtn').click()

# Para saber que la promoción fue aplicada
applied = driver.find_element(By.CSS_SELECTOR, value="span.promoInfo").text

assert "applied" in applied