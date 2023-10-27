from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.common.by import By


class MyAccountPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    # Localizadores dos elementos da página
    username_input = (By.ID, 'username')
    password_input = (By.ID, 'password')
    login_button = (By.NAME, 'login')

    # Métodos para interagir com os elementos
    def open(self):
        self.driver.get('https://practice.automationtesting.in/my-account/')

    def enter_username(self, username):
        self.driver.find_element(*self.username_input).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(*self.password_input).send_keys(password)

    def click_login_button(self):
        self.driver.find_element(*self.login_button).click()

    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login_button()
