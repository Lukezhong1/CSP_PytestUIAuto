from Database.testDataBase import TestDataBase

class UDCSetupData(object):
    """测试数据"""
    db = TestDataBase()
    query_udc_setup_success = db.get_test_data_by_name("CSP", "udcsetup_data", "udc_setup_query_data")

    # query_udc_setup_success = [
    #     (
    #         "custom",
    #         "custom"
    #     )
    # ]

if __name__ == '__main__':
    pass
