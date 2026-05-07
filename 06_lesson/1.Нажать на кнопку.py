from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

edge_driver_path = "C:\\Users\\user\\Documents\\2.НЕ ПЕРЕКИНУТОЕ\\5.Автоматизация тестирования на Python\\Урок_1. Знакомство с языком Python\\Эдже_драйвер\\msedgedriver.exe"
driver = webdriver.Edge(service=EdgeService(executable_path=edge_driver_path))

try:
    driver.get('http://uitestingplayground.com/ajax')

    driver.find_element(By.CSS_SELECTOR, '.btn-primary').click()


    wait = WebDriverWait(driver, 20)
    success_element = wait.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, '.bg-success'))
    )

    text_ajax = success_element.text
    print(text_ajax)

finally:
    driver.quit()
