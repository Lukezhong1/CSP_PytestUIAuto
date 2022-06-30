import pytest
from TestData.udcSetupData import UDCSetupData

#@pytest.mark.FunctionsetupTest
class TestFunctionSetup(object):

    @pytest.mark.parametrize('udcGroup,expect', UDCSetupData.query_udc_setup_success)
    def test_query_udc_setup_success(self, login, udcGroup,expect):
        """测试查询UDC_Setup"""
        scalebar_page = login[1]
        udcsetup_page = login[2]
        scalebar_page.select_menu(menu="UDC_Setup")
        udcsetup_page.query_udcGroup_setup(udcGroup)
        actual = udcsetup_page.get_Query_result_text()
        assert expect in actual
        print("查询udcGroup成功: %s" % udcGroup)

if __name__ == "__main__":
    pytest.main(['-v', 'test_TaskMamtCase.py'])
