from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


driver = webdriver.Firefox()

driver.get('https://demo.automationtesting.in/Resizable.html')

# 01 - resizable
try:
    resizable = driver.find_element(By.XPATH, '/html/body/section/div[1]/div/div/div/div/div[3]')
    action = ActionChains(driver)
    action.drag_and_drop_by_offset(resizable, 405, 205).perform()
    print('Resizable 01 - Passed')
except:
    print('Resizable 01 - Failed')

driver.quit()
