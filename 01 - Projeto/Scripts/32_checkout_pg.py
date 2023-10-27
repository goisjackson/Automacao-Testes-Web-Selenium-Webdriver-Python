from time import sleep
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from PageObject.login_page import MyAccountPage

driver = webdriver.Firefox()

my_account_page = MyAccountPage(driver)
my_account_page.open()
my_account_page.login("jack02@jack02.com.br", "123!@#qweQWE")

driver.get('https://practice.automationtesting.in/basket/')

# click checkout
driver.find_element(By.CSS_SELECTOR, '.checkout-button').click()
sleep(3)

# checkout
# nome
driver.find_element(By.XPATH, '//*[@id="billing_first_name"]').send_keys('Jackson')

# sobrenome
driver.find_element(By.XPATH, '//*[@id="billing_last_name"]').send_keys('Smith')

# phone
driver.find_element(By.XPATH, '//*[@id="billing_phone"]').send_keys('1234567890')

# Address
driver.find_element(By.XPATH, '//*[@id="billing_address_1"]').send_keys('James')

# City
driver.find_element(By.XPATH, '//*[@id="billing_city"]').send_keys('New York')

# State
driver.find_element(By.XPATH, '//*[@id="billing_state"]').send_keys('NY')

# postcode
driver.find_element(By.XPATH, '//*[@id="billing_postcode"]').send_keys('0102030')

# pay
driver.find_element(By.XPATH, '//*[@id="payment_method_bacs"]').click()

# place order
driver.find_element(By.XPATH, '//*[@id="place_order"]').send_keys(Keys.ENTER)
sleep(3)

if driver.find_element(By.CSS_SELECTOR, '.woocommerce-thankyou-order-received').text == ('Thank you. Your order '
                                                                                         'has been received.'):
    print('Checkout - Passed')
else:
    print('Checkout - Failed')

driver.quit()
