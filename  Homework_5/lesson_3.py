from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Firefox()

driver.get('http://the-internet.herokuapp.com/inputs')
input_field = driver.find_element(By.CSS_SELECTOR, '[type="number"]')
input_field.send_keys('12345 - вышел зайчик погулять')
time.sleep(2)
input_field.clear()
time.sleep(1)
input_field.send_keys('54321 - кот залез на барабан, барабанит: «Там - парам!')
time.sleep(3)

driver.quit()