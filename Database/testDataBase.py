from Database.mysqlBase import MySQLBase
import Common.define as Define


class TestDataBase(MySQLBase):
    def __init__(self):
        self.host = Define.getDBConfig('MS_DATABASE', 'DB_HOST')
        self.port = int(Define.getDBConfig('MS_DATABASE', 'DB_PORT'))
        self.dbName = Define.getDBConfig('MS_DATABASE', 'DB_NAME')
        self.user = Define.getDBConfig('MS_DATABASE', 'DB_USER')
        self.password = Define.getDBConfig('MS_DATABASE', 'DB_PASSWORD')
        self.charset = Define.getDBConfig('MS_DATABASE', 'DB_CHARSET')

    def get_test_data_by_name(self, Project, Module, Name, pri='0'):
        # 根据项目名称，模块名称，以及用例名称来获取用例数据
        sql1 = "SELECT  d.data_contents FROM project p JOIN skw_ui_test_data_head h ON (p.id = h.project_id)" \
               " JOIN skw_ui_test_data_detail d ON (h.id = d.ui_test_id) WHERE p.name='%s'" \
               " AND h.name='%s' and d.name='%s' " % (Project, Module, Name)
        # 测试级别不存在时忽略级别参数设定
        if pri != '0':
            sql1 = sql1 + "and d.priority = '%s'" % pri
        else:
            #从配置文件中读取：CASELEVEL
            pris = ",".join(tuple(Define.getDirConfig("CASELEVEL", "level").split(",")))
            print(pris)
            sql1 = sql1 + "and d.priority in ("+ pris +")"
        print(sql1)
        try:
            test_data = self.mysql_execute(sql1)
            results = []
            for result in test_data:
                for lists in result:
                    results.append(tuple(lists.split('->')))
            return results
        except Exception as e:
            print(e)
            return 'error: No option "{}" in section: "{}"'.format(e)


if __name__ == '__main__':
    db = TestDataBase()
    # data = db.get_test_data_by_name("CSP", "login_data", "login_success_data")
    # print(data)
