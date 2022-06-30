from PageObjects.basePage.basePage import BasePage
from util.parseConFile import ParseConFile


class ScalebarPage(BasePage):
    # 配置文件读取元素
    do_conf = ParseConFile('scalebarPage.conf')
    # 首页
    scalebarpage = do_conf.get_locators_or_account('scalebarpageElements', 'homePage')
    # System_Mgmt
    System_Mgmt = do_conf.get_locators_or_account('scalebarpageElements', 'System_Mgmt')
    User_Setup = do_conf.get_locators_or_account('scalebarpageElements', 'User_Setup')
    Role_Setup = do_conf.get_locators_or_account('scalebarpageElements', 'Role_Setup')
    Function_Setup = do_conf.get_locators_or_account('scalebarpageElements', 'Function_Setup')
    UDC_Setup = do_conf.get_locators_or_account('scalebarpageElements', 'UDC_Setup')
    Market_Mgmt = do_conf.get_locators_or_account('scalebarpageElements', 'Market_Mgmt')

    # Configuration_Mgmt
    Configuration_Mgmt = do_conf.get_locators_or_account('scalebarpageElements', 'Configuration_Mgmt')
    Datasource_Mgmt = do_conf.get_locators_or_account('scalebarpageElements', 'Datasource_Mgmt')
    Json_Convert_Config = do_conf.get_locators_or_account('scalebarpageElements', 'Json_Convert_Config')

    # Report_Mgmt
    Report_Mgmt = do_conf.get_locators_or_account('scalebarpageElements', 'Report_Mgmt')
    Report_Basic_Setup = do_conf.get_locators_or_account('scalebarpageElements', 'Report_Basic_Setup')
    Report_Output_Setup = do_conf.get_locators_or_account('scalebarpageElements', 'Report_Output_Setup')
    Report_Func_Setup = do_conf.get_locators_or_account('scalebarpageElements', 'Report_Func_Setup')

    # Task_Mgmt
    Task_Mgmt = do_conf.get_locators_or_account('scalebarpageElements', 'Task_Mgmt')
    Task_Mgmt_list = do_conf.get_locators_or_account('scalebarpageElements', 'Task_Mgmt_list')

    def select_menu(self, menu='home'):
        if menu == "home":
            self.click_home_page_menu()
        elif menu == 'User_Setup':
            self.click_system_mgmt_menu()
            self.click_user_setup_menu()

        elif menu == 'Role_Setup':
            self.click_system_mgmt_menu()
            self.click_role_setup_menu()

        elif menu == 'Function_Setup':
            self.click_system_mgmt_menu()
            self.click_function_setup_menu()

        elif menu == 'UDC_Setup':
            self.click_system_mgmt_menu()
            self.click_UDC_Setup_menu()

        elif menu == 'Market_Mgmt':
            self.click_system_mgmt_menu()
            self.click_Market_Mgmt_menu()

        elif menu == 'Datasource_Mgmt':
            self.click_configuration_mgmt_menu()
            self.click_datasource_mgmt_menu()

        elif menu == 'Json_Convert_Config':
            self.click_configuration_mgmt_menu()
            self.click_json_convert_config_menu()

        elif menu == 'Report_Func_Setup':
            self.click_Report_Mgmt_menu()
            self.click_Report_Func_Setup_menu()

        elif menu == 'Task_Mgmt':
            self.click_task_mgmt_menu()
            self.click_task_mgmt_list_menu()

        else:
            raise ValueError(
                '''
                菜单选择错误!
                home->首页
                System_Mgmt->系统管理
                System_Mgmt->User_Setup
                '''
            )

    def click_home_page_menu(self):
        return self.click(*ScalebarPage.scalebarpage)

    def click_system_mgmt_menu(self):
        return self.click(*ScalebarPage.System_Mgmt)

    def click_user_setup_menu(self):
        return self.click(*ScalebarPage.User_Setup)

    def click_role_setup_menu(self):
        return self.click(*ScalebarPage.Role_Setup)

    def click_function_setup_menu(self):
        return self.click(*ScalebarPage.Function_Setup)

    def click_UDC_Setup_menu(self):
        return self.click(*ScalebarPage.UDC_Setup)

    def click_Market_Mgmt_menu(self):
        return self.click(*ScalebarPage.Market_Mgmt)

    def click_configuration_mgmt_menu(self):
        return self.click(*ScalebarPage.Configuration_Mgmt)

    def click_json_convert_config_menu(self):
        return self.click(*ScalebarPage.Json_Convert_Config)

    def click_datasource_mgmt_menu(self):
        return self.click(*ScalebarPage.Datasource_Mgmt)

    def click_Report_Mgmt_menu(self):
        return self.click(*ScalebarPage.Report_Mgmt)

    def click_Report_Func_Setup_menu(self):
        return self.click(*ScalebarPage.Report_Func_Setup)

    def click_task_mgmt_menu(self):
        return self.click(*ScalebarPage.Task_Mgmt)

    def click_task_mgmt_list_menu(self):
        return self.click(*ScalebarPage.Task_Mgmt_list)


if __name__ == '__main__':
    pass
