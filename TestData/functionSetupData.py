from Database.testDataBase import TestDataBase

class FunctionSetupData(object):
    """测试数据"""
    db = TestDataBase()
    query_function_setup_success = db.get_test_data_by_name("CSP", "function_setup_data", "query_function_setup_success_data")

    # query_function_setup_success = [
    #     (
    #         "System Mgmt",
    #         "System Mgmt"
    #     )
    # ]


if __name__ == '__main__':
    pass
