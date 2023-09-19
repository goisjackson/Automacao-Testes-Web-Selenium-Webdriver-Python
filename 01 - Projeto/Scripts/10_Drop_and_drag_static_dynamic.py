from time import sleep
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


driver = webdriver.Firefox()

driver.get('http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html')

# 01 - drag and drop

source = driver.find_element(By.XPATH, '//*[@id="box5"]')
target = driver.find_element(By.XPATH, '//*[@id="box105"]')

action = ActionChains(driver)

action.drag_and_drop(source, target).perform()

sleep(2)
driver.get('https://jqueryui.com/draggable/')
sleep(3)

# 01 - drag and drop
driver.switch_to.frame(0)
source1 = driver.find_element(By.XPATH, '//*[@id="draggable"]')
action = ActionChains(driver)
action.drag_and_drop_by_offset(source1, 100, 100).perform()

driver.close()
