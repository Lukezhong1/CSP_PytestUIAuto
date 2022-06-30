from Database.testDataBase import TestDataBase


class LoginData(object):
    """用户登录测试数据"""
    db = TestDataBase()
    login_success_data = db.get_test_data_by_name("CSP", "login_data", "login_success_data")

    login_fail_data = db.get_test_data_by_name("CSP", "login_data", "login_fail_data")

    login_fail_repeat_data = db.get_test_data_by_name("CSP", "login_data", "login_fail_repeat_data")

    # login_success_data = [
    #     (
    #         "admin",
    #         "admin1234",
    #         "Welcome, admin"
    #     )
    # ]
    #
    # login_fail_data = [
    #     (
    #         "luke.zhong",
    #         "wrong",
    #         "Wrong password"
    #     ),
    #     (
    #         "",
    #         "",
    #         "User ID is required!"
    #     ),
    #     (
    #         "admin",
    #         "",
    #         "Password is required!"
    #     ),
    #     (
    #         "fdsfdsfdf",
    #         "xiaochao11520",
    #         "User not found!"
    #     )
    # ]
    # login_fail_repeat_data = [
    #     (
    #         "luke.zhong",
    #         "wrong",
    #         "Password retry times over, user account locked!"
    #     )
    # ]


if __name__ == '__main__':
    pass
    # LoginData()
