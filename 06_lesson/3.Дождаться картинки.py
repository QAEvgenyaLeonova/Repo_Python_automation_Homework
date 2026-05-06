from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService


driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.implicitly_wait(20)

driver.get('https://bonigarcia.dev/selenium-webdriver-java/loading-images.html')

img_element = driver.find_element(By.CSS_SELECTOR, "img:nth-of-type(3)")
src_value = img_element.get_attribute("src")
print(f'Значение атрибута src у третьей картинки: {src_value}')

sleep(3)

driver.quit()






