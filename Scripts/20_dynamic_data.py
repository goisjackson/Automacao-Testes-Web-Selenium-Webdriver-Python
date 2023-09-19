from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()

driver.get('https://demo.automationtesting.in/DynamicData.html')
sleep(3)

# 01 - Dynamic Data
driver.find_element(By.XPATH, '//*[@id="save"]').click()
sleep(5)

try:
    driver.find_element(By.XPATH, '/html/body/section/div[1]/div/div/div/div[2]/div/img')
    print('Gerar Imagem - OK')
    print('-' * 40)
except 'teste image':
    print('Gerar Imagem - NOK')
    print('-' * 40)

try:
    name = driver.find_element(By.XPATH, '//*[@id="loading"]').text
    print(name)
    print('_' * 40)
    print('Dynamic Data 01 - Passed')
except 'validar nome':
    print('_' * 40)
    print('Dynamic Data 01 - Failed')

driver.quit()
