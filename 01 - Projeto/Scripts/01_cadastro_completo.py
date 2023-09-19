from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.webdriver import WebDriver

# 01 - Cadastro Completo
email = 'teste@test.com'

driver: WebDriver = webdriver.Firefox()

driver.get('https://demo.automationtesting.in/Index.html')

# informar email
driver.find_element(By.XPATH, '//*[@id="email"]').send_keys(email)

# aceite email
driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/span/a').click()
sleep(3)

assert driver.find_element(By.XPATH, '/html/body/section/div/h2')
print('Email Aceito', email)

# Nome
driver.find_element(By.XPATH, '/html/body/section/div/div/div[2]/form/div[1]/div[1]/input').send_keys('Jackson')

# Sobrenome
driver.find_element(By.XPATH, '/html/body/section/div/div/div[2]/form/div[1]/div[2]/input').send_keys('Gois')

# endereço
driver.find_element(By.XPATH, '/html/body/section/div/div/div[2]/form/div[2]/div/'
                              'textarea').send_keys('Barueri - SP')

# email
driver.find_element(By.XPATH, '/html/body/section/div/div/div[2]/form/div[3]/div[1]/'
                              'input').send_keys('teste@test.com')

# telefone
driver.find_element(By.XPATH, '/html/body/section/div/div/div[2]/form/div[4]/div/'
                              'input').send_keys('1234567891')

# Gênero
driver.find_element(By.XPATH, '/html/body/section/div/div/div[2]/form/div[5]/div/label[1]/input').click()

# Hobbies
driver.find_element(By.XPATH, '//*[@id="checkbox2"]').click()
sleep(2)

# idioma
try:
    driver.find_element(By.XPATH, '//*[@id="msdd"]').click()
    sleep(3)
    driver.find_element(By.CSS_SELECTOR, 'li.ng-scope:nth-child(29)').click()
except:
    print('Linguagem Não Selecionada')

# Skills
driver.find_element(By.XPATH, '//*[@id="Skills"]').send_keys('Python')

# País
try:
    driver.find_element(By.XPATH, '//*[@id="countries"]').click()
except:
    print('País Não Selecionado')

# Selecionar País
sleep(2)
driver.find_element(By.XPATH, '/html/body/section/div/div/div[2]/form/div[10]/div/span').click()
sleep(2)
driver.find_element(By.XPATH, '/html/body/span/span/span[1]/input').send_keys('Japan')

# Date Of Birth
driver.find_element(By.XPATH, '//*[@id="yearbox"]').send_keys('1989')
driver.find_element(By.CSS_SELECTOR, 'div.col-md-3:nth-child(3) > select:nth-child(1)').send_keys('July')
driver.find_element(By.XPATH, '//*[@id="daybox"]').send_keys('3')

# senha
driver.find_element(By.XPATH,'//*[@id="firstpassword"]').send_keys('123456')
driver.find_element(By.XPATH,'//*[@id="secondpassword"]').send_keys('123456')

# subir foto
driver.find_element(By.ID, 'imagesrc').send_keys(r"C:\Users\jacks\Desktop\mib.jpg")

# submit
driver.find_element(By.XPATH, '//*[@id="submitbtn"]').click()

# driver.close()
