from PageObjects.basePage.basePage import BasePage
from util.parseConFile import ParseConFile
import Common.define as Define
# 从selenium里面导入webdriver
from selenium import webdriver


class DataSourceMgmtPage(BasePage):
    # 配置文件读取元素
    do_conf = ParseConFile('configPage.conf')
    # 主界面元素
    # 市场ID
    MarketIDInput = do_conf.get_locators_or_account('DataSourceMgmtPage', 'MarketIDInput')
    # 市场 name
    MarketNameInput = do_conf.get_locators_or_account('DataSourceMgmtPage', 'MarketNameInput')
    # 查询按钮
    QueryButton = do_conf.get_locators_or_account('DataSourceMgmtPage', 'QueryButton')
    # 重置按钮
    ResetButton = do_conf.get_locators_or_account('DataSourceMgmtPage', 'ResetButton')
    # 新增按钮
    AddButton = do_conf.get_locators_or_account('DataSourceMgmtPage', 'AddButton')
    # 增加详情页面的元素
    DBName = do_conf.get_locators_or_account('DataSourceMgmtAddPage', 'DBName')
    DBFlag = do_conf.get_locators_or_account('DataSourceMgmtAddPage', 'DBFlag')
    ActiveStatus = do_conf.get_locators_or_account('DataSourceMgmtAddPage', 'ActiveStatus')
    JdbcURL = do_conf.get_locators_or_account('DataSourceMgmtAddPage', 'JdbcURL')
    UserName = do_conf.get_locators_or_account('DataSourceMgmtAddPage', 'UserName')
    UserPwd = do_conf.get_locators_or_account('DataSourceMgmtAddPage', 'UserPwd')
    DSSlave = do_conf.get_locators_or_account('DataSourceMgmtAddPage', 'DSSlave')
    Add_Button = do_conf.get_locators_or_account('DataSourceMgmtAddPage', 'Add_Button')
    Query_BABU = do_conf.get_locators_or_account('DataSourceMgmtAddPage', 'Query_BABU')
    babuList_all = do_conf.get_locators_or_account('DataSourceMgmtAddPage', 'babuList_all')
    saveBtn = do_conf.get_locators_or_account('DataSourceMgmtAddPage', 'saveBtn')
    Submit_result = do_conf.get_locators_or_account('DataSourceMgmtAddPage', 'Submit_result')
    # 更新按钮
    UpdateButton = do_conf.get_locators_or_account('DataSourceMgmtPage', 'UpdateButton')
    # 激活按钮
    ActiveButton = do_conf.get_locators_or_account('DataSourceMgmtPage', 'ActiveButton')
    # 选择数据按钮
    SelectButton = do_conf.get_locators_or_account('DataSourceMgmtPage', 'SelectButton')
    # 市场ID
    MarketIDLabel = do_conf.get_locators_or_account('DataSourceMgmtPage', 'MarketIDLabel')
    # 数据源名称
    DataSourceLabel = do_conf.get_locators_or_account('DataSourceMgmtPage', 'DataSourceLabel')

    def query_by_Name_and_ID(self, MarketName , MarketID):
        self.input_market_ID(MarketID)
        self.input_market_Name(MarketName)
        self.click_query_btn()

    def add_datasource(self,DBName,JdbcURL,UserName,UserPwd):
        self.click_Add_btn()
        self.input_DBName(DBName)
        self.input_JdbcURL(JdbcURL)
        self.input_UserName(UserName)
        self.input_UserPwd(UserPwd)
        self.click_Query_BABU()
        self.click_babuList_all()
        self.click_saveBtn()

    def clear_Market_ID(self):
        return self.clear(*DataSourceMgmtPage.MarketIDInput)

    def clear_Market_Name(self):
        return self.clear(*DataSourceMgmtPage.MarketNameInput)

    def input_market_ID(self, MarketID):
        self.clear_Market_ID()
        return self.send_keys(*DataSourceMgmtPage.MarketIDInput, MarketID)

    def input_market_Name(self, MarketName):
        self.clear_Market_Name()
        return self.send_keys(*DataSourceMgmtPage.MarketNameInput, MarketName)

    def click_query_btn(self):
        return self.click(*DataSourceMgmtPage.QueryButton)

    def click_reset_btn(self):
        return self.click(*DataSourceMgmtPage.ResetButton)

    def click_Add_btn(self):
        return self.click(*DataSourceMgmtPage.AddButton)

    def click_update_btn(self):
        return self.click(*DataSourceMgmtPage.UpdateButton)

    def click_active_btn(self):
        return self.click(*DataSourceMgmtPage.ActiveButton)

    def click_select_btn(self):
        return self.click(*DataSourceMgmtPage.SelectButton)

    def get_marketID_text(self):
        return self.get_element_text(*DataSourceMgmtPage.MarketIDLabel)

    def get_dataSource_text(self):
        return self.get_element_text(*DataSourceMgmtPage.DataSourceLabel)

    def clear_DBName(self):
        return self.clear(*DataSourceMgmtPage.DBName)
    def input_DBName(self, DBName):
        self.clear_DBName()
        return self.send_keys(*DataSourceMgmtPage.DBName, DBName)

    def clear_JdbcURL(self):
        return self.clear(*DataSourceMgmtPage.JdbcURL)
    def input_JdbcURL(self, JdbcURL):
        self.clear_JdbcURL()
        return self.send_keys(*DataSourceMgmtPage.JdbcURL, JdbcURL)

    def clear_UserName(self):
        return self.clear(*DataSourceMgmtPage.UserName)
    def input_UserName(self, UserName):
        self.clear_UserName()
        return self.send_keys(*DataSourceMgmtPage.UserName, UserName)

    def clear_UserPwd(self):
        return self.clear(*DataSourceMgmtPage.UserPwd)
    def input_UserPwd(self, UserPwd):
        self.clear_UserPwd()
        return self.send_keys(*DataSourceMgmtPage.UserPwd, UserPwd)

    def click_Query_BABU(self):
        return self.click(*DataSourceMgmtPage.Query_BABU)

    def click_babuList_all(self):
        return self.click(*DataSourceMgmtPage.babuList_all)

    def click_saveBtn(self):
        return self.click(*DataSourceMgmtPage.saveBtn)

    def get_Submit_result(self):
        return self.get_element_text(*DataSourceMgmtPage.Submit_result)