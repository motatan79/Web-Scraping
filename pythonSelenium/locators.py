from selenium import webdriver
from selenium.webdriver.common.by import By
# Bring browser
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(executable_path=
                          'C:\\Users\m.pirela.escobar\OneDrive - Accenture\Documents\Courses\Selenium'
                          '\Chrome\chromedriver.exe')

# Load web page into browser
driver.get("https://rahulshettyacademy.com/angularpractice/")

# Aquí encontramos objeto según el locator que vemos en INSPECT
#driver.find_element(By.NAME, value="name").send_keys("Moises")

#Encontrar el objeto nombre por CSS
driver.find_element(By.CSS_SELECTOR, value="input[name='name']").send_keys("Moises")

# llenamos email con name
driver.find_element(By.NAME, value = 'email').send_keys("prueba@gmail.com")

# Para hacer check en una selección
driver.find_element(By.ID, value="exampleCheck1").click()

# Para señalar en una lista desplegable
# primero se crea el objeto que tiene la clase Select
dropdown = Select(driver.find_element(By.ID, value="exampleFormControlSelect1"))
#puedes seleccionar de varias maneras
# Por visible text
dropdown.select_by_visible_text("Male")
# Por Index
dropdown.select_by_index(1)

# Usando el xpath para exportar lo que hemos llenado en el formulario, haciendo click en el botón
driver.find_element(By.XPATH, value = "//input[@type='submit']").click()

# Para saber si el proceso fue exitoso usando class_name
#print(driver.find_element(By.CLASS_NAME, value='alert-success').text)
# Para saber si el proceso fue exitoso usando css_selector y expresiones regulares
#print(driver.find_element(By.CSS_SELECTOR, value= "[class*='alert-success']").text)

# Para saber si el proceso fue exitoso usando xpath y expresiones regulares
message = driver.find_element(By.XPATH, value="//*[contains(@class,'alert-success')]").text

# Para validar que el proceso ha sido completado
assert "Success" in message
