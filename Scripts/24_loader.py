from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

driver: WebDriver = webdriver.Firefox()

driver.get('https://demo.automationtesting.in/Loader.html')

# 01 - Loader
driver.find_element(By.XPATH, '//*[@id="loader"]').click()

try:
    driver.find_element(By.XPATH, '/html/body/div[3]')
    print('Please Wait OK')
except 'Please Wait':
    print('Please Wait NOK')

try:
    wait = WebDriverWait(driver, 20)
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.btn-default')))
    print('01 - Loader - Passed')
except 'Loader':
    print('01 - Loader - Failed')

driver.close()
