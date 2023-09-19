from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
passed = []

driver = webdriver.Firefox()

driver.get('https://demo.automationtesting.in/Frames.html')

# 01 - Iframe with in an Iframe
driver.find_element(By.XPATH, '/html/body/section/div[1]/div/div/div/div[1]/div/ul/li[2]/a').click()

print('--- Teste Parcial')
try:
    frame1 = driver.find_element(By.CSS_SELECTOR, '#Multiple > iframe:nth-child(1)')
    sleep(2)
    driver.switch_to.frame(frame1)
    print('Iframe 01 - Passed')
    passed.append(1)
except:
    print('Iframe 01 - Failed')

try:
    frame2 = driver.find_element(By.CSS_SELECTOR, '.iframe-container > iframe:nth-child(2)')
    sleep(2)
    driver.switch_to.frame(frame2)
    print('Iframe 02 - Passed')
    passed.append(1)
except:
    print('Iframe 02 - Failed')

try:
    driver.find_element(By.CSS_SELECTOR, '.col-xs-6 > input:nth-child(1)').send_keys('Iframe3')
    print('Iframe 03 - Passed')
    passed.append(1)
except:
    print('Iframe 03 - Failed')

print('_' * 40)
print('--- Teste Completo')
if len(passed) == 3:
    print('01 - Iframe with in an Iframe - Passed')
else:
    print('01 - Iframe with in an Iframe - Failed')

driver.quit()
