from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.webdriver import WebDriver

driver: WebDriver = webdriver.Firefox()

driver.get('https://demo.automationtesting.in/ProgressBar.html')

# 01 - ProgressBar
driver.find_element(By.XPATH, '//*[@id="cricle-btn"]').click()

progressbar_text = driver.find_element(By.XPATH, '/html/body/section/div[1]/div/div/div/div').text

try:
    while progressbar_text == '100':
        print(progressbar_text)
    print('Progress Bar - Passed')
except 'Progress Bar':
    print('Progress Bar - Failed')

driver.close()
