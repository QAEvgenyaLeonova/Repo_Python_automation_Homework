from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService

def test_users_registration():
    driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    wait = WebDriverWait(driver, 10)  # Явное ожидание до 10 секунд

    try:
        driver.get('https://www.saucedemo.com/')
        driver.maximize_window()

        wait.until(EC.visibility_of_element_located((By.ID, 'user-name'))).send_keys('standard_user')
        wait.until(EC.visibility_of_element_located((By.ID, 'password'))).send_keys('secret_sauce')
        wait.until(EC.element_to_be_clickable((By.ID, 'login-button'))).click()

        WebDriverWait(driver, 5).until(lambda d: d.execute_script('return document.readyState') == 'complete')

        wait.until(EC.visibility_of_element_located((By.ID, 'add-to-cart-sauce-labs-backpack'))).click()
        wait.until(EC.visibility_of_element_located((By.ID, 'add-to-cart-sauce-labs-bolt-t-shirt'))).click()
        wait.until(EC.visibility_of_element_located((By.ID, 'add-to-cart-sauce-labs-onesie'))).click()

        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.shopping_cart_link'))).click()

        WebDriverWait(driver, 5).until(lambda d: d.execute_script('return document.readyState') == 'complete')

        wait.until(EC.visibility_of_element_located((By.ID, 'checkout'))).click()

        wait.until(EC.visibility_of_element_located((By.ID, 'first-name'))).send_keys('Евгения')
        wait.until(EC.visibility_of_element_located((By.ID, 'last-name'))).send_keys('Леонова')
        wait.until(EC.visibility_of_element_located((By.ID, 'postal-code'))).send_keys('644 058')
        wait.until(EC.visibility_of_element_located((By.ID, 'continue'))).click()

        WebDriverWait(driver, 5).until(lambda d: d.execute_script('return document.readyState') == 'complete')

        total_element = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div.summary_total_label')))
        total_text = total_element.text
        total_value = total_text.replace('Total: ', '').strip()

        if total_value == '$58.29':
            print('Тест успешно прошел: сумма совпадает.')
        else:
            print(f'Ошибка: сумма не совпадает. Получена сумма: {total_value}')


    finally:
        driver.quit()
