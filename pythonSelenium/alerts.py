from selenium import webdriver
from selenium.webdriver.common.by import By

validateTest = "Option3"
driver = webdriver.Chrome(executable_path=
                          'C:\\Users\m.pirela.escobar\OneDrive - Accenture\Documents\Courses\Selenium'
                          '\Chrome\chromedriver.exe')
# Conectarse a la url
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

# Acceder a la casilla "Enter your name"
driver.find_element(By.XPATH, value="//input[@name='enter-name']").send_keys(validateTest)

# Para presionar el botón Alert
driver.find_element(By.CSS_SELECTOR, value="input[value='Alert']").click()

# Cuando aparece un pop-up Selenium no lo puede manejar porque está escrito en Java y Selenium maneja cosas en html
# Por ello hay que cambiar el driver a un modo .alert
alert = driver.switch_to.alert

# luego para extraer el texto en el pop-up usamos este nuevo objeto como driver
assert validateTest in alert.text

# para aceptar la alerta
alert.accept()

#Ahora hagamos el ejercicio de seleccionar el boton confirm y después Cancel en el pop-up
driver.find_element(By.ID, value='confirmbtn').click()
alert2 = driver.switch_to.alert
assert "confirm" in alert2.text
# para rechazar el pop-up , presionar Cancel
alert2.dismiss()