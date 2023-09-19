from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Firefox()

driver.get('https://demo.automationtesting.in/Selectable.html')

# 01 - selectable serialize

driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[1]/ul/li[2]/a').click()

try:
    driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[2]/div[2]/ul/li[7]').click()
    texto = driver.find_element(By.XPATH, '//*[@id="result"]').text
    if texto == 'Functional Testing':
        print('Texto selecionado:  Functional Testing')
        print('Texto apresentado: ', texto)
        print('Selectable 01 - Passed')
except:
    print('Selectable 01 - Failed')

driver.close()
