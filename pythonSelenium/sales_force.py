from selenium import webdriver
from selenium.webdriver.common.by import By
# Bring browser
driver = webdriver.Chrome(executable_path=
                          'C:\\Users\m.pirela.escobar\OneDrive - Accenture\Documents\Courses\Selenium'
                          '\Chrome\chromedriver.exe')

# para conectarse a la página
driver.get("https://login.salesforce.com/?locale=eu")

#para obtener la casilla del nombre, construyendo el tag con css desde un id
driver.find_element(By.CSS_SELECTOR, value="input#username").send_keys(("Moises"))
#para rellenar la casilla de password, construyendo la expresión regular usando CSS
driver.find_element(By.CSS_SELECTOR, value='input#password').send_keys("")
# para rellenar la casilla de password, construyendo la expresión regular para clases usando CSS
driver.find_element(By.CLASS_NAME, value='input.password').send_keys("piloto02")

# PAra limpiar la casilla de password
driver.find_element(By.CLASS_NAME, value='input.password').clear()

# Para acceder a un link construyendo el path con link text.
# Aquí va funcionar porque el tag está asociado a un anchor "a"
driver.find_element(By.LINK_TEXT, value='Forgot Your Password?').click()

# Para construir el Xpath on text
driver.find_element(By.NAME, value='cancel').click()

# Construyendo el XPATH desde el padre al hijo
print(driver.find_element(By.XPATH, value="//form[@name='login']/div[1]/label").text)

# Construyendo el CSS desde el padre para obtener el hijo pero con el elemento password
print(driver.find_element(By.CSS_SELECTOR, value="form[name='login'] label:nth-child(4)").text)


