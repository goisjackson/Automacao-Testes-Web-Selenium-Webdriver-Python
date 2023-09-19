from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
import os

driver = webdriver.Firefox()

driver.get('https://demo.automationtesting.in/FileDownload.html')
sleep(3)

# 01 - File Download
# Teste Generate File txt
try:
    driver.find_element(By.XPATH, '//*[@id="textbox"]').send_keys('Teste Generate File txt')
    driver.find_element(By.XPATH, '//*[@id="createTxt"]').click()
    sleep(2)
    driver.find_element(By.XPATH, '//*[@id="link-to-download"]').click()
    print('Teste Generate File txt - OK')
except 'Teste Generate File txt':
    print('Teste Generate File txt - NOK')

# Teste Generate File pdf
try:
    driver.find_element(By.XPATH, '//*[@id="pdfbox"]').send_keys('Teste Generate File pdf')
    driver.find_element(By.XPATH, '//*[@id="createPdf"]').click()
    sleep(2)
    driver.find_element(By.XPATH, '//*[@id="pdf-link-to-download"]').click()
    print('Teste Generate File pdf - OK')
except 'Teste Generate File pdf':
    print('Teste Generate File pdf - NOK')

# File down another tab
try:
    driver.get('https://raw.githubusercontent.com/KrishnaSakinala/AutomationTesting/master/samplefile.pdf')
    url = 'https://raw.githubusercontent.com/KrishnaSakinala/AutomationTesting/master/samplefile.pdf'
    download_dir = r'C:\Users\jacks\Downloads'
    response = requests.get(url)
    if response.status_code == 200:
        file_path = os.path.join(download_dir, os.path.basename(url))
        with open(file_path, 'wb') as f:
            f.write(response.content)
            print('File down another tab - OK')
            print(' ' * 40)
            print('01 - File Download - Passed')
except 'File down another tab':
    print('File down another tab - NOK')
    print(' ' * 40)
    print('01 - File Download - Failed')

driver.quit()
