import pytest
from TestData.reportFuncSetupData import ReportFuncSetupData

@pytest.mark.ReportFuncSetupTest
class TestReportFuncSetupCase(object):
    """ReportFunc_Setup"""

    add_success_data = ReportFuncSetupData.add_report_func_setup_success
    @pytest.mark.parametrize('functionId,functionName,exportFileName_tr1,exportFileName_tr2,exportFileName_tr3,exportFileName_tr4,seq,exportPath,'
                             'paramCount,mappingBtn_paramValue1,mappingBtn_paramValue2,mappingBtn_paramValue3,mappingBtn_paramValue4,expect', add_success_data)
    def test_add_ReportFunc_setup_success(self,login,functionId,functionName,exportFileName_tr1,exportFileName_tr2,exportFileName_tr3,exportFileName_tr4,seq,exportPath,
                                          paramCount,mappingBtn_paramValue1,mappingBtn_paramValue2,mappingBtn_paramValue3,mappingBtn_paramValue4,expect):
        """测试添加ReportFunc_Setup"""
        home_page = login[1]
        Report_FuncSetup_Page = login[2]
        home_page.select_menu(menu="Report_Func_Setup")
        Report_FuncSetup_Page.add_report_func_setup(functionId,functionName,exportFileName_tr1,exportFileName_tr2,exportFileName_tr3,exportFileName_tr4,seq,exportPath,
                                                    paramCount,mappingBtn_paramValue1,mappingBtn_paramValue2,mappingBtn_paramValue3,mappingBtn_paramValue4)
        # 断言提示信息
        actual = Report_FuncSetup_Page.get_Submit_result_text()
        assert expect in actual
        print("新增ReportFuncId成功: %s" % functionId)

    @pytest.mark.parametrize('functionFormList_functionId,exportPath,exportFileName_tr1,exportFileName_tr3,expect', ReportFuncSetupData.update_all_report_func_setup_success)
    def test_update_all_ReportFuncdetail_setup_success(self,login,functionFormList_functionId,exportPath,exportFileName_tr1,exportFileName_tr3,expect):
        """测试更新ReportFunc_Setup"""
        home_page = login[1]
        Report_FuncSetup_Page = login[2]
        home_page.select_menu(menu="Report_Func_Setup")
        Report_FuncSetup_Page.update_all_report_func_setup(functionFormList_functionId,exportPath,exportFileName_tr1,exportFileName_tr3)
        # 断言提示信息
        actual = Report_FuncSetup_Page.get_Submit_result_text()
        assert expect in actual
        print("更新ReportFuncId成功: %s" % functionFormList_functionId)

if __name__ == "__main__":
    pytest.main(['-v', 'testReportFuncSetupCase.py'])
