from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Firefox()

driver.get('https://demo.automationtesting.in/Youtube.html')

# 01 - video
try:
    driver.switch_to.frame(0)
    sleep(2)
    # start
    driver.find_element(By.XPATH, '/html/body/div[1]/div/div[4]/button').click()
    sleep(7)
    # pause
    driver.find_element(By.XPATH, '//*[@id="movie_player"]').click()
    print('Youtube 01 - Passed')
except:
    print('Youtube 01 - Failed')

sleep(2)
driver.get('https://demo.automationtesting.in/Vimeo.html')

try:
    driver.switch_to.frame(0)
    sleep(2)
    # start
    driver.find_element(By.XPATH, '/html/body/div/div[7]/div[8]/div[1]/button').click()
    sleep(7)
    # pause
    driver.find_element(By.XPATH, '/html/body/div/div[7]/div[8]/div[1]/button').click()
    print('Vimeo 01 - Passed')
except:
    print('Vimeo 01 - Failed')


driver.quit()
