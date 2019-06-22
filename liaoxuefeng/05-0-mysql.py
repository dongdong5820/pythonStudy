'''
数据库连接
先要安装PyMySQL模块 ：pip3 install PyMySQL
'''
import pymysql

db_host = '10.40.6.26'
db_port = 3306
db_database = 'obs_gb_new'
db_username = 'gb_m_user'
db_password = 'fEtWqVMzBC'

# 创建数据库连接
connect = pymysql.connect(db_host,db_username,db_password,db_database)

# 创建一个游标对象 cursor
cursor = connect.cursor()

# 准备sql语句
field = 'id,label_name,start_time,end_time,`type`,service_order,create_time,update_time,updater,logo'
sql = 'SELECT %s FROM label WHERE is_delete=0 AND is_effective=1 ORDER BY id DESC LIMIT 10' % field

# 使用execute() 方法执行sql语句
cursor.execute(sql)

# 使用 fetchone() 方法获取单条数据
#data = cursor.fetchone()
data = cursor.fetchall()

print(type(data))
print(data)

# 关闭游标
cursor.close()

#关闭数据库连接
connect.close()

