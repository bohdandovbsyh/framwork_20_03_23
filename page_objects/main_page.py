from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class DashboardPage:
    def __init__(self, driver):
        self.driver = driver
        self.__wait = WebDriverWait(self.driver, 10, 1)

    __nav_bar = (By.XPATH, "//*[@id='navbarText']")

    def is_navigation_bar_displayed(self):
        nav_bar_element = self.__wait.until(EC.visibility_of_element_located(self.__nav_bar))
        return nav_bar_element.is_displayed()
