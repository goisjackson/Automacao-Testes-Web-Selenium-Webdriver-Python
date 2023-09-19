from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()

driver.get('https://demo.automationtesting.in/Windows.html')

# 01 - Open New Tabbed Windows
driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[1]/ul/li[1]/a').click()

driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[2]/div[1]/a/button').click()

sleep(2)
driver.switch_to.window(driver.window_handles[1])
get_url = driver.current_url
if get_url == 'https://www.selenium.dev/':
    print('Url obtida =', get_url)
    print('url espera = https://www.selenium.dev/')
    print('01 - Open New Tabbed Windows - Passed')
else:
    print('01 - Open New Tabbed Windows - Failed')

driver.close()
print('_' * 40)
# 02 - Open New Seperate Windows
driver.switch_to.window(driver.window_handles[0])
driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[1]/ul/li[2]/a').click()

driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[2]/div[2]/button').click()

sleep(2)
driver.switch_to.window(driver.window_handles[1])
get_url = driver.current_url
if get_url == 'https://www.selenium.dev/':
    print('Url obtida   =', get_url)
    print('url esperada = https://www.selenium.dev/')
    print('02 - Open New Seperate Windows - Passed')
else:
    print('02 - Open New Seperate Windows - Failed')

driver.close()

print('_' * 40)
# 03 - Open Seperate Multiple Windows
driver.switch_to.window(driver.window_handles[0])
driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[1]/ul/li[3]/a').click()
driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[2]/div[3]/button').click()

sleep(3)
driver.switch_to.window(driver.window_handles[1])
get_url = driver.current_url

driver.switch_to.window(driver.window_handles[2])
get_url2 = driver.current_url

if get_url == 'https://www.selenium.dev/' and get_url2 == 'https://demo.automationtesting.in/Index.html':
    print('Url obtida =', get_url)
    print('url espera = https://www.selenium.dev/')

    print('Url obtida   =', get_url2)
    print('url esperada = https://demo.automationtesting.in/Index.html')
    print('03 - Open Seperate Multiple Windows - Passed')
else:
    print('03 - Open Seperate Multiple Windows - Failed')

driver.quit()
