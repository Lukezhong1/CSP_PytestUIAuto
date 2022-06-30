from Database.testDataBase import TestDataBase

class DataSourceData(object):


    db = TestDataBase()
    search_market_and_datasource = db.get_test_data_by_name("CSP", "Datasource_Mgmt", "search_market_and_datasource_data")
    add_datasource_data = db.get_test_data_by_name("CSP", "Datasource_Mgmt", "add_datasource_data_data")


    # search_market_and_datasource =[("HAVI","","HAVI",""),("HAVI","41-3306","HAVI","41-3306"),("","41-3306","","41-3306"),("HAVI","","HAVI12","")]
    #
    # add_datasource_data = [
    #     (
    #         "soa_sea_3308",
    #         "jdbc:mysql://172.18.188.84:3308/soa_sea?characterEncoding=utf8&serverTimezone=GMT%2B8",
    #         "test",
    #         "6789test",
    #         "Operate Successfully"
    #     )
    # ]



