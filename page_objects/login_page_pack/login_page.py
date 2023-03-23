from page_objects.login_page_pack.login_page_locators import LoginPageLocators
from page_objects.main_page import DashboardPage
from utilities.web_ui.base_page import BasePage


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.__page_locator = LoginPageLocators()

    def set_email(self, email: str):
        self._send_keys_js(locator=self.__page_locator.email_input, value=email)
        return self

    def set_password(self, password: str):
        self._send_keys(locator=self.__page_locator.password_input, value=password)
        return self

    def click_login_button(self):
        self._click_via_js(self.__page_locator.login_button)
        return DashboardPage(self.driver)

    def login(self, email, password):
        self.set_email(email).set_password(password).click_login_button()
        return DashboardPage(self.driver)

