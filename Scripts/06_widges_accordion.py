from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()

driver.get('https://demo.automationtesting.in/Accordion.html')

# 01 - Accordion
driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div/div[1]/div'
                              '/div/div/div[1]/div[1]/h4/a').click()

try:
    driver.find_element(By.CSS_SELECTOR, '#collapse1 > div:nth-child(1)')
    print('Accordion 01 - Passed')
except:
    print('Accordion 01 - Failed')

# 02 - Accordion
driver.find_element(By.CSS_SELECTOR, 'div.panel:nth-child(2) > div:nth-child(1) > h4:nth-child(1) > '
                                     'a:nth-child(1)').click()

try:
    driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div/div[1]/div/div/div/div[2]/div[2]/div')
    print('Accordion 02 - Passed')
except:
    print('Accordion 02 - Failed')

# 03 - Accordion
driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div/div[1]/div').click()

try:
    driver.find_element(By.CSS_SELECTOR, '#collapse3 > div:nth-child(1)')
    print('Accordion 03 - Passed')
except:
    print('Accordion 03 - Failed')

# 04 - Accordion
driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div/div[1]/div/div/div/div[4]'
                              '/div[1]/h4/a').click()

try:
    driver.find_element(By.CSS_SELECTOR, '#collapse4 > div:nth-child(1)')
    print('Accordion 04 - Passed')
except:
    print('Accordion 04 - Failed')

driver.quit()
