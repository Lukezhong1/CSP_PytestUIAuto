from PageObjects.basePage.basePage import BasePage
from util.parseConFile import ParseConFile

class RoleSetupPage(BasePage):
    # 配置文件读取元素
    do_conf = ParseConFile('systemMgmtPage.conf')
    # 新建按钮
    add_role_setup_btn = do_conf.get_locators_or_account('RoleSetupPageElements', 'Add')
    # roleId输入框
    roleId = do_conf.get_locators_or_account('RoleSetupPageElements', 'roleId')
    # 提交按钮
    Submit = do_conf.get_locators_or_account('RoleSetupPageElements', 'Submit')
    # 添加新增成功的提示信息
    Submit_result = do_conf.get_locators_or_account('RoleSetupPageElements', 'Submit_result')
    # 添加新增失败的提示信息
    sys_error = do_conf.get_locators_or_account('RoleSetupPageElements', 'sys_error')

    def add_role_setup(self, roleId):
        """添加roleSetup"""
        self.click_add_role_setup_btn()
        self.input_roleId(roleId)
        self.click_Submit_btn()

    def click_add_role_setup_btn(self):
        return self.click(*RoleSetupPage.add_role_setup_btn)

    def input_roleId(self, roleId):
        return self.send_keys(*RoleSetupPage.roleId, roleId)

    def click_Submit_btn(self):
        return self.click(*RoleSetupPage.Submit)

    def get_Submit_result_text(self):
        return self.get_element_text(*RoleSetupPage.Submit_result)

    def get_sys_error_text(self):
        return self.get_element_text(*RoleSetupPage.sys_error)


if __name__ == '__main__':
    pass
