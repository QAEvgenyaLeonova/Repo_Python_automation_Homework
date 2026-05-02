from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

service = ChromeService(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

try:
    driver.get('http://uitestingplayground.com/classattr')
    driver.implicitly_wait(10)

    blue_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, '.btn-primary'))
    )


    blue_button.click()
    print("Клик по синей кнопке выполнен!")

    time.sleep(5)

finally:
    driver.quit()
