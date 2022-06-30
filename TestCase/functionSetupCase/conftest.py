import pytest

from PageObjects.loginPageObject import LoginPageObject
from PageObjects.scalebarPageObject import ScalebarPage
from PageObjects.functionSetupPage import FunctionSetupPage
import Common.define as Define

# 从配置文件中获取正确的用户名和密码
username = Define.getDirConfig("LOGIN", "username")
password = Define.getDirConfig("LOGIN", "password")

@pytest.fixture(scope='class')
def ini_pages(driver):
    login_page = LoginPageObject(driver)
    scalebar_page = ScalebarPage(driver)
    functionsetup_page = FunctionSetupPage(driver)
    yield driver, login_page, scalebar_page,functionsetup_page

@pytest.fixture(scope='function')
def open_url(ini_pages):
    driver = ini_pages[0]
    login_page = ini_pages[1]
    login_page.open_url()
    yield login_page
    # driver.delete_all_cookies()

@pytest.fixture(scope='class')
def login(ini_pages):
    driver, login_page, scalebar_page,functionsetup_page = ini_pages
    login_page.open_url()
    login_page.login(username, password)
    yield login_page, scalebar_page,functionsetup_page
    # driver.delete_all_cookies()

@pytest.fixture(scope='function')
def refresh_page(ini_pages):
    driver = ini_pages[0]
    yield
    driver.refresh()
