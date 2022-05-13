import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path=
                          'C:\\Users\m.pirela.escobar\OneDrive - Accenture\Documents\Courses\Selenium'
                          '\Chrome\chromedriver.exe')

# para conectarnos a la página web
driver.get("http://3.110.88.201/dropdownsPractise/")

# para seleccionar la lista dinámica desplegable
driver.find_element(By.ID, value='autosuggest').send_keys("ind")
# Hay que introducir un sleep time porque la lista tarda en desplegarse
time.sleep(2)

# PAra guardar la lista desplegable según nuestra opción de arriba
countries = driver.find_elements(By.CSS_SELECTOR, value="li[class='ui-menu-item'] a")
print(len(countries))

# El objetivo es darle click a cada una de las opciones en la lista y por eso iteramos sobre ella
# Para seleccionar el país en cuestión
for country in countries:
    if country.text == "India":
        country.click()
        break

# Para probar que lo obtenido en el dropdown corresponde a India
assert driver.find_element(By.ID, value="autosuggest").get_attribute('value') == "India"
