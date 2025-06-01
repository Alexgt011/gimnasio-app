from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from faker import Faker
import time
import traceback

fake = Faker()

# Opciones de navegador
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
driver = webdriver.Chrome(options=options)
wait = WebDriverWait(driver, 10)

try:
    # Abre la página del formulario
    driver.get("http://127.0.0.1:5000/newinstructores")
    time.sleep(2)

    def fill_input(name, value):
        campo = wait.until(EC.presence_of_element_located((By.NAME, name)))
        driver.execute_script("arguments[0].scrollIntoView();", campo)
        time.sleep(0.3)
        campo.send_keys(value)

    # Llenar campos del formulario
    fill_input("nombre", fake.name())
    fill_input("edad", str(fake.random_int(min=25, max=60)))
    fill_input("direccion", fake.address())
    fill_input("user_name", fake.user_name())
    fill_input("password", "1234")

    # Seleccionar el radio de "Musculacion"
    rol_radio = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@name="rol" and @value="Musculacion"]')))
    driver.execute_script("arguments[0].scrollIntoView();", rol_radio)
    time.sleep(0.3)
    driver.execute_script("arguments[0].click();", rol_radio)

    # Horarios
    fill_input("turno_ini", "08:00")
    fill_input("turno_fin", "12:00")

    # Enviar formulario
    submit_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[@type="submit"]')))
    driver.execute_script("arguments[0].scrollIntoView();", submit_button)
    time.sleep(0.3)
    driver.execute_script("arguments[0].click();", submit_button)

    # Confirmar que se registró correctamente
    time.sleep(2)
    assert "instructores" in driver.current_url or "Instructor" in driver.page_source
    print("✅ Instructor registrado correctamente")

except Exception as e:
    print("❌ Test de registro de instructor FALLO")
    traceback.print_exc()

finally:
    driver.quit()

