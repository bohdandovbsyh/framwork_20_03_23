from selenium.webdriver.common.by import By

from utilities.config_reader import get_user_creds
from utilities.web_ui.base_page import BasePage


def test_login():
    # login_page = open_login_page
    # main_page = login_page.set_email(get_user_creds()[0]).set_password(get_user_creds()[1]).click_login_button()
    # # assert main_page.is_navigation_bar_displayed(), 'Nav bar is not displayed'
    # actual_text = main_page.get_start_accepting_orders_card_text()
    is_visible = True
    assert is_visible is False, 'Element is visible'
    #
    # assert actual_text == "Start accepting orders", 'Text not as expected'


def test_cookies_storage(create_browser):
    driver = create_browser
    driver.execute_script("window.localStorage['auth_token2'] = Token_apI().generate")
    c = 0


def test_scroll(create_browser):
    driver = create_browser
    BasePage(driver).scroll_to_element((By.CSS_SELECTOR, '#Email'))
