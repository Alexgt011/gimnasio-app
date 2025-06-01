import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class TestRegistroPlanAceptacion(unittest.TestCase):
    def setUp(self):
        chrome_options = Options()
        # chrome_options.add_argument('--headless')  # Activar si ya estás seguro
        self.driver = webdriver.Chrome(service=Service(), options=chrome_options)
        self.wait = WebDriverWait(self.driver, 20)
        self.driver.get("http://127.0.0.1:5000/planes")

    def test_registro_plan_aceptacion(self):
        driver = self.driver
        wait = self.wait

        # Nombre del plan
        wait.until(EC.presence_of_element_located((By.NAME, "nombre"))).send_keys("Plan Selenium OK")

        # Scroll manual al form
        driver.execute_script("window.scrollBy(0, 300);")

        # Forzar clic con JS si no se deja hacer click directo
        try:
            radio_duracion = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@name='tiempo_dur' and @value='1 Mes']")))
            driver.execute_script("arguments[0].click();", radio_duracion)
        except Exception as e:
            print("❌ Error seleccionando duración:", e)
            self.fail("No se pudo seleccionar '1 Mes'")

        try:
            radio_incluye = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@name='incluye' and @value='Solo Aerobicos']")))
            driver.execute_script("arguments[0].click();", radio_incluye)
        except Exception as e:
            print("❌ Error seleccionando incluye:", e)
            self.fail("No se pudo seleccionar 'Solo Aerobicos'")

        # Precio
        wait.until(EC.presence_of_element_located((By.NAME, "precio"))).send_keys("150")

        # Enviar formulario
        driver.find_element(By.XPATH, "//button[@type='submit']").click()
        time.sleep(2)

        # Verificación
        body_text = driver.find_element(By.TAG_NAME, "body").text
        self.assertIn("Plan Selenium OK", body_text)

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
