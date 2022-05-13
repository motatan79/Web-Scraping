from selenium import webdriver

# Para invocar Chrome desde selenium
# Every exposes an executable file
# Through Selenium test we need to invoke the executable file which will then invoke actual browser
# aquí le pasamos el path del executable file entre paréntesis
# Run in Chrome
driver = webdriver.Chrome(executable_path='C:\\Users\m.pirela.escobar\OneDrive - Accenture\Documents\Courses\Selenium\Chrome\chromedriver.exe')

# Run in Firefox
#driver = webdriver.Firefox(executable_path='geckodriver.exe')

# Run in Internet Explorer (Isn't working)
#driver = webdriver.Ie(executable_path='C:\\Users\m.pirela.escobar\OneDrive - Accenture\Documents\Courses\Selenium\Explorer\IEDriverServer.exe')

# maximizing window, give you full screen
driver.maximize_window()

# Getting url
driver.get('https://rahulshettyacademy.com/') #get method to hit url on browser

# Get title of that web page
print(driver.title)

# Knowing if web page has been hacked
print(driver.current_url)

# Showing another web page
driver.get("https://rahulshettyacademy.com/AutomationPractice")

# Minimizing your window
driver.minimize_window()

# Para volver a la página anterior que había invocado
driver.back()
# Para refrescar la web page que estamos mirando actualmente
driver.refresh()


# Closing actual window web page
driver.close()




