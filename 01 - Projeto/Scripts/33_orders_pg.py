from time import sleep
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from PageObject.login_page import MyAccountPage

driver = webdriver.Firefox()

my_account_page = MyAccountPage(driver)
my_account_page.open()
my_account_page.login("jack02@jack02.com.br", "123!@#qweQWE")

# Orders
driver.find_element(By.CSS_SELECTOR, 'li.woocommerce-MyAccount-navigation-link:nth-child(2) '
                                     '> a:nth-child(1)').click()
sleep(3)

# View Order
if driver.find_element(By.CSS_SELECTOR, 'tr.order:nth-child(3) > td:nth-child(5) > a:nth-child(1)'):
    print('Ordem Gerada')
    numb_order = driver.find_element(By.CSS_SELECTOR, 'tr.order:nth-child(3) > td:nth-child(1) > a:nth-child(1)').text
    print('Numero da ordem = ', numb_order)
    sleep(3)
    driver.find_element(By.CSS_SELECTOR, 'tr.order:nth-child(3) > td:nth-child(5) > a:nth-child(1)').click()
else:
    print('Ordem Não gerada')
sleep(3)

if driver.find_element(By.CSS_SELECTOR, '.woocommerce-MyAccount-content > '
                                        'h2:nth-child(2)').text == 'Order Details':
    print('Orders - Passed')
else:
    print('Orders - Failed')

# logout
driver.find_element(By.CSS_SELECTOR, 'li.woocommerce-MyAccount-navigation-link:nth-child(6) > '
                                     'a:nth-child(1)').send_keys(Keys.ENTER)
sleep(3)

driver.quit()
