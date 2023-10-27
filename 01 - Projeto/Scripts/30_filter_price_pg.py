from time import sleep
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from PageObject.login_page import MyAccountPage
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Firefox()

my_account_page = MyAccountPage(driver)
my_account_page.open()
my_account_page.login("jack02@jack02.com.br", "123!@#qweQWE")

driver.get('https://practice.automationtesting.in/shop/')

try:
    # controle deslizante
    slider = driver.find_element(By.CSS_SELECTOR, 'span.ui-slider-handle:nth-child(3)')

    # ActionChains para interagir com o controle deslizante
    action = ActionChains(driver)

    # Movendo o controle deslizante para uma posição específica
    action.click_and_hold(slider).move_by_offset(-10, 0).release().perform()

    # Clicando em filtrar
    driver.find_element(By.CSS_SELECTOR, 'button.button').send_keys(Keys.ENTER)

    # Ordenar por
    driver.find_element(By.CSS_SELECTOR, '.orderby').click()
    sleep(3)
    driver.find_element(By.CSS_SELECTOR, '.orderby > option:nth-child(5)').click()

    # selecionar produto
    li_element = driver.find_element(By.CSS_SELECTOR, 'li.cat-item:nth-child(1)')
    categories_link = li_element.find_element(By.CSS_SELECTOR, 'li.cat-item:nth-child(1) > a:nth-child(1)')
    categories_url = categories_link.get_attribute('href')
    driver.get(categories_url)
    print('Filter - Passed')
except 'Filter':
    print('Filter - Failed')

driver.quit()
