from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

# 01 - Teste Alert with OK
driver = webdriver.Firefox()

driver.get('https://demo.automationtesting.in/Alerts.html')

driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[1]/ul/li[1]/a').click()

driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[2]/div[1]/button').click()

sleep(2)
driver.switch_to.alert.accept()
print('01 - Teste Alert - Passed')

# 02 - Teste Alert with OK & Cancel
driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[1]/ul/li[2]/a').click()

driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[2]/div[2]/button').click()

sleep(2)
driver.switch_to.alert.accept()

if driver.find_element(By.XPATH, '//*[@id="demo"]').text == 'You pressed Ok':
    print('02 - Teste Alert - Passed')
else:
    print('Test Alert Failed')

# 03 - Alert with Textbox
driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[1]/ul/li[3]/a').click()

driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[2]/div[3]/button').click()

sleep(2)
driver.switch_to.alert.accept()

if driver.find_element(By.XPATH, '//*[@id="demo1"]').text == 'Hello Automation Testing user How are you today':
    print('03 - Teste Alert - Passed')
else:
    print('Test Alert Failed')

driver.close()
