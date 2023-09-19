from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Firefox()

driver.get('https://demo.automationtesting.in/Charts.html')
sleep(3)

# 01 - Charts
# Monthly Volume
# Shares Traded
if driver.find_element(By.XPATH, '/html/body/section/div[1]/div/div/div/div/div/div[1]/div/'
                                 'div[3]/div[1]/ul/li[1]/h3').text == '13.5 M':
    print('Shares Traded - OK')
else:
    print('Shares Traded - NOK')

# Market Cap
if driver.find_element(By.XPATH, '/html/body/section/div[1]/div/div/div/div/div/div[1]/div/'
                                 'div[3]/div[1]/ul/li[2]/h3').text == '28.44 B':
    print('Market Cap - OK')
else:
    print('Market Cap - NOK')

# Data Transfer
# Video
if driver.find_element(By.XPATH, '/html/body/section/div[1]/div/div/div/div/div/div[2]/div/'
                                 'div[3]/div[1]/ul/li[1]/h2').text == '62%':
    print('Video % - OK')
else:
    print('Video % - NOK')

# Photo
if driver.find_element(By.XPATH, '/html/body/section/div[1]/div/div/div/div/div/div[2]/div/div'
                                 '[3]/div[1]/ul/li[2]/h2').text == '21%':
    print('Photo % - OK')
else:
    print('Photo % - NOK')

# Audio
if driver.find_element(By.XPATH, '/html/body/section/div[1]/div/div/div/div/div/div[2]'
                                 '/div/div[3]/div[1]/ul/li[3]/h2').text == '10%':
    print('Audio % - OK')
    print('_' * 40)
    print('Charts 01 - Passed')
else:
    print('Audio % - NOK')
    print('Charts 01 - Failed')

driver.quit()
