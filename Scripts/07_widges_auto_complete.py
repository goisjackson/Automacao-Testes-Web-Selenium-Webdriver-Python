from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()

driver.get('https://demo.automationtesting.in/AutoComplete.html')

# 01 - Autocomplete

driver.find_element(By.XPATH, '/html/body/section/div[1]/div[2]/div[1]/div').click()
sleep(2)

driver.find_element(By.XPATH, '//*[@id="searchbox"]').send_keys('Brazil')
sleep(3)

driver.find_element(By.CSS_SELECTOR, '#ui-id-1').click()
sleep(3)

driver.find_element(By.XPATH, '/html/body/section/div[1]/div[2]/div[1]/div').click()
sleep(2)

driver.find_element(By.XPATH, '//*[@id="searchbox"]').send_keys('Japan')
sleep(3)

driver.find_element(By.CSS_SELECTOR, '#ui-id-1').click()
sleep(3)

try:
    # confirmado seleção
    t = driver.find_element(By.XPATH, '/html/body/section/div[1]/div[2]/div[1]/div/div').text
    sleep(2)
    if 'Brazil' == t:
        print('Seleção Informada = Brazil')
        print('Seleção Capturada = ', t)
        print('Seleção 01 - Passed')
    else:
        print('Seleção 01 - Failed')
    sleep(2),
    # fechando seleção
    driver.find_element(By.XPATH, '/html/body/section/div[1]/div[2]/div[1]/div/div/span').click()
    sleep(2)

    # confirmado seleção
    t = driver.find_element(By.XPATH, '/html/body/section/div[1]/div[2]/div[1]/div/div').text
    sleep(2)
    if 'Japan' == t:
        print('Seleção Informada = Japan')
        print('Seleção Capturada = ', t)
        print('Seleção 02 - Passed')
    else:
        print('Seleção 02 - Failed')
    sleep(2),
    # fechando seleção
    driver.find_element(By.XPATH, '/html/body/section/div[1]/div[2]/div[1]/div/div/span').click()
    sleep(2)
    print('Autocomplete 01 - Passed')
except:
    print('Autocomplete 01 - Failed')

driver.quit()
