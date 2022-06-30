from PageObjects.basePage.basePage import BasePage
from util.parseConFile import ParseConFile
from time import sleep

class Report_FuncSetupPage(BasePage):
    # 配置文件读取元素
    do_conf = ParseConFile('Report_Mgmt.conf')
    # Report_Func_Setup head
    add_report_func_setup_btn = do_conf.get_locators_or_account('Report_Func_SetupPageElements', 'Add')
    editBtn = do_conf.get_locators_or_account('Report_Func_SetupPageElements', 'editBtn')
    upBtn = do_conf.get_locators_or_account('Report_Func_SetupPageElements', 'upBtn')
    # marketId 输入框
    marketId = do_conf.get_locators_or_account('Report_Func_SetupPageElements', 'marketId')
    marketTree_1 = do_conf.get_locators_or_account('Report_Func_SetupPageElements', 'marketTree_1')
    submit_marketId = do_conf.get_locators_or_account('Report_Func_SetupPageElements', 'submit_marketId')
    # functionId 输入框
    functionId = do_conf.get_locators_or_account('Report_Func_SetupPageElements', 'functionId')
    # functionName 输入框
    functionName = do_conf.get_locators_or_account('Report_Func_SetupPageElements', 'functionName')
    # isNeedZip 选择框,选择NO
    isNeedZip = do_conf.get_locators_or_account('Report_Func_SetupPageElements', 'isNeedZip')
    NoNeedZip = do_conf.get_locators_or_account('Report_Func_SetupPageElements', 'NoNeedZip')
    # 提交按钮
    saveBtn = do_conf.get_locators_or_account('Report_Func_SetupPageElements', 'saveBtn')
    # 添加head成功或失败的提示信息
    Submit_result = do_conf.get_locators_or_account('Report_Func_SetupPageElements', 'Submit_result')
    #Report_Func_Setup detail
    detail_add = do_conf.get_locators_or_account('Report_Func_SetupPageElements', 'detail_add')
    reportSetupOid = do_conf.get_locators_or_account('Report_Func_SetupPageElements', 'reportSetupOid')
    reportSetupOid1 = do_conf.get_locators_or_account('Report_Func_SetupPageElements', 'reportSetupOid1')
    outputSetupOid = do_conf.get_locators_or_account('Report_Func_SetupPageElements', 'outputSetupOid')
    outputSetupOid1 = do_conf.get_locators_or_account('Report_Func_SetupPageElements', 'outputSetupOid1')
    exportPath = do_conf.get_locators_or_account('Report_Func_SetupPageElements', 'exportPath')
    exportFileName = do_conf.get_locators_or_account('Report_Func_SetupPageElements', 'exportFileName')
    exportFileName_iframe = do_conf.get_locators_or_account('Report_Func_SetupPageElements', 'exportFileName_iframe')
    #3行exportFileName
    exportFileName_Param_Type1 = do_conf.get_locators_or_account('Report_Func_SetupPageElements', 'exportFileName_Param_Type1')
    exportFileName_Param_Type1_selectother = do_conf.get_locators_or_account('Report_Func_SetupPageElements', 'exportFileName_Param_Type1_selectother')
    exportFileName_tr1 = do_conf.get_locators_or_account('Report_Func_SetupPageElements', 'exportFileName_tr1')

    exportFileName_Param_Type2 = do_conf.get_locators_or_account('Report_Func_SetupPageElements', 'exportFileName_Param_Type2')
    exportFileName_Param_Type2_selectdate = do_conf.get_locators_or_account('Report_Func_SetupPageElements', 'exportFileName_Param_Type2_selectdate')
    exportFileName_Param_Type2_selectyyyyMMddHHmmss = do_conf.get_locators_or_account('Report_Func_SetupPageElements', 'exportFileName_Param_Type2_selectyyyyMMddHHmmss')
    exportFileName_tr2 = do_conf.get_locators_or_account('Report_Func_SetupPageElements', 'exportFileName_tr2')
    exportFileName_tr2_click = do_conf.get_locators_or_account('Report_Func_SetupPageElements', 'exportFileName_tr2_click')

    exportFileName_Param_Type3 = do_conf.get_locators_or_account('Report_Func_SetupPageElements', 'exportFileName_Param_Type3')
    exportFileName_Param_Type3_selectother = do_conf.get_locators_or_account('Report_Func_SetupPageElements', 'exportFileName_Param_Type3_selectother')
    exportFileName_tr3 = do_conf.get_locators_or_account('Report_Func_SetupPageElements', 'exportFileName_tr3')

    exportFileName_tr4 = do_conf.get_locators_or_account('Report_Func_SetupPageElements', 'exportFileName_tr4')
    exportFileName_saveBtn = do_conf.get_locators_or_account('Report_Func_SetupPageElements', 'exportFileName_saveBtn')
    seq = do_conf.get_locators_or_account('Report_Func_SetupPageElements', 'seq')
    dbOid = do_conf.get_locators_or_account('Report_Func_SetupPageElements', 'dbOid')
    dbOid1 = do_conf.get_locators_or_account('Report_Func_SetupPageElements', 'dbOid1')
    detail_saveBtn = do_conf.get_locators_or_account('Report_Func_SetupPageElements', 'detail_saveBtn')
    #Report_Func_Setup detail Param Mapping
    updateBtn = do_conf.get_locators_or_account('Report_Func_SetupPageElements', 'updateBtn')
    functionReportRefFormList = do_conf.get_locators_or_account('Report_Func_SetupPageElements', 'functionReportRefFormList')
    functionReportRefFormLists = do_conf.get_locators_or_account('Report_Func_SetupPageElements', 'functionReportRefFormLists')
    functionReportRefFormList_head = do_conf.get_locators_or_account('Report_Func_SetupPageElements', 'functionReportRefFormList_head')
    functionReportRefFormList_end = do_conf.get_locators_or_account('Report_Func_SetupPageElements', 'functionReportRefFormList_end')

    mappingBtn = do_conf.get_locators_or_account('Report_Func_SetupPageElements', 'mappingBtn')
    Param_Mapping_iframe = do_conf.get_locators_or_account('Report_Func_SetupPageElements', 'Param_Mapping_iframe')
    paramCount = do_conf.get_locators_or_account('Report_Func_SetupPageElements', 'paramCount')
    #点击空白处生效paramCount
    templateError = do_conf.get_locators_or_account('Report_Func_SetupPageElements', 'templateError')
    #第一、二行 Param_Type  Param_Value
    Param_Type1 = do_conf.get_locators_or_account('Report_Func_SetupPageElements', 'Param_Type1')
    Param_Type2 = do_conf.get_locators_or_account('Report_Func_SetupPageElements', 'Param_Type2')
    Param_Value1 = do_conf.get_locators_or_account('Report_Func_SetupPageElements', 'Param_Value1')
    Param_Value2 = do_conf.get_locators_or_account('Report_Func_SetupPageElements', 'Param_Value2')
    Select_All1 = do_conf.get_locators_or_account('Report_Func_SetupPageElements', 'Select_All1')
    Select_All2 = do_conf.get_locators_or_account('Report_Func_SetupPageElements', 'Select_All2')
    mappingBtn_paramValue1 = do_conf.get_locators_or_account('Report_Func_SetupPageElements', 'mappingBtn_paramValue1')
    mappingBtn_paramValue2 = do_conf.get_locators_or_account('Report_Func_SetupPageElements', 'mappingBtn_paramValue2')
    mappingBtn_paramValue3 = do_conf.get_locators_or_account('Report_Func_SetupPageElements', 'mappingBtn_paramValue3')
    mappingBtn_paramValue4 = do_conf.get_locators_or_account('Report_Func_SetupPageElements', 'mappingBtn_paramValue4')
    mappingBtn_saveBtn = do_conf.get_locators_or_account('Report_Func_SetupPageElements', 'mappingBtn_saveBtn')
    cancelBtn = do_conf.get_locators_or_account('Report_Func_SetupPageElements', 'cancelBtn')
    #query
    functionFormList_functionId = do_conf.get_locators_or_account('Report_Func_SetupPageElements', 'functionFormList_functionId')
    queryBtn = do_conf.get_locators_or_account('Report_Func_SetupPageElements', 'queryBtn')
    functionFormList = do_conf.get_locators_or_account('Report_Func_SetupPageElements', 'functionFormList')
    functionFormLists = do_conf.get_locators_or_account('Report_Func_SetupPageElements', 'functionFormLists')
    functionFormList_head = do_conf.get_locators_or_account('Report_Func_SetupPageElements', 'functionFormList_head')
    functionFormList_end = do_conf.get_locators_or_account('Report_Func_SetupPageElements', 'functionFormList_end')

    def add_report_func_setup(self,functionId,functionName,exportFileName_tr1,exportFileName_tr2,exportFileName_tr3,exportFileName_tr4,seq,exportPath,
                              paramCount,mappingBtn_paramValue1,mappingBtn_paramValue2,mappingBtn_paramValue3,mappingBtn_paramValue4):
        """添加report_funcSetup"""
        self.click_add_report_func_setup_btn()
        self.click_marketId_btn()
        self.click_marketTree_1_btn()
        self.click_submit_marketId_btn()
        self.input_functionId(functionId)
        self.input_funcName(functionName)
        self.click_isNeedZip()
        self.click_NoNeedZip()
        self.click_saveBtn()
        self.click_detail_add()
        self.click_reportSetupOid()
        self.click_reportSetupOid1()
        self.click_outputSetupOid()
        self.click_outputSetupOid1()
        self.input_exportPath(exportPath)
        self.click_exportFileName()
        self.switch_exportFileName_iframe()
        self.input_exportFileName_tr1(exportFileName_tr1)
        self.input_exportFileName_tr2(exportFileName_tr2)
        self.input_exportFileName_tr3(exportFileName_tr3)
        self.input_exportFileName_tr4(exportFileName_tr4)
        self.click_exportFileName_saveBtn()
        self.input_seq(seq)
        self.click_dbOid()
        self.click_dbOid1()
        self.click_detail_saveBtn()
        self.click_functionReportRefFormList()
        self.click_mappingBtn()
        self.switch_Param_Mapping_iframe()
        sleep(3)
        self.input_paramCount(paramCount)
        self.click_templateError()
        self.input_mappingBtn_paramValue1(mappingBtn_paramValue1)
        self.input_mappingBtn_paramValue2(mappingBtn_paramValue2)
        self.input_mappingBtn_paramValue3(mappingBtn_paramValue3)
        self.input_mappingBtn_paramValue4(mappingBtn_paramValue4)
        sleep(3)
        self.click_mappingBtn_saveBtn()
        self.click_upBtn()

    def update_all_report_func_setup(self,functionFormList_functionId,exportPath,exportFileName_tr1,exportFileName_tr3):
        """更新所有report_funcSetup"""
        self.input_functionFormList_functionId(functionFormList_functionId)
        self.click_queryBtn()
        # 循环找到对应的function
        functionFormLists=self.find_elements_functionFormLists()
        for i in range(1,len(functionFormLists)):
            xpathi=self.functionFormList_head+str(i+1)+self.functionFormList_end
            functionFormList_title=self.get_element_text('xpath',xpathi,'title')
            if functionFormList_functionId==functionFormList_title:
                self.click('xpath',xpathi)
                #更新detail
                self.cycle_function_report_detail(exportPath,exportFileName_tr1,exportFileName_tr3)

    def cycle_function_report_detail(self,exportPath,exportFileName_tr1,exportFileName_tr3):
        """更新所有 循环functionReport detail"""
        functionReportRefFormList=self.find_elements_functionReportRefFormLists()
        for seq in range(1,len(functionReportRefFormList)):
            xpathi=self.functionReportRefFormList_head+str(seq+1)+self.functionReportRefFormList_end
            # xpathi='//*[@id="functionReportRefFormList_tab"]/tbody/tr['+str(i+1)+']/td[1]/input'
            self.sleep(2)
            self.click('xpath',xpathi)
            self.click_updateBtn()
            self.input_exportPath(exportPath)
            self.click_exportFileName()
            self.switch_exportFileName_iframe()
            self.sleep(2)
            self.input_paramCount('3')
            self.sleep(2)
            self.click_templateError()
            self.click_exportFileName_Param_Type1()
            self.click_exportFileName_Param_Type1_selectother()
            self.input_exportFileName_tr1(exportFileName_tr1)
            self.click_exportFileName_Param_Type2()
            self.click_exportFileName_Param_Type2_selectdate()
            self.click_exportFileName_tr2_click()
            self.click_exportFileName_Param_Type2_selectyyyyMMddHHmmss()
            self.click_exportFileName_Param_Type3()
            self.click_exportFileName_Param_Type3_selectother()
            self.input_exportFileName_tr3(exportFileName_tr3)
            self.click_exportFileName_saveBtn()
            self.click_dbOid()
            self.click_dbOid1()
            self.click_detail_saveBtn()
            self.click_functionReportRefFormList()
            self.click_mappingBtn()
            self.switch_Param_Mapping_iframe()
            self.sleep(2)
            paramCount=self.get_paramCount_text('value')
            if int(paramCount)==1:
                if 'BA' in self.get_Param_Type1('title'):
                    self.click_Param_Value1()
                    self.click_Select_All1()
                    self.click_templateError()
            elif int(paramCount)>=2:
                if 'BA' in self.get_Param_Type1('title'):
                    self.click_Param_Value1()
                    self.click_Select_All1()
                    self.click_templateError()
                if 'BU' in self.get_Param_Type2('title'):
                    self.click_Param_Value2()
                    self.click_Select_All2()
                    self.click_templateError()
            else:
                pass
            self.sleep(2)
            self.click_mappingBtn_saveBtn()
            self.click_editBtn()
            self.sleep(2)
            self.click_editBtn()

    def click_add_report_func_setup_btn(self):
        return self.click(*Report_FuncSetupPage.add_report_func_setup_btn)

    def click_editBtn(self):
        return self.click(*Report_FuncSetupPage.editBtn)

    def click_upBtn(self):
        return self.click(*Report_FuncSetupPage.upBtn)

    def click_marketId_btn(self):
        return self.click(*Report_FuncSetupPage.marketId)

    def click_marketTree_1_btn(self):
        return self.click(*Report_FuncSetupPage.marketTree_1)

    def click_submit_marketId_btn(self):
        return self.click(*Report_FuncSetupPage.submit_marketId)

    def clear_functionId(self):
        return self.clear(*Report_FuncSetupPage.functionId)

    def input_functionId(self, functionId):
        self.clear_functionId()
        return self.send_keys(*Report_FuncSetupPage.functionId, functionId)

    def clear_functionName(self):
        return self.clear(*Report_FuncSetupPage.functionName)

    def input_funcName(self, functionName):
        self.clear_functionName()
        return self.send_keys(*Report_FuncSetupPage.functionName, functionName)

    def click_isNeedZip(self):
        return self.click(*Report_FuncSetupPage.isNeedZip)

    def click_NoNeedZip(self):
        return self.click(*Report_FuncSetupPage.NoNeedZip)

    def click_saveBtn(self):
        return self.click(*Report_FuncSetupPage.saveBtn)

    def get_Submit_result_text(self):
        return self.get_element_text(*Report_FuncSetupPage.Submit_result)

    def click_detail_add(self):
        return self.click(*Report_FuncSetupPage.detail_add)

    def click_reportSetupOid(self):
        return self.click(*Report_FuncSetupPage.reportSetupOid)

    def click_reportSetupOid1(self):
        return self.click(*Report_FuncSetupPage.reportSetupOid1)

    def click_outputSetupOid(self):
        return self.click(*Report_FuncSetupPage.outputSetupOid)

    def click_outputSetupOid1(self):
        return self.click(*Report_FuncSetupPage.outputSetupOid1)

    def clear_exportPath(self):
        return self.clear(*Report_FuncSetupPage.exportPath)

    def input_exportPath(self, exportPath):
        self.clear_exportPath()
        return self.send_keys(*Report_FuncSetupPage.exportPath, exportPath)

    def click_exportFileName(self):
        return self.click(*Report_FuncSetupPage.exportFileName)

    def switch_exportFileName_iframe(self):
        return self.switch_to_frame(*Report_FuncSetupPage.exportFileName_iframe)

    def click_exportFileName_Param_Type1(self):
        return self.click(*Report_FuncSetupPage.exportFileName_Param_Type1)
    def click_exportFileName_Param_Type1_selectother(self):
        return self.click(*Report_FuncSetupPage.exportFileName_Param_Type1_selectother)
    def click_exportFileName_Param_Type2(self):
        return self.click(*Report_FuncSetupPage.exportFileName_Param_Type2)
    def click_exportFileName_Param_Type2_selectdate(self):
        return self.click(*Report_FuncSetupPage.exportFileName_Param_Type2_selectdate)
    def click_exportFileName_tr2_click(self):
        return self.click(*Report_FuncSetupPage.exportFileName_tr2_click)
    def click_exportFileName_Param_Type2_selectyyyyMMddHHmmss(self):
        return self.click(*Report_FuncSetupPage.exportFileName_Param_Type2_selectyyyyMMddHHmmss)
    def click_exportFileName_Param_Type3(self):
        return self.click(*Report_FuncSetupPage.exportFileName_Param_Type3)
    def click_exportFileName_Param_Type3_selectother(self):
        return self.click(*Report_FuncSetupPage.exportFileName_Param_Type3_selectother)

    def clear_exportFileName_tr1(self):
        return self.clear(*Report_FuncSetupPage.exportFileName_tr1)

    def input_exportFileName_tr1(self, exportFileName_tr1):
        self.clear_exportFileName_tr1()
        return self.send_keys(*Report_FuncSetupPage.exportFileName_tr1, exportFileName_tr1)

    def clear_exportFileName_tr2(self):
        return self.clear(*Report_FuncSetupPage.exportFileName_tr2)

    def input_exportFileName_tr2(self, exportFileName_tr2):
        self.clear_exportFileName_tr2()
        return self.send_keys(*Report_FuncSetupPage.exportFileName_tr2, exportFileName_tr2)

    def clear_exportFileName_tr3(self):
            return self.clear(*Report_FuncSetupPage.exportFileName_tr3)

    def input_exportFileName_tr3(self, exportFileName_tr3):
        self.clear_exportFileName_tr3()
        return self.send_keys(*Report_FuncSetupPage.exportFileName_tr3, exportFileName_tr3)

    def clear_exportFileName_tr4(self):
            return self.clear(*Report_FuncSetupPage.exportFileName_tr4)

    def input_exportFileName_tr4(self, exportFileName_tr4):
        self.clear_exportFileName_tr4()
        return self.send_keys(*Report_FuncSetupPage.exportFileName_tr4, exportFileName_tr4)

    def click_exportFileName_saveBtn(self):
        return self.click(*Report_FuncSetupPage.exportFileName_saveBtn)

    def clear_seq(self):
        return self.clear(*Report_FuncSetupPage.seq)

    def input_seq(self, seq):
        self.clear_seq()
        return self.send_keys(*Report_FuncSetupPage.seq, seq)

    def click_dbOid(self):
        return self.click(*Report_FuncSetupPage.dbOid)

    def click_dbOid1(self):
        return self.click(*Report_FuncSetupPage.dbOid1)

    def click_detail_saveBtn(self):
        return self.click(*Report_FuncSetupPage.detail_saveBtn)

    def click_functionReportRefFormList(self):
        return self.click(*Report_FuncSetupPage.functionReportRefFormList)

    def find_elements_functionFormLists(self):
        return self.find_elements(*Report_FuncSetupPage.functionFormLists)

    def find_elements_functionReportRefFormLists(self):
        return self.find_elements(*Report_FuncSetupPage.functionReportRefFormLists)

    def clear_paramCount(self):
        return self.clear(*Report_FuncSetupPage.paramCount)

    def input_paramCount(self, paramCount):
        self.clear_paramCount()
        return self.send_keys(*Report_FuncSetupPage.paramCount, paramCount)

    def get_paramCount_text(self,name):
        return self.get_element_text(*Report_FuncSetupPage.paramCount,name)

    def click_mappingBtn(self):
        return self.click(*Report_FuncSetupPage.mappingBtn)

    def click_templateError(self):
        return self.click(*Report_FuncSetupPage.templateError)

    def get_Param_Type1(self,name):
        return self.get_element_text(*Report_FuncSetupPage.Param_Type1,name)

    def get_Param_Type2(self,name):
        return self.get_element_text(*Report_FuncSetupPage.Param_Type2,name)

    def click_Param_Value1(self):
        return self.click(*Report_FuncSetupPage.Param_Value1)

    def click_Param_Value2(self):
        return self.click(*Report_FuncSetupPage.Param_Value2)

    def click_Select_All1(self):
        return self.click(*Report_FuncSetupPage.Select_All1)

    def click_Select_All2(self):
        return self.click(*Report_FuncSetupPage.Select_All2)

    def switch_Param_Mapping_iframe(self):
        return self.switch_to_frame(*Report_FuncSetupPage.Param_Mapping_iframe)

    def clear_mappingBtn_paramValue1(self):
        return self.clear(*Report_FuncSetupPage.mappingBtn_paramValue1)

    def input_mappingBtn_paramValue1(self, mappingBtn_paramValue1):
        self.clear_mappingBtn_paramValue1()
        return self.send_keys(*Report_FuncSetupPage.mappingBtn_paramValue1, mappingBtn_paramValue1)

    def clear_mappingBtn_paramValue2(self):
        return self.clear(*Report_FuncSetupPage.mappingBtn_paramValue2)

    def input_mappingBtn_paramValue2(self, mappingBtn_paramValue2):
        self.clear_mappingBtn_paramValue2()
        return self.send_keys(*Report_FuncSetupPage.mappingBtn_paramValue2, mappingBtn_paramValue2)

    def clear_mappingBtn_paramValue3(self):
        return self.clear(*Report_FuncSetupPage.mappingBtn_paramValue3)

    def input_mappingBtn_paramValue3(self, mappingBtn_paramValue3):
        self.clear_mappingBtn_paramValue3()
        return self.send_keys(*Report_FuncSetupPage.mappingBtn_paramValue3, mappingBtn_paramValue3)

    def clear_mappingBtn_paramValue4(self):
        return self.clear(*Report_FuncSetupPage.mappingBtn_paramValue4)

    def input_mappingBtn_paramValue4(self, mappingBtn_paramValue4):
        self.clear_mappingBtn_paramValue4()
        return self.send_keys(*Report_FuncSetupPage.mappingBtn_paramValue4, mappingBtn_paramValue4)

    def click_mappingBtn_saveBtn(self):
        return self.click(*Report_FuncSetupPage.mappingBtn_saveBtn)

    def click_cancelBtn(self):
        return self.click(*Report_FuncSetupPage.cancelBtn)

    def clear_functionFormList_functionId(self):
        return self.clear(*Report_FuncSetupPage.functionFormList_functionId)

    def input_functionFormList_functionId(self, functionFormList_functionId):
        self.clear_functionFormList_functionId()
        return self.send_keys(*Report_FuncSetupPage.functionFormList_functionId, functionFormList_functionId)

    def click_queryBtn(self):
        return self.click(*Report_FuncSetupPage.queryBtn)

    def click_functionFormList(self):
        return self.click(*Report_FuncSetupPage.functionFormList)

    def click_updateBtn(self):
        return self.click(*Report_FuncSetupPage.updateBtn)

if __name__ == '__main__':
    pass