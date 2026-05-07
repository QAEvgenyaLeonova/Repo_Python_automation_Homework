from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

try:
    driver.get('http://uitestingplayground.com/textinput')

    wait = WebDriverWait(driver, 10)
    text_field = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, '#newButtonName'))
    )

    text_field.send_keys('SkyPro')

    button = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, '.btn-primary'))
    )
    button.click()

    updated_button = wait.until(
        EC.text_to_be_present_in_element((By.CSS_SELECTOR, '.btn-primary'), 'SkyPro')
    )

    button_text = driver.find_element(By.CSS_SELECTOR, '.btn-primary').text
    print(button_text)  # Вывод: SkyPro

finally:
    driver.quit()
