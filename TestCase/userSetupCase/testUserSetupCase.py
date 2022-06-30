import pytest
from TestData.userSetupData import UserSetupData

@pytest.mark.UserSetupTest
class TestUserSetup(object):

    """Add User_Setup"""
    success_data = UserSetupData.add_user_setup_success
    fail_data = UserSetupData.add_user_setup_fail
    repeat_data = UserSetupData.add_user_setup_repeat

    @pytest.mark.parametrize('userId, userName, email, expect', success_data)
    def test_add_user_setup_success(self, login, userId, userName, email, expect):
        """测试添加User_Setup"""
        home_page = login[1]
        user_setup_page = login[2]
        home_page.select_menu(menu="User_Setup")
        user_setup_page.add_user_setup(userId, userName, email)
        # 断言提示信息
        actual = user_setup_page.get_Submit_result_text()
        assert expect in actual
        print("新增userId成功: %s" % userId)
        return userId

    @pytest.mark.parametrize('userId, userName, email, expect', success_data)
    def test_query_user_setup_success(self, login, userId, userName, email, expect):
        userId=TestUserSetup().test_add_user_setup_success(login, userId, userName, email, expect)
        """查询新增的User_Setup"""
        user_setup_page = login[2]
        user_setup_page.query_user_setup(userId)
        actual = user_setup_page.get_fwGetUserListPl_tab_text()
        assert userId == actual

    @pytest.mark.parametrize('userId, userName, email, expect', repeat_data)
    def test_add_user_setup_repeat(self, login, userId, userName, email, expect):
        """测试添加User_Setup,userId重复，添加失败"""
        home_page = login[1]
        user_setup_page = login[2]
        home_page.select_menu(menu="User_Setup")
        user_setup_page.add_user_setup(userId, userName, email)
        actual = user_setup_page.get_Submit_result_text()
        assert expect in actual

    @pytest.mark.parametrize('userId, userName, email, expect', fail_data)
    def test_add_user_setup_fail(self, login, userId, userName, email, expect):
        """测试添加User_Setup-userId为空/添加User_Setup-userId少于5个字符，提交失败"""
        home_page = login[1]
        user_setup_page = login[2]
        home_page.select_menu(menu="User_Setup")
        user_setup_page.add_user_setup(userId, userName, email)
        actual = user_setup_page.get_userFrom_text()
        assert expect in actual


if __name__ == "__main__":
    pytest.main(['-v', 'testUserSetupCase.py'])
