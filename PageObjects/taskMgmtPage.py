from PageObjects.basePage.basePage import BasePage
from util.parseConFile import ParseConFile


class TaskMgmtPage(BasePage):
    # 配置文件读取元素
    do_conf = ParseConFile('TaskMgmtPage.conf')
    # taskListPl_taskId 查询输入框
    taskListPl_taskId = do_conf.get_locators_or_account('TaskMgmtPageElements', 'taskListPl_taskId')
    # Query
    Query = do_conf.get_locators_or_account('TaskMgmtPageElements', 'Query')
    # oid 选择task记录
    oid = do_conf.get_locators_or_account('TaskMgmtPageElements', 'oid')
    # Execute 执行task
    Execute = do_conf.get_locators_or_account('TaskMgmtPageElements', 'Execute')
    # hint 提示信息
    hint = do_conf.get_locators_or_account('TaskMgmtPageElements', 'hint')
    # Execute_Status 执行结果
    Execute_Status = do_conf.get_locators_or_account('TaskMgmtPageElements', 'Execute_Status')
    # add
    addBtn = do_conf.get_locators_or_account('TaskMgmtPageElements', 'addBtn')
    marketId = do_conf.get_locators_or_account('TaskMgmtPageElements', 'marketId')
    marketTree_1_check = do_conf.get_locators_or_account('TaskMgmtPageElements', 'marketTree_1_check')
    marketId_submit = do_conf.get_locators_or_account('TaskMgmtPageElements', 'marketId_submit')
    # Function ID
    Function_ID_click = do_conf.get_locators_or_account('TaskMgmtPageElements', 'Function_ID_click')
    Function_IDs = do_conf.get_locators_or_account('TaskMgmtPageElements', 'Function_IDs')
    Function_ID_head = do_conf.get_locators_or_account('TaskMgmtPageElements', 'Function_ID_head')
    Function_ID_end = do_conf.get_locators_or_account('TaskMgmtPageElements', 'Function_ID_end')
    Function_Detail = do_conf.get_locators_or_account('TaskMgmtPageElements', 'Function_Detail')
    Function_Detail_Select_All = do_conf.get_locators_or_account('TaskMgmtPageElements', 'Function_Detail_Select_All')
    taskId = do_conf.get_locators_or_account('TaskMgmtPageElements', 'taskId')
    saveBtn = do_conf.get_locators_or_account('TaskMgmtPageElements', 'saveBtn')

    def query_taskListPl_taskId(self, taskListPl_taskId):
        """查询taskListPl_taskId"""
        self.input_taskListPl_taskId(taskListPl_taskId)
        self.click_query_btn()

    def execute_task(self):
        """执行task"""
        self.click_oid_btn()
        self.click_execute_btn()

    def add_task(self,functionID,taskId):
        """add task"""
        self.click_addBtn()
        self.click_marketId()
        self.click_marketTree_1_check()
        self.click_marketId_submit()
        self.click_Function_ID_click()
        find_elements_Function_IDs=self.find_elements_Function_IDs()
        for i in range(1,len(find_elements_Function_IDs)):
            xpathi=self.Function_ID_head+str(i)+self.Function_ID_end
            xpathi_text=self.get_element_text('xpath',xpathi)
            if xpathi_text == functionID:
                self.click('xpath',xpathi)
                self.click_Function_Detail()
                self.click_Function_Detail_Select_All()
                self.input_taskId(taskId)
                self.click_saveBtn()
                self.sleep(5)
                return 0

    def clear_taskListPl_taskId(self):
        return self.clear(*TaskMgmtPage.taskListPl_taskId)
    def input_taskListPl_taskId(self, taskListPl_taskId):
        self.clear_taskListPl_taskId()
        return self.send_keys(*TaskMgmtPage.taskListPl_taskId, taskListPl_taskId)

    def click_query_btn(self):
        return self.click(*TaskMgmtPage.Query)

    def click_oid_btn(self):
        return self.click(*TaskMgmtPage.oid)

    def click_execute_btn(self):
        return self.click(*TaskMgmtPage.Execute)

    def get_hint_text(self):
        return self.get_element_text(*TaskMgmtPage.hint)

    def get_execute_status_text(self):
        return self.get_element_text(*TaskMgmtPage.Execute_Status)

    def click_addBtn(self):
        return self.click(*TaskMgmtPage.addBtn)
    def click_marketId(self):
        return self.click(*TaskMgmtPage.marketId)
    def click_marketTree_1_check(self):
        return self.click(*TaskMgmtPage.marketTree_1_check)
    def click_marketId_submit(self):
        return self.click(*TaskMgmtPage.marketId_submit)
    def click_Function_ID_click(self):
        return self.click(*TaskMgmtPage.Function_ID_click)
    def find_elements_Function_IDs(self):
        return self.find_elements(*TaskMgmtPage.Function_IDs)
    def click_Function_Detail(self):
        return self.click(*TaskMgmtPage.Function_Detail)
    def click_Function_Detail_Select_All(self):
        return self.click(*TaskMgmtPage.Function_Detail_Select_All)
    def clear_taskId(self):
        return self.clear(*TaskMgmtPage.taskId)
    def input_taskId(self, taskId):
        self.clear_taskId()
        return self.send_keys(*TaskMgmtPage.taskId, taskId)
    def click_saveBtn(self):
        return self.click(*TaskMgmtPage.saveBtn)

if __name__ == '__main__':
    pass
