from PageObjects.basePage.basePage import BasePage
from util.parseConFile import ParseConFile


class FunctionSetupPage(BasePage):
    # 配置文件读取元素
    do_conf = ParseConFile('systemMgmtPage.conf')
    # fwGetResListPl_defaultLabel FunctionSetup查询输入框
    fwGetResListPl_defaultLabel = do_conf.get_locators_or_account('FunctionSetupPageElements', 'fwGetResListPl_defaultLabel')
    # Query
    Query = do_conf.get_locators_or_account('FunctionSetupPageElements', 'Query')
    # Query_result 查询结果
    Query_result = do_conf.get_locators_or_account('FunctionSetupPageElements', 'Query_result')

    def query_function_setup(self, functionId):
        """查询FunctionSetup"""
        self.input_fwGetResListPl_defaultLabel(functionId)
        self.click_Query_btn()

    def input_fwGetResListPl_defaultLabel(self, fwGetResListPl_defaultLabel):
        return self.send_keys(*FunctionSetupPage.fwGetResListPl_defaultLabel, fwGetResListPl_defaultLabel)

    def click_Query_btn(self):
        return self.click(*FunctionSetupPage.Query)

    def get_Query_result_text(self):
        return self.get_element_text(*FunctionSetupPage.Query_result)


if __name__ == '__main__':
    pass
