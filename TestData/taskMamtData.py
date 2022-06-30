from Database.dataBaseSQL import DataBaseSQL
from Database.testDataBase import TestDataBase

class TaskMamtData(object):
    """测试数据"""
    # query_execute_task_success = [
    #     (
    #         "test",
    #         "Success"
    #     )
    # ]

    db = TestDataBase()
    query_execute_task_success = db.get_test_data_by_name("CSP", "task_mamt_data", "query_execute_task_success_data")
    # print('query_execute_task_success:',query_execute_task_success)

    add_query_execute_task_success = db.get_test_data_by_name("CSP", "task_mamt_data", "add_query_execute_task_success_data")
    print('update_all_report_func_setup_success:',add_query_execute_task_success)

    db=DataBaseSQL()
    add_query_execute_task_success=db.get_add_query_execute_task()
    # print(add_query_execute_task_success)


if __name__ == '__main__':
    pass
