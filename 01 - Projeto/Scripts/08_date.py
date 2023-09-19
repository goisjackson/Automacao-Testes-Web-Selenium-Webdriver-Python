from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()

driver.get('https://demo.automationtesting.in/Datepicker.html')

# 01 - Date
try:
    driver.find_element(By.XPATH, '//*[@id="datepicker1"]').click()
    driver.find_element(By.XPATH, '/html/body/div/div/a[2]').click()
    driver.find_element(By.XPATH, '/html/body/div/table/tbody/tr[3]/td[1]').click()
    print('Data 01 - Passed')
except:
    print('Data 01 - Failed')

# 02 - Date
try:
    driver.find_element(By.XPATH, '//*[@id="datepicker2"]').click()
    driver.find_element(By.XPATH, '/html/body/div[2]/div/div[1]/a[3]').click()
    driver.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/div/div/select[2]').click()
    driver.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/div/div/select[2]/option[13]').click()
    driver.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/div/table/tbody/tr[2]/td[3]/a').click()
    print('Data 02 - Passed')
except:
    print('Data 02 - Failed')

# driver.quit()
