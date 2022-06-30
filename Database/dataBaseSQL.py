from Database.mysqlBase import MySQLBase
import Common.define as Define


class DataBaseSQL(MySQLBase):
    def __init__(self):
        self.host = Define.getDBConfig('DATABASE', 'DB_HOST')
        self.port = int(Define.getDBConfig('DATABASE', 'DB_PORT'))
        self.dbName = Define.getDBConfig('DATABASE', 'DB_NAME')
        self.user = Define.getDBConfig('DATABASE', 'DB_USER')
        self.password = Define.getDBConfig('DATABASE', 'DB_PASSWORD')
        self.charset = Define.getDBConfig('DATABASE', 'DB_CHARSET')


    def get_USER_OID(self, userId):
        mysql_userId = None
        try:
            sql1 = "SELECT CAST(a.`OID` AS CHAR)  FROM `fw_security_user` a ORDER BY a.`CREATEDATE` DESC;"  # SQL操作语句
            mysql_userId = self.mysql_execute(sql1)
        except Exception as e:
            print(e)
        finally:
            # print(mysql_userId)
            return mysql_userId

    def get_update_all_report_func_setup(self):
        mysql_userId = None
        try:
            sql1 = "SELECT CAST(functionID AS CHAR) FROM mf_function ORDER BY oid;"  # SQL操作语句
            functionID = self.mysql_execute(sql1)
            exportPath=('D:\\Export_Import',)
            expect=('.csv', 'Operate Successfully',)
            update_all_report_func_setup_success=[]
            for i in range(0,len(functionID)):
                tuple_result=functionID[i]+exportPath+functionID[i]+expect
                update_all_report_func_setup_success.append(tuple_result)
            print(update_all_report_func_setup_success)
        except Exception as e:
            print(e)
        finally:
            return update_all_report_func_setup_success

    def get_add_query_execute_task(self):
        mysql_userId = None
        try:
            sql1 = "SELECT CAST(functionID AS CHAR) FROM mf_function ORDER BY oid;"  # SQL操作语句
            functionID = self.mysql_execute(sql1)
            taskId='_taskId'
            expect=('Operate Successfully',)
            add_query_execute_task=[]
            for i in range(0,len(functionID)):
                str_taskId=''.join(functionID[i])+taskId
                tuple_result=functionID[i]+tuple(str_taskId.split(','))+expect
                add_query_execute_task.append(tuple_result)
            print(add_query_execute_task)
        except Exception as e:
            print(e)
        finally:
            return add_query_execute_task

if __name__ == '__main__':
    db =DataBaseSQL()
    db.get_update_all_report_func_setup()
    db.get_add_query_execute_task()

