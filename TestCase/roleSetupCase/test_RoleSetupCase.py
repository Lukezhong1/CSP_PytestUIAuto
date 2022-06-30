import pytest
from TestData.roleSetupData import RoleSetupData

@pytest.mark.RolesetupTest
class TestRoleSetup(object):
    """Role_Setup"""
    Role_Setup_data = RoleSetupData
    success_data = RoleSetupData.add_role_setup_success
    fail_data = RoleSetupData.add_role_setup_fail

    @pytest.mark.parametrize('roleId, expect', success_data)
    def test_add_role_setup_success(self, login, roleId, expect):
        """测试添加Role_Setup"""
        scalebar_page = login[1]
        role_setup_page = login[2]
        scalebar_page.select_menu(menu="Role_Setup")
        role_setup_page.add_role_setup(roleId)
        actual_Submit_result = role_setup_page.get_Submit_result_text()
        assert expect in actual_Submit_result
        print("新增roleId成功: %s" % roleId)

    @pytest.mark.parametrize('roleId, expect', fail_data)
    def test_add_role_setup_fail(self, login, roleId, expect):
        """测试添加Role_Setup"""
        home_page = login[1]
        role_setup_page = login[2]
        home_page.select_menu(menu="Role_Setup")
        role_setup_page.add_role_setup(roleId)
        actual = role_setup_page.get_sys_error_text()
        assert expect in actual


if __name__ == "__main__":
    pytest.main(['-v', 'test_RoleSetupCase.py'])
