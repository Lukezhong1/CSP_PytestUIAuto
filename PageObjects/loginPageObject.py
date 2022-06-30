from PageObjects.basePage.basePage import BasePage
from util.parseConFile import ParseConFile
import Common.define as Define
# 从selenium里面导入webdriver
from selenium import webdriver


class LoginPageObject(BasePage):
    # 配置文件读取元素
    do_conf = ParseConFile('loginPage.conf')
    # 用户名输入框
    username = do_conf.get_locators_or_account('LoginPageElements', 'username')
    # 密码输入框
    password = do_conf.get_locators_or_account('LoginPageElements', 'password')
    # 登录按钮
    loginBtn = do_conf.get_locators_or_account('LoginPageElements', 'loginBtn')
    # 登录失败的提示信息
    error_head = do_conf.get_locators_or_account('LoginPageElements', 'loginError')
    # forgotPwd
    forgotPwd = do_conf.get_locators_or_account('LoginPageElements', 'forgotPwd')
    # 配置文件读取元素
    do_conf_scalebarPage = ParseConFile('scalebarPage.conf')
    # 登录成功后的用户显示元素
    welcome_message = do_conf_scalebarPage.get_locators_or_account('scalebarpageElements', 'welcome_message')
    homePage = do_conf_scalebarPage.get_locators_or_account('scalebarpageElements', 'homePage')

    def login(self, username, password):
        """登录流程"""
        self.open_url()
        self.input_username(username)
        self.input_password(password)
        self.click_login_btn()

    def open_url(self):
        url =  '/csp/app/login?lang=en_US'
        # url = self.base_url + '/csp/app/login'
        return self.load_url(url)

    def clear_username(self):
        return self.clear(*LoginPageObject.username)

    def input_username(self, username):
        self.clear_username()
        return self.send_keys(*LoginPageObject.username, username)

    def clear_password(self):
        return self.clear(*LoginPageObject.password)

    def input_password(self, password):
        self.clear_password()
        return self.send_keys(*LoginPageObject.password, password)

    def click_login_btn(self):
        return self.click(*LoginPageObject.loginBtn)

    def click_forgotPwd_btn(self):
        return self.click(*LoginPageObject.forgotPwd)

    def switch_default_frame(self):
        return self.switch_to_default_frame()

    def get_error_text(self):
        return self.get_element_text(*LoginPageObject.error_head)

    def get_login_success_text(self,name):
        return self.get_element_text(*LoginPageObject.welcome_message,name)

    def get_loginBtn_text(self):
        return self.get_element_text(*LoginPageObject.loginBtn)

    def get_homePage_text(self):
        return self.get_element_text(*LoginPageObject.homePage)


if __name__ == '__main__':
    pass
    # driver_path = Define.getDirConfig("PATH", "DRIVER_PATH")
    # driver = webdriver.Chrome(driver_path)
    # driver.maximize_window()
    # login_test = LoginPageObject(driver)
    # login_test.login('admin', 'admin1234')
    # assert login_test.get_login_success_text() in "Welcome, admin"
