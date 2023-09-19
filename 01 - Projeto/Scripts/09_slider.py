from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()

driver.get('https://demo.automationtesting.in/Slider.html')

# 01 - Slider
driver.find_element(By.XPATH, '/html/body/section/div[1]/div/div/div/a').click()
sleep(3)

try:
    for i in range(10):
        driver.find_element(By.XPATH, '/html/body/section/div[1]/div/div/div/a').send_keys(Keys.ARROW_UP)
    print('Slider 01 - Passed')
except:
    print('Slider 01 - Failed')

driver.quit()
