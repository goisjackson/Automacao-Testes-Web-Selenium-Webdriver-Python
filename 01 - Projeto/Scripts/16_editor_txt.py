from time import sleep
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


driver = webdriver.Firefox()

driver.get('https://demo.automationtesting.in/CKEditor.html')
sleep(3)

# 01 - Editor texto
# iframe
try:
    ckeditor_frame = driver.find_element(By.CLASS_NAME, 'cke_wysiwyg_frame')
    driver.switch_to.frame(ckeditor_frame)
    print('Iframe OK')
except 'iframe':
    print('Iframe NOK')

# editor
try:
    ck_editor_body = driver.find_element(By.TAG_NAME, 'body')
    driver.execute_script("arguments[0].innerHTML = '<h1>Automation CKEditor</h1> <b>Analyst:</b> "
                          "<i>Jackson</i>'", ck_editor_body)
    print('Editor OK')
    # selecionar texto
    try:
        ck_editor_body.click()
        ck_editor_body.send_keys(Keys.CONTROL, 'a')
        print('Seleção OK')
    except 'selecionar':
        print('Seleção NOK')
except 'editor':
    print('Editor NOK')

# saindo do frame
try:
    sleep(2)
    driver.switch_to.default_content()
    driver.find_element(By.XPATH, '/html/body/section/div[1]/div/h4')
    print('Out iframe OK')
except 'iframe':
    print('Out iframe NOK')

# menu
try:
    # cut
    # driver.find_element(By.XPATH, '//*[@id="cke_11"]').click()
    driver.find_element(By.CSS_SELECTOR, '#cke_39').click()
    print('Menu OK')
except 'menu':
    print('Menu NOK')

# iframe
try:
    ckeditor_frame = driver.find_element(By.CLASS_NAME, 'cke_wysiwyg_frame')
    driver.switch_to.frame(ckeditor_frame)
    print('Iframe OK')
except 'iframe':
    print('Iframe NOK')

# editor
try:
    ck_editor_body = driver.find_element(By.TAG_NAME, 'body')
    ck_editor_body.click()
    print('Testes Completed')
    print('_' * 40)
    print('01 - Editor texto - Passed')
except 'editor':
    print('01 - Editor texto - Failed')

sleep(3)
driver.quit()
