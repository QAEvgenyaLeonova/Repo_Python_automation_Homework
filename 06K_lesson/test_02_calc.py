from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService

def test_calculator_plus():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    wait = WebDriverWait(driver, 45)

    try:
        driver.get('https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html')
        driver.maximize_window()

        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[value="5"]'))).clear()
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[value="5"]'))).send_keys(45)

        xpath_seven = '//*[@id="calculator"]/div[2]/span[1]'
        wait.until(EC.visibility_of_element_located((By.XPATH, xpath_seven))).click()

        xpath_plus = '//*[@id="calculator"]/div[2]/span[4]'
        wait.until(EC.visibility_of_element_located((By.XPATH, xpath_plus))).click()

        xpath_eight = '//*[@id="calculator"]/div[2]/span[2]'
        wait.until(EC.visibility_of_element_located((By.XPATH, xpath_eight))).click()

        xpath_equally = '//*[@id="calculator"]/div[2]/span[15]'
        wait.until(EC.visibility_of_element_located((By.XPATH, xpath_equally))).click()

        wait.until(EC.text_to_be_present_in_element((By.CLASS_NAME, 'screen'), '15'))
        result_element = driver.find_element(By.CLASS_NAME, 'screen')

        if result_element.text.strip() == '15':
            print("Тест прошёл успешно: результат равен 15")
        else:
            print(f"Тест не прошёл: найден результат '{result_element.text.strip()}', ожидается '15'")

        assert result_element.text.strip() == '15', f'Результат не совпадает, найден: {result_element.text}'

    finally:
        driver.quit()

