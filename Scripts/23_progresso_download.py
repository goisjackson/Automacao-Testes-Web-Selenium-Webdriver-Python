from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.webdriver import WebDriver

driver: WebDriver = webdriver.Firefox()

driver.get('https://demo.automationtesting.in/JqueryProgressBar.html')

# 01 - Progress Bar
driver.find_element(By.XPATH, '//*[@id="downloadButton"]').click()

try:
    while True:
        barra = driver.find_element(By.XPATH, '/html/body/div/div[2]/div[1]').text
        if barra == 'Complete!':
            print('_' * 40)
            print('Complete!')
            print('01 - Progress Bar - Passed')
            break
        else:
            sleep(1)
            print(barra)
except 'Progress Bar':
    print('01 - Progress Bar - Failed')

driver.close()
