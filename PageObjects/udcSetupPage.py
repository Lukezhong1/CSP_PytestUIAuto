from PageObjects.basePage.basePage import BasePage
from util.parseConFile import ParseConFile


class UDCSetupPage(BasePage):
    # 配置文件读取元素
    do_conf = ParseConFile('systemMgmtPage.conf')
    # udcGrouppl_udcGroup 查询输入框
    udcGrouppl_udcGroup = do_conf.get_locators_or_account('UDCSetupPageElements', 'udcGrouppl_udcGroup')
    # Query
    Query = do_conf.get_locators_or_account('UDCSetupPageElements', 'Query')
    # Query_result 查询结果
    Query_result = do_conf.get_locators_or_account('UDCSetupPageElements', 'Query_result')

    def query_udcGroup_setup(self, udcGroup):
        """查询UDCSetup"""
        self.input_udcGrouppl_udcGroup(udcGroup)
        self.click_Query_btn()

    def input_udcGrouppl_udcGroup(self, udcGrouppl_udcGroup):
        return self.send_keys(*UDCSetupPage.udcGrouppl_udcGroup, udcGrouppl_udcGroup)

    def click_Query_btn(self):
        return self.click(*UDCSetupPage.Query)

    def get_Query_result_text(self):
        return self.get_element_text(*UDCSetupPage.Query_result)


if __name__ == '__main__':
    pass
