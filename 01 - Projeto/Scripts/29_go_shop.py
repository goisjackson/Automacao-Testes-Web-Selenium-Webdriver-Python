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

# go shop
sleep(3)
try:
    li_element = driver.find_element(By.XPATH, '//*[@id="menu-item-40"]')
    sleep(2)
    shop_link = li_element.find_element(By.CSS_SELECTOR, '#menu-item-40 > a:nth-child(1)')
    sleep(2)
    shop_url = shop_link.get_attribute("href")
    sleep(2)
    driver.get(shop_url)
    print('Go Shop - Passed')
except 'go shop':
    print('Go Shop - Failed')

driver.close()
