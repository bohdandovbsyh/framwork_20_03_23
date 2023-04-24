from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utilities.web_ui.base_page import BasePage


class DashboardPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    __nav_bar = (By.XPATH, "//*[@id='navbarText']")
    __start_accepting_orders_card = (By.XPATH, "//div[@id='configuration-steps-card']//h3")

    def is_navigation_bar_displayed(self):
         nav_bar_element = self.__wait.until(EC.visibility_of_element_located(self.__nav_bar))
         return nav_bar_element.is_displayed(self.__nav_bar)

    def get_start_accepting_orders_card_text(self):
        return self._get_text(self.__start_accepting_orders_card)
