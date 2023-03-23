import pytest

from page_objects.login_page_pack.login_page import LoginPage
from utilities.config_reader import get_application_url, get_browser_id, get_user_creds

from utilities.driver_factory import driver_factory

cokie = "CfDJ8BEIKWkx7BZOr2O7gS37lpeZkqv7KDFsZLECQ-yzNQaOeYtpM5oqoa6Ip47z2U9BACzH2ntzqlgQ_xcNnLnMrJkIjkmrCV4Rwe6e2lR7k" \
        "T4tp6mNMgG1wC4od2fMI5xkNx4V2IkjhZou2fyH4FcWxJd9_5Fyxxu00rT-aZL1OFLSAbtk2ICCSwlra5d9RvTLVylOUHRnkKoemR1CHzvFpRh" \
        "SIaQrw7TRV58ShVI-O-OQT6CAPrXskkxwf7vQMKsKktH1IyD4RhnhFD-FUxTJWqb8mAhuu85uWOIFTKJGGHo7VrbgxHIqqjceXd6oMKblrwCi" \
        "f8GgC_Q0Cg2Io5bLG5iBxOmkXXL5MH1G2fdzdnpQ5Fdvdu2ecfPhQcnHgpejodM25ro1AARZiMkaItqDD15UFZj02Y-mfoWkBlPyKeGw26aQrf" \
        "H1IxlLNyOAEXgYsA8lMn3NVkDOoORtWSXYpT58NX0lCRLIlnsbFhr40BzqDIiyjVlBlquuMOed259CmlhtFuDpE9ZE9KuRShYbGq1MsaDRrUX" \
        "wsQrE0c7PcSKS0d1N3l0U2OqxzEMkEY3Euw"


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
