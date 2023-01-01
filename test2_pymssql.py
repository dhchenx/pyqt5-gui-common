import pymssql

# DB configuratiob
server = "127.0.0.1\SQLEXPRESS"
user = "sa"
password = "123456"
# connectoin
conn = pymssql.connect(server, user, password, database='HealthEval',
                               # charset="cp936"
                               )
cursor = conn.cursor()  # 数据库里面的操作指针
# define search condition
user_id=""
where = "where 1=1 "
if user_id != "":
    where += f" and PatientId = '{user_id}'"
# execute sql statement
cursor.execute(f"select *  FROM PatientInfo {where}")  # 向数据库发送SQL命令

row = cursor.fetchone()
list_result = []
while row:
    data = []
    for idx, d in enumerate(row):
        if idx == 0:
            data.append(str(d))
        else:
            data.append(str(d).encode("latin-1").decode("gbk"))
    print(data)
    list_result.append(data)
    row = cursor.fetchone()

conn.close()