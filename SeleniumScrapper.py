
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time


#ABRIR PAGINA

chrome_options = webdriver.ChromeOptions()
prefs = {"profile.defaul_content_setting_values.notifications":2}
chrome_options.add_experimental_option("prefs",prefs)

driver = webdriver.Chrome("C:\\Users\\User\\ChromeDriver\\chromedriver-win64\\chromedriver.exe", chrome_options=chrome_options)
driver.get("https://www.facebook.com/?locale=es_LA")
print(driver.title)

#iniciar Sesion
username = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='email']")))
password = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='pass']")))
username.clear()
password.clear()
#correo electronico para iniciar sesion
username.send_keys("correofalso@gmail.com ")
#contraseña del usuario
password.send_keys("*******")
#click button
button = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"button[name='login']"))).click()
time.sleep(1000)

name="email"




