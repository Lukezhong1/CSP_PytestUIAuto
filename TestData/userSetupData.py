from util.randomNumber import RandomNumber
from Database.testDataBase import TestDataBase

class UserSetupData(object):
    """测试数据"""

    db = TestDataBase()
    add_user_setup_success = db.get_test_data_by_name("CSP", "user_setup_data", "add_user_setup_success")

    add_user_setup_repeat = db.get_test_data_by_name("CSP", "user_setup_data", "add_user_setup_repeat_data")

    add_user_setup_fail = db.get_test_data_by_name("CSP", "user_setup_data", "add_user_setup_fail_data")

    # add_user_setup_success = [
    #     (
    #         RandomNumber().random_userid(),
    #         "UserName",
    #         RandomNumber().random_email(),
    #         "Operate Successfully"
    #     )
    # ]
    #
    # add_user_setup_repeat = [
    #     (
    #         "admin",
    #         "adminname",
    #         "admin@qq.com",
    #         "The user already exists."
    #     )
    # ]
    #
    # add_user_setup_fail = [
    #     (
    #         "",
    #         "luke.zhongname",
    #         "Luke.Zhong@qq.com",
    #         "* This field is required"
    #     ),
    #     (
    #         "123",
    #         "luke.zhongname",
    #         "Luke.Zhong@qq.com",
    #         "* Minimum 5 characters allowed"
    #     )
    # ]

if __name__ == '__main__':
    pass
    # success_data = UserSetupData.add_user_setup_success
    # print(success_data)
