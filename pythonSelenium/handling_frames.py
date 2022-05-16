from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path=
                          'C:\\Users\m.pirela.escobar\OneDrive - Accenture\Documents\Courses\Selenium'
                          '\Chrome\chromedriver.exe')

# Connect to url webpage
driver.get("https://the-internet.herokuapp.com/iframe")

# First we need to switch to THE FRAME before handle it.
driver.switch_to.frame("mce_0_ifr")

# Para limpiar el contenido en el recuadro
driver.find_element(By.CSS_SELECTOR, value="body[id='tinymce']").clear()

# Para escribir en el frame
driver.find_element(By.CSS_SELECTOR, value="body[id='tinymce']").send_keys("I am ready to automate")

# Para asegurarnos que la prueba fue exitosa
# Si queremos hacer algo fuera del Frame debemos salir de él
driver.switch_to.default_content()
print(driver.find_element(By.TAG_NAME, value='h3').text)