from util.randomNumber import RandomNumber
from Database.testDataBase import TestDataBase

class RoleSetupData(object):
    """测试数据"""
    db = TestDataBase()
    add_role_setup_success = db.get_test_data_by_name("CSP", "role_setup_data", "add_role_setup_success_data")
    add_role_setup_fail = db.get_test_data_by_name("CSP", "role_setup_data", "add_role_setup_fail_data")

    # add_role_setup_success = [
    #     (
    #         RandomNumber().random_Id(),
    #         "Operate Successfully"
    #     )
    # ]
    #
    # add_role_setup_fail = [
    #     (
    #         "admin",
    #         "Role[admin] already exist!"
    #     )
    # ]

if __name__ == '__main__':
    pass
