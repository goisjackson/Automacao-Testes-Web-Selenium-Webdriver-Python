from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Firefox()

driver.get('https://demo.automationtesting.in/Selectable.html')

# 01 - selectable

driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[1]/ul/li[1]/a').click()

try:
    driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[2]/div[1]/ul/li[2]').click()
    print('Selectable 01 - Passed')
except:
    print('Selectable 01 - Failed')

# driver.close()
