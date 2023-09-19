from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.webdriver import WebDriver

driver: WebDriver = webdriver.Firefox()

driver.get('https://demo.automationtesting.in/FileUpload.html')

# 01 - File Upload
try:
    driver.find_element(By.XPATH, '//*[@id="input-4"]').send_keys(r"C:\Users\jacks\Desktop\mib.jpg")
    print('01 - File Upload - Passed')
except 'File Upload':
    print('01 - File Upload - Failed')

driver.close()
