# 初始化CSP数据
# 1.执行初始化脚本到V3.2,存储过程
# 2.执行此文件对seq进行排序

import pymysql

# 连接数据库
conn1= pymysql.Connect(host="172.18.188.103",
                       user="root",
                       password="123456",
                       port=3307,
                       db="csp",
                       charset="utf8",
                       )
cursor1=conn1.cursor()
sql1 = "SELECT CAST(OID AS CHAR) FROM mf_function ORDER BY oid;"
cursor1.execute(sql1)
mf_function_oid=cursor1.fetchall()
print(mf_function_oid)
print(''.join(mf_function_oid[0]))

for i in range(0,len(mf_function_oid)):
    mf_function_oid1=''.join(mf_function_oid[i])
    sql2 = "SELECT CAST(OID AS CHAR) FROM mf_function_detail WHERE functionOid =%s ORDER BY oid;"
    cursor1.execute(sql2 %mf_function_oid1)
    mf_function_detail_oid=cursor1.fetchall()
    for j in range(0,len(mf_function_detail_oid)):
        mf_function_detail_oid1=''.join(mf_function_detail_oid[j])
        sql3 = "UPDATE mf_function_detail SET seq=%s WHERE functionOid =%s AND oid=%s;"
        cursor1.execute(sql3 %(j+1,mf_function_oid1,mf_function_detail_oid1))
        conn1.commit()

cursor1.close()
conn1.close()

