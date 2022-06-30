from PageObjects.basePage.basePage import BasePage
from util.parseConFile import ParseConFile
from time import sleep


class UserSetupPage(BasePage):
    # 配置文件读取元素
    do_conf = ParseConFile('systemMgmtPage.conf')
    # 新建按钮
    add_user_setup_btn = do_conf.get_locators_or_account('UserSetupPageElements', 'Add')
    # userId输入框
    userId = do_conf.get_locators_or_account('UserSetupPageElements', 'userId')
    # userName输入框
    userName = do_conf.get_locators_or_account('UserSetupPageElements', 'userName')
    # email输入框
    email = do_conf.get_locators_or_account('UserSetupPageElements', 'email')
    # 提交按钮
    Submit = do_conf.get_locators_or_account('UserSetupPageElements', 'Submit')
    # 添加成功或失败的提示信息
    Submit_result = do_conf.get_locators_or_account('UserSetupPageElements', 'Submit_result')
    # userId输入框下的错误提示信息
    userFrom = do_conf.get_locators_or_account('UserSetupPageElements', 'userFrom')
    # fwGetUserListPl_userId userId查询输入框
    fwGetUserListPl_userId = do_conf.get_locators_or_account('UserSetupPageElements', 'fwGetUserListPl_userId')
    # Query
    Query = do_conf.get_locators_or_account('UserSetupPageElements', 'Query')
    # fwGetUserListPl_tab 查询userId结果
    fwGetUserListPl_tab = do_conf.get_locators_or_account('UserSetupPageElements', 'fwGetUserListPl_tab')

    def add_user_setup(self, userId, userName, email):
        """添加UserSetup"""
        self.click_add_user_setup_btn()
        self.input_userId(userId)
        self.input_userName(userName)
        self.input_email(email)
        sleep(1)
        self.click_Submit_btn()

    def query_user_setup(self, userId):
        """查询UserSetup"""
        self.input_fwGetUserListPl_userId(userId)
        self.click_Query_btn()

    def click_add_user_setup_btn(self):
        return self.click(*UserSetupPage.add_user_setup_btn)

    def input_userId(self, userId):
        return self.send_keys(*UserSetupPage.userId, userId)

    def input_userName(self, userName):
        return self.send_keys(*UserSetupPage.userName, userName)

    def input_email(self, email):
        return self.send_keys(*UserSetupPage.email, email)

    def input_fwGetUserListPl_userId(self, fwGetUserListPl_userId):
        return self.send_keys(*UserSetupPage.fwGetUserListPl_userId, fwGetUserListPl_userId)

    def click_Query_btn(self):
        return self.click(*UserSetupPage.Query)

    def click_Submit_btn(self):
        return self.click(*UserSetupPage.Submit)

    def get_Submit_result_text(self):
        return self.get_element_text(*UserSetupPage.Submit_result)

    def get_userFrom_text(self):
        return self.get_element_text(*UserSetupPage.userFrom)

    def get_fwGetUserListPl_tab_text(self):
        return self.get_element_text(*UserSetupPage.fwGetUserListPl_tab)


if __name__ == '__main__':
    pass
