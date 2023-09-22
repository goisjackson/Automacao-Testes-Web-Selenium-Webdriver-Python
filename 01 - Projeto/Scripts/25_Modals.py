from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.webdriver import WebDriver

driver: WebDriver = webdriver.Firefox()

driver.get('https://demo.automationtesting.in/Modals.html')

# 01 - Modals

# Bootstrap Modal
try:
    driver.find_element(By.XPATH, '/html/body/section/div[1]/div[1]/div/div[2]/a').click()

    sleep(3)
    texto = driver.find_element(By.CSS_SELECTOR, 'div.modal-body:nth-child(2) > p:nth-child(5)')
    driver.execute_script("arguments[0].scrollIntoView()", texto)

    sleep(3)
    driver.find_element(By.XPATH, '/html/body/section/div[1]/div[1]/div/div[2]/div/div/div/div[2]'
                                  '/button').click()
    print('Bootstrap Modal - OK')
except 'Bootstrap Modal':
    print('Bootstrap Modal - NOK')

# Multiple Modals
# Button Launch modal
try:
    sleep(2)
    driver.find_element(By.XPATH, '/html/body/section/div[1]/div[2]/div/div[2]/a').click()

    # Button Launch modal 02
    sleep(2)
    driver.find_element(By.CSS_SELECTOR, 'a.btn:nth-child(7)').click()

    # Button Launch modal 03
    sleep(2)
    driver.find_element(By.CSS_SELECTOR, 'div.modal-footer:nth-child(6) > a:nth-child(2)').click()
    print('Multiple Modals - OK')
    print('_' * 40)
    print('Modals - Passed')
except 'Multiple Modals':
    print('Multiple Modals - NOK')
    print('_' * 40)
    print('Modals - Failed')

driver.close()
