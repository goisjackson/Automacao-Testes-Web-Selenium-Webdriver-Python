from time import sleep
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


driver = webdriver.Firefox()

driver.get('https://demo.automationtesting.in/CodeMirror.html')
sleep(3)

# 01 - Editor Code
try:
    editor = driver.find_element(By.XPATH, '/html/body/section/div[1]/div/div/div/div[1]/textarea')
    editor.send_keys('print("Teste 01")')
    editor.send_keys(Keys.ENTER)
    editor.send_keys('print("Editor OK")')
    print('01 - Editor Code - Passed')
except 'editor':
    print('01 - Editor Code - Failed')

driver.quit()
