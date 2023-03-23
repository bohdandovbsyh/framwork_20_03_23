from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.__wait = WebDriverWait(self.driver, 2, 1)

    def _wait_until_element_located(self, locator):
        return self.__wait.until(EC.visibility_of_element_located(locator))

    def _wait_until_to_be_clickable(self, locator):
        return self.__wait.until(EC.element_to_be_clickable(locator))

    def _send_keys(self, locator, value, is_clear=True):
        element = self._wait_until_element_located(locator)
        if is_clear:
            element.clear()
        element.send_keys(value)

    def _click(self, locator):
        self._wait_until_to_be_clickable(locator).click()

    def _click_via_js(self, locator):
        self.driver.execute_script('arguments[0].click()', self._wait_until_to_be_clickable(locator))

    def _send_keys_js(self, locator, value):
        self.driver.execute_script(f"arguments[0].setAttribute('value', '{value}')",
                                   self._wait_until_element_located(locator))

    def _get_text(self, locator):
        element = self._wait_until_element_located(locator)
        return element.text

    def vertical_scroll_page(self, y: int):
        self.driver.execute_script(f'window.scrollBy(0,{y})')

    def scroll_to_element(self, locator):
        max_retries = 10
        _try = 0
        while _try != max_retries:
            try:
                element = self._wait_until_element_located(locator)
                return element
            except Exception:
                self.vertical_scroll_page(100)
                _try += 1
        raise NoSuchElementException(str(locator))

    def _is_element_visible(self, locator):
        element = self._wait_until_element_located(locator)
        return element.is_visible()

    def _is_displayed(self):
        try:
            self._wait_until_element_located(1)
            return True
        except:
            return False
