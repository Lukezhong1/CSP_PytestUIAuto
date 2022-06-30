import pytest
from TestData.functionSetupData import FunctionSetupData

@pytest.mark.FunctionsetupTest
class TestFunctionSetup(object):

    @pytest.mark.parametrize('functionId,expect', FunctionSetupData.query_function_setup_success)
    def test_query_function_setup_success(self, login, functionId,expect):
        """测试查询function_Setup"""
        scalebar_page = login[1]
        functionsetup_page = login[2]
        scalebar_page.select_menu(menu="Function_Setup")
        functionsetup_page.query_function_setup(functionId)
        actual = functionsetup_page.get_Query_result_text()
        assert expect in actual
        print("查询functionId成功: %s" % functionId)

if __name__ == "__main__":
    pytest.main(['-v', 'test_FunctionSetupCase.py'])
