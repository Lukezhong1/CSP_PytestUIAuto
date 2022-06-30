from PageObjects.basePage.basePage import BasePage
from util.parseConFile import ParseConFile


class MarketMgmtPage(BasePage):
    # 配置文件读取元素
    do_conf = ParseConFile('Market_Mgmt.conf')
    # 查询输入框
    marketList_marketName = do_conf.get_locators_or_account('MarketMgmtPageElements', 'marketList_marketName')
    # Query
    Query = do_conf.get_locators_or_account('MarketMgmtPageElements', 'Query')
    # 选择Market记录
    MarketListPl_MarketId = do_conf.get_locators_or_account('MarketMgmtPageElements', 'marketList_tab')
    # assignDb
    assignDbBtn = do_conf.get_locators_or_account('MarketMgmtPageElements', 'assignDbBtn')
    marketAssignedDbList_cb = do_conf.get_locators_or_account('MarketMgmtPageElements', 'marketAssignedDbList_cb')
    SubmitBtn = do_conf.get_locators_or_account('MarketMgmtPageElements', 'SubmitBtn')
    Submit_result = do_conf.get_locators_or_account('MarketMgmtPageElements', 'Submit_result')
    #assignFunc
    assignFuncBtn = do_conf.get_locators_or_account('MarketMgmtPageElements', 'assignFuncBtn')
    addBtn = do_conf.get_locators_or_account('MarketMgmtPageElements', 'addBtn')
    funcList_cb = do_conf.get_locators_or_account('MarketMgmtPageElements', 'funcList_cb')
    saveBtn = do_conf.get_locators_or_account('MarketMgmtPageElements', 'saveBtn')

    def market_assignDb(self):
        """市场分配DB"""
        self.click_MarketListPl_MarketId()
        self.click_assignDbBtn()
        self.click_marketAssignedDbList_cb()
        self.click_SubmitBtn()

    def market_assignFun(self):
        """市场分配Assign Report Func"""
        self.click_MarketListPl_MarketId()
        self.click_assignFuncBtn()
        self.click_addBtn()
        self.click_funcList_cb()
        self.click_saveBtn()

    def clear_marketList_marketName(self):
        return self.clear(*MarketMgmtPage.marketList_marketName)
    def input_MarketId(self, marketList_marketName):
        self.marketList_marketName()
        return self.send_keys(*MarketMgmtPage.marketList_marketName, marketList_marketName)

    def click_Query(self):
        return self.click(*MarketMgmtPage.Query)

    def click_MarketListPl_MarketId(self):
        return self.click(*MarketMgmtPage.MarketListPl_MarketId)

    def click_assignDbBtn(self):
        return self.click(*MarketMgmtPage.assignDbBtn)

    def click_marketAssignedDbList_cb(self):
        return self.click(*MarketMgmtPage.marketAssignedDbList_cb)

    def click_SubmitBtn(self):
        return self.click(*MarketMgmtPage.SubmitBtn)

    def click_assignFuncBtn(self):
        return self.click(*MarketMgmtPage.assignFuncBtn)

    def click_addBtn(self):
        return self.click(*MarketMgmtPage.addBtn)

    def click_funcList_cb(self):
        return self.click(*MarketMgmtPage.funcList_cb)

    def click_saveBtn(self):
        return self.click(*MarketMgmtPage.saveBtn)

    def get_Submit_result_text(self):
        return self.get_element_text(*MarketMgmtPage.Submit_result)

if __name__ == '__main__':
    pass
