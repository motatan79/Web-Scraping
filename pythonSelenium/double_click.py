from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path=
                          'C:\\Users\m.pirela.escobar\OneDrive - Accenture\Documents\Courses\Selenium'
                          '\Chrome\chromedriver.exe')

driver.get("https://chercher.tech/practice/practice-pop-ups-selenium-webdriver")

# Creamos una acción para ejecutar varias tareas sobre la página
action = ActionChains(driver)

# Para darle doble click sobre el elemento
action.double_click(driver.find_element(By.CSS_SELECTOR, value="input[id='double-click']")).perform()

# Para poder trabajar con la ventana que es Java
alert = driver.switch_to.alert

assert alert.text == "You double clicked me!!!, You got to be kidding me"

alert.accept()
