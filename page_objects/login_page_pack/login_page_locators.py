from utilities.web_ui.locator import Locator
from selenium.webdriver.common.by import By


class LoginPageLocators:

    def __init__(self):
        self.__email_input = Locator(By.CSS_SELECTOR, '#Email')
        self.__password_input = Locator(By.XPATH, '//*[@id="Password"]')
        self.__login_button = Locator(By.XPATH, "//button[@type='submit']")

    @property
    def email_input(self):
        return self.__email_input.get_locator()

    @property
    def password_input(self):
        return self.__password_input.get_locator()

    @property
    def login_button(self):
        return self.__login_button.get_locator()
