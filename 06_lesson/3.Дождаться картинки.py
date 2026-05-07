from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.implicitly_wait(20)

try:
    driver.get('https://bonigarcia.dev/selenium-webdriver-java/loading-images.html')

    wait = WebDriverWait(driver, 20)

    img_element = wait.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "img:nth-of-type(3)"))
    )

    src_value = img_element.get_attribute("src")

    print(f'Значение атрибута src у третьей картинки: {src_value}')

finally:
    driver.quit()

