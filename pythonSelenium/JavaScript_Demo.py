from selenium import webdriver
from selenium.webdriver.common.by import By
# Bring browser
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(executable_path=
                          'C:\\Users\m.pirela.escobar\OneDrive - Accenture\Documents\Courses\Selenium'
                          '\Chrome\chromedriver.exe')

# Load web page into browser
driver.get("https://rahulshettyacademy.com/angularpractice/")

driver.find_element(By.NAME, value="name").send_keys("Moiss")
# En este primer caso no imprime nada porque al evaluar el elemento Selenium no evalúa el DOM
print(driver.find_element(By.NAME, value="name").text)

# Aquí si imprime lo que acabamos de enviar como keys porque estamos trabajando con atributos de
# get attribute en Java DOS Document
print(driver.find_element(By.NAME, value="name").get_attribute("value"))

# para acceder al valor construyendo el locator con el DOM usando JavaScript
print(driver.execute_script("return document.getElementsByName('name')[0].value"))
# En este caso estamos trabajando con el propio JavaScript en la página no hay nada de Selenium
#  Selenium solamente te está dando el control

# Otro ejemplo
shop_bottom = driver.find_element(By.CSS_SELECTOR, value="a[href*='shop'")

# Supongamos que no podemos hacer click sobre el botón, porque hay alguna ventana que lo tapa
# y por lo tanto Selenium no lo detecta
driver.execute_script('arguments[0].click();',shop_bottom)
# en argumentos va a estar una lista de todos los elementos que estén contenidos en la variable anterior

# PAra hacer scrolldown en la página no podemos usar Selenium pero si JavaScript
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")