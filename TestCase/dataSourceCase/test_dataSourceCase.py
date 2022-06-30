import pytest
from TestData.dataSourceData import DataSourceData


class TestDataSourceCase(object):
    dataSource = DataSourceData

    @pytest.mark.parametrize('DBName,JdbcURL,UserName,UserPwd,expect', dataSource.add_datasource_data)
    def test_add_data_source(self, login, DBName,JdbcURL,UserName,UserPwd, expect):
        """新增数据连接"""
        scale_page = login[1]
        data_source_page = login[2]
        scale_page.select_menu(menu="Datasource_Mgmt")
        data_source_page.add_datasource(DBName,JdbcURL,UserName,UserPwd)
        actual = data_source_page.get_Submit_result()
        assert expect in actual
        print("新增Datasource成功: %s" % DBName)

    @pytest.mark.parametrize('market_id,market_name,expected_Market_Id,expected_data_Source',
                             dataSource.search_market_and_datasource)
    def test_search_by_market_and_datasource_name(self, login, refresh_page, market_id, market_name,
                                                  expected_Market_Id,
                                                  expected_data_Source):
        """搜索市场和数据连接名称"""
        scale_page = login[1]
        data_source_page = login[2]
        scale_page.select_menu(menu="Datasource_Mgmt")
        data_source_page.query_by_Name_and_ID(market_name, market_id)
        actual_marker_id = data_source_page.get_marketID_text()
        actual_datasource_name = data_source_page.get_dataSource_text()

        assert expected_Market_Id in actual_marker_id, "匹配市场名称"
        assert expected_data_Source in actual_datasource_name, "匹配数据源名称"


if __name__ == "__main__":
    pytest.main(['-v', 'test_dataSourceCase.py'])
