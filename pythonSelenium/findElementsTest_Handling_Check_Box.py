from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path=
                          'C:\\Users\m.pirela.escobar\OneDrive - Accenture\Documents\Courses\Selenium'
                          '\Chrome\chromedriver.exe')

# Conectarse a la url
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

# Para obtener todos los elementos que son Checkbox
check_boxes = driver.find_elements(By.XPATH, value="//input[@type='checkbox']")
print(len(check_boxes))
print(check_boxes)

# PAra seleccionar todas las checkboxes
'''for check_box in check_boxes:
    check_box.click()
    # Para saber si la checkbox fue seleccionada o no usamos el método .is_selected()
    assert check_box.is_selected()'''

# Para seleccionar sólo la caja # 2
for check_box in check_boxes:
    # usamos el atributo value para ver el "option2"
    print(check_box.get_attribute("value"))
    if check_box.get_attribute("value") == 'option2':
        check_box.click()
        # Para saber si la checkbox fue seleccionada o no, usamos el método .is_selected()
        assert check_box.is_selected()

'''if check_box.find_element(By.XPATH, value="//input[@value='option2']"):
        check_box.click()
        # Para saber si la checkbox fue seleccionada o no, usamos el método .is_selected()
        assert check_box.is_selected()'''

# para el caso en que sólo se pueda seleccionar un botón porque la página permite una única selección
#driver.find_element(By.XPATH, value="//input[@value='radio3']").click()

radio_buttons = driver.find_elements(By.NAME, value="radioButton")
radio_buttons[2].click()
assert radio_buttons[2].is_selected()

