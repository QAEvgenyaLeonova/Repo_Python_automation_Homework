from selenium import webdriver
from selenium.webdriver.common.by import By

import time

driver = webdriver.Firefox()

driver.get('https://the-internet.herokuapp.com/login')

input_username = driver.find_element(By.CSS_SELECTOR, '#username')
input_username.send_keys('tomsmith')
time.sleep(1)

input_password = driver.find_element(By.CSS_SELECTOR, '#password')
input_password.send_keys('SuperSecretPassword!')
time.sleep(1)

input_blue = driver.find_element(By.CSS_SELECTOR, '.radius')
input_blue.click()

time.sleep(3)

driver.quit()