from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path=
                          'C:\\Users\m.pirela.escobar\OneDrive - Accenture\Documents\Courses\Selenium'
                          '\Chrome\chromedriver.exe')

driver.get("https://rahulshettyacademy.com/AutomationPractice/")

# Creamos una acción para ejecutar varias tareas sobre la página
action = ActionChains(driver)

# Creamos el objeto sobre el cual se moverá el mouse
menu = driver.find_element(By.ID, value="mousehover")

# Ejecutamos la acción sobre el objeto
action.move_to_element(menu).perform()

# Buscamos el elemento sobre el cual vamos hacer la acción
childMenu = driver.find_element(By.LINK_TEXT, value="Top")

# Realizamos la acción sobre el nuevo elemento
action.move_to_element(childMenu).click().perform()
