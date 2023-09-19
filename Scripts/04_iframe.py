from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()

driver.get('https://demo.automationtesting.in/Frames.html')

# 01 - Single Frame
driver.switch_to.frame('singleframe')

sleep(3)
assert driver.find_element(By.XPATH, '/html/body/section/div/h5')

try:
    driver.find_element(By.XPATH, '/html/body/section/div/div/div/input').send_keys('Single frame')
    print('01 - Single Frame - Passed')
except:
    print('01 - Single Frame - Failed')

# 02 - Iframe with in an Iframe
driver.find_element(By.XPATH, '/html/body/section/div[1]/div/div/div/div[1]/div/ul/li[2]/a').click()

driver.switch_to.frame('MultipleFrames.html')





# driver.close()

