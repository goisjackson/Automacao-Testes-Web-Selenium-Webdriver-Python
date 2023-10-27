from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from PageObject.login_page import MyAccountPage

driver = webdriver.Firefox()

my_account_page = MyAccountPage(driver)
my_account_page.open()
my_account_page.login("jack02@jack02.com.br", "123!@#qweQWE")

driver.get('https://practice.automationtesting.in/shop/')

# add to basket
driver.find_element(By.CSS_SELECTOR, '.post-169 > a:nth-child(2)').click()

# View basket
li_element = driver.find_element(By.CSS_SELECTOR, '.post-169')
sleep(3)
view_basket_link = li_element.find_element(By.CSS_SELECTOR, '.added_to_cart')
view_basket_url = view_basket_link.get_attribute('href')
driver.get(view_basket_url)

if driver.find_element(By.CSS_SELECTOR, '.cart_totals > h2:nth-child(1)').text == 'Basket Totals':
    print('Add Basket - Passed')
else:
    print('Add Basket - Failed')

driver.quit()
