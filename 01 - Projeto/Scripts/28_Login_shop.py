from time import sleep
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.webdriver import WebDriver

driver: WebDriver = webdriver.Firefox()

driver.get('https://practice.automationtesting.in/my-account/')

# 01 - Login Shop

# email
driver.find_element(By.XPATH, '//*[@id="username"]').send_keys('jack02@jack02.com.br')

# senha
driver.find_element(By.XPATH, '//*[@id="password"]').send_keys('123!@#qweQWE')
sleep(2)

# button
(driver.find_element(By.CSS_SELECTOR,
                     'p.form-row:nth-child(3) > input:nth-child(3)').send_keys(Keys.ENTER + Keys.ENTER))

try:
    sleep(3)
    driver.find_element(By.CSS_SELECTOR, 'li.woocommerce-MyAccount-navigation-link:nth-child(6) > a:nth-child(1)')
    print('Login Shop - Passed')
except 'login Shop':
    print('Login Shop - Failed')

driver.close()
