import pytest
from TestData.login_data import LoginData
from time import sleep

@pytest.mark.loginTest
class TestBase(object):
    """登录"""
    login_data = LoginData

    @pytest.mark.parametrize('username, password, expect', login_data.login_success_data)
    def test_login_success(self, open_url, username, password, expect):
        login_page = open_url
        login_page.login(username, password)
        actual = login_page.get_login_success_account()
        assert expect in actual, "登录成功, 断言失败"

    @pytest.mark.parametrize('username, password, expect', login_data.login_fail_data)
    def test_login_fail(self, open_url, username, password, expect):
        # 错误的用户名密码登录失败
        login_page = open_url
        login_page.login(username, password)
        sleep(2)
        actual = login_page.get_error_text()
        assert expect in actual


if __name__ == "__main__":
    pytest.main(['-v', 'baseCase.py'])
