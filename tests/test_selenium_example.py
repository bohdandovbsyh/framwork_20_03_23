from selenium.webdriver.common.by import By

from utilities.config_reader import get_user_creds
from utilities.web_ui.base_page import BasePage


def test_login(open_login_page):
    login_page = open_login_page
    main_page = login_page.set_email(get_user_creds()[0]).set_password(get_user_creds()[1]).click_login_button()
    assert main_page.is_navigation_bar_displayed(), 'Nav bar is not displayed'
