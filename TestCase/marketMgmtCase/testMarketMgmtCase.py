import pytest

@pytest.mark.MarketMgmtTest
class TestMarketMgmtCase(object):


    def test_market_assignDb_success(self,login):
        """测试market_assignDb"""
        home_page = login[1]
        MarketMgmt_Page = login[2]
        home_page.select_menu(menu="Market_Mgmt")
        MarketMgmt_Page.market_assignDb()
        # 断言提示信息
        actual = MarketMgmt_Page.get_Submit_result_text()
        assert 'Operate Successfully' in actual

    def test_market_assignFun_success(self,login):
        """测试market_assignFun"""
        home_page = login[1]
        MarketMgmt_Page = login[2]
        home_page.select_menu(menu="Market_Mgmt")
        MarketMgmt_Page.market_assignFun()
        # 断言提示信息
        actual = MarketMgmt_Page.get_Submit_result_text()
        assert 'Operate Successfully' in actual


if __name__ == "__main__":
    pytest.main(['-v', 'testMarketMgmtCase.py'])
