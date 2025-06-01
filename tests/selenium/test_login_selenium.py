from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Inicia Chrome
driver = webdriver.Chrome()

try:
    # Abrir la página de login de tu app Flask
    driver.get("http://127.0.0.1:5000/login")
    time.sleep(1)

    # Rellenar el formulario
    username_input = driver.find_element(By.NAME, "username")
    password_input = driver.find_element(By.NAME, "password")
    username_input.send_keys("admin")
    password_input.send_keys("admin123")

    # Enviar formulario
    driver.find_element(By.XPATH, "//input[@type='submit']").click()
    time.sleep(2)

    # Mostrar mensaje si no hubo errores
    print("✅ Test de login con Selenium: PASÓ (sin validación de texto)")

except Exception as e:
    print("❌ Test de login con Selenium: FALLO")
    print("Error:", e)

finally:
    driver.quit()

