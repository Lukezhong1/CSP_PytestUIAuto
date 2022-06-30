import Common.define as Define
import pymysql

conn = None

class MySQLBase(object):
    def __init__(self, host, user, password, port, dbName, charset):
        self.host = host
        self.user = user
        self.password = password
        self.port = port
        self.dbName = dbName
        self.charset = charset

    def conn_mysql(self):
        global conn
        try:
            conn = pymysql.connect(user=self.user, passwd=self.password,
                                   host=self.host, port=self.port, db=self.dbName, charset=self.charset)
            print("连接数据库成功...", self.host, self.dbName)
        except Exception as e:
            print(e)
        return conn

    #查询数据
    def mysql_execute(self, sql1):
        conn1 = self.conn_mysql()
        cursor1 = conn1.cursor()
        try:
            cursor1.execute(sql1)  # 执行SQL语句
        except Exception as e:
            print(e)
        results = cursor1.fetchall()  # 读取SQL执行得到的结果并赋给变量
        # 元组转字符串
        cursor1.close()  # 关闭游标
        conn1.close()  # 关闭连接
        return results

# a=MySQLBase('172.18.188.103','root','123456',3307,'metersphere','utf8')
# print(a.conn_mysql())
