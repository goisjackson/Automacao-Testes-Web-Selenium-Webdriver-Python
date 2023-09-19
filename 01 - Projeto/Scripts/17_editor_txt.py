from time import sleep
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


driver = webdriver.Firefox()

driver.get('https://demo.automationtesting.in/SummerNote.html')
sleep(3)

# 01 - Editor Summer note
try:
    editor = driver.find_element(By.XPATH, '/html/body/section/div[1]/div/div/div[2]/div[3]/div[3]')
    editor.click()
    editor.send_keys(Keys.CONTROL, 'a')
    editor.send_keys('Summer Note')
    editor.send_keys(Keys.CONTROL, 'a')
    # formatação
    driver.find_element(By.XPATH, '/html/body/section/div[1]/div/div/div[2]/div[2]/div[2]/button[1]').click()
    driver.find_element(By.XPATH, '/html/body/section/div[1]/div/div/div[2]/div[2]/div[4]/div/button[1]').click()
    print('01 - Editor texto - Passed')
    editor.click()
except 'editor':
    print('01 - Editor texto - Failed')

driver.quit()
