import pytest
from TestData.login_data import LoginData
from time import sleep

#@pytest.mark.loginTest
class TestLogin(object):
    """登录"""
    login_data = LoginData

    @pytest.mark.parametrize('username, password, expect', login_data.login_success_data)
    def test_login_success(self, open_url, username, password, expect):
        login_page = open_url
        login_page.login(username, password)
        actual = login_page.get_login_success_text('innerText')
        assert expect in actual, "登录成功, 断言失败"

    @pytest.mark.parametrize('username, password, expect', login_data.login_fail_data)
    def test_login_fail(self, open_url, username, password, expect):
        # 错误的用户名密码登录失败
        login_page = open_url
        login_page.login(username, password)
        sleep(2)
        actual = login_page.get_error_text()
        assert expect in actual

    @pytest.mark.parametrize('username, password, expect', login_data.login_fail_repeat_data)
    def test_login_repeat(self, open_url, username, password, expect):
        # 密码输入错误次数大于5次，登录失败，锁定用户
        login_page = open_url
        login_page.login(username, password)
        for i in range(1,6):
            sleep(2)
            login_page.click_login_btn()
        actual = login_page.get_error_text()
        assert expect in actual


if __name__ == "__main__":
    pytest.main(['-v', 'testLginCase.py'])
