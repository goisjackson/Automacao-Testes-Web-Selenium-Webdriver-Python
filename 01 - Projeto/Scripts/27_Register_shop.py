from time import sleep
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.webdriver import WebDriver

driver: WebDriver = webdriver.Firefox()

driver.get('https://practice.automationtesting.in/my-account/')

# 01 - Register Shop

# email
driver.find_element(By.XPATH, '//*[@id="reg_email"]').send_keys('jack02@jack02.com.br')

# senha
driver.find_element(By.XPATH, '//*[@id="reg_password"]').send_keys('123!@#qweQWE')
sleep(2)
driver.find_element(By.XPATH, '//*[@id="reg_password"]').send_keys(Keys.ENTER + Keys.ENTER)

try:
    sleep(3)
    driver.find_element(By.CSS_SELECTOR, 'li.woocommerce-MyAccount-navigation-link:nth-child(6) > a:nth-child(1)')
    print('Register Shop - Passed')
except 'Register Shop':
    print('Register Shop - Failed')

driver.close()
