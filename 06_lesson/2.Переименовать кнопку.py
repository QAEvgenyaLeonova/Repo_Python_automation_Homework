from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

driver.get('http://uitestingplayground.com/textinput')

text_new = driver.find_element(By.CSS_SELECTOR, '#newButtonName')
text_new.send_keys('SkyPro')

press_button = driver.find_element(By.CSS_SELECTOR, '.btn-primary')
press_button.click()

sleep(2)

button_text = driver.find_element(By.CSS_SELECTOR, '.btn-primary').text
print(button_text)

sleep(2)

driver.quit()

