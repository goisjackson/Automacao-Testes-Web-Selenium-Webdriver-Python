from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Firefox()

driver.get('https://demo.automationtesting.in/TinyMCE.html')

# 01 - Editor texto
try:
    driver.find_element(By.XPATH, '/html/body/section/div[1]/div/div/textarea').send_keys('Nome: Jackson\n'
                                                                                      'Estado: São Paulo')
    print('Editor texto 01 - Passed')
except:
    print('Editor texto 01 - Failed')

driver.quit()
