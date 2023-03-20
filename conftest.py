import pytest

from page_objects.login_page import LoginPage
from utilities.config_reader import get_application_url, get_browser_id, get_user_creds

from utilities.driver_factory import driver_factory


@pytest.fixture()
def create_browser():
    driver = driver_factory(get_browser_id())
    driver.maximize_window()
    driver.get(get_application_url())
    yield driver
    driver.quit()


@pytest.fixture()
def open_login_page(create_browser):
    return LoginPage(create_browser)


@pytest.fixture()
def open_dashboard_page(open_login_page):
    return open_login_page.login(get_user_creds()[0], get_user_creds()[1])
