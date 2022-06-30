# from Database.dataBaseSQL import DataBaseSQL
# from util.randomNumber import RandomNumber
from Database.testDataBase import TestDataBase

class ReportFuncSetupData(object):
    """测试数据"""

    # add_report_func_setup_success = [
    #     (
    #         RandomNumber().random_Id(),"functionName","exportFileName_tr1","exportFileName_tr2","exportFileName_tr3",".csv","1","D:\Export_Import",
    #         "4","mappingBtn_paramValue1","mappingBtn_paramValue2","mappingBtn_paramValue3","mappingBtn_paramValue4",
    #         "Operate Successfully"
    #     )
    # ]

    db = TestDataBase()
    add_report_func_setup_success = db.get_test_data_by_name("CSP", "report_func_setup", "add_report_func_setup_data")

    update_all_report_func_setup_success = db.get_test_data_by_name("CSP", "report_func_setup", "update_all_report_func_setup_data")

    # db=DataBaseSQL()
    # update_all_report_func_setup_success=db.get_update_all_report_func_setup()

if __name__ == '__main__':
    pass
    # success_data = reportFuncSetupData.add_report_func_setup_success
    # print(success_data)
