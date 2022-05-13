import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

driver = webdriver.Chrome(executable_path=
                          'C:\\Users\m.pirela.escobar\OneDrive - Accenture\Documents\Courses\Selenium'
                          '\Chrome\chromedriver.exe')

# Connect to url
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")

# Writing an information in box
driver.find_element(By.CSS_SELECTOR, value="input.search-keyword").send_keys("ber")
time.sleep(4)

driver.find_elements(By.XPATH, value="//div[@class='products']/div")
print(len(driver.find_elements(By.XPATH, value="//div[@class='products']/div")))

# Para Seleccionar los productos
products = driver.find_elements(By.XPATH, value="//div[@class='product-action']/button")

all_items = []
for product in products:
    p = product.find_element(By.XPATH, value="parent::div/parent::div/h4").text
    all_items.append(p)
    product.click()
print(all_items)

driver.find_element(By.CSS_SELECTOR, value="img[alt='Cart']").click()

# Para seleccionar el botón de Proceed to Checkout
driver.find_element(By.XPATH, value="//button[text()='PROCEED TO CHECKOUT']").click()



#Explicit Wait time. Para esperar que cargue el checkout y luego introducir el código
wait = WebDriverWait(driver, 5)
wait.until(expected_conditions.presence_of_element_located((By.CLASS_NAME, 'promoCode')))

# Para Extraer el monto antes del descuento
previous_disc = float(driver.find_element(By.CLASS_NAME, value="totAmt").text)
print(previous_disc)

# para ingresar el cupón descuento
driver.find_element(By.XPATH, value="//input[@class='promoCode']").send_keys("rahulshettyacademy")

# Para tomar el nombre de los elementos en la tabla
vegetables = driver.find_elements(By.CSS_SELECTOR, value="p.product-name")

list2 = []
for veg in vegetables:
    list2.append(veg.text)
print(list2)

assert all_items == list2
# Para presionar promo button
driver.find_element(By.CSS_SELECTOR, value='.promoBtn').click()

driver.implicitly_wait(5)

# Para saber que la promoción fue aplicada
applied = driver.find_element(By.XPATH, value="//span[@class='promoInfo']").text

assert "applied" in applied


# Para extraer total después del descuento
after_disc = float(driver.find_element(By.CLASS_NAME, value="discountAmt").text)
print(after_disc)
assert previous_disc > after_disc

# Para extraer el precio de cada producto
prices = driver.find_elements(By.CSS_SELECTOR,value="tr td:nth-child(5) p[class='amount']")

#total_cost= []
#for price in prices:
#    total_cost.append(int(price.text))

total_cost = 0
for price in prices:
    total_cost += int(price.text)

print(total_cost)
assert total_cost == previous_disc
