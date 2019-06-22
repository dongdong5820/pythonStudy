'''
数据库连接
先要安装PyMySQL模块 ：pip3 install PyMySQL
fetchone():获取下一个查询结果集。结果集是一个tuple对象
fetchall():接受全部的返回结果行。也是tuple对象
'''
import pymysql,time

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

sql = 'UPDATE label SET end_time=%d WHERE id=143' % int(time.time())
print(sql)
try:
	cursor.execute(sql)
	affectedRows = cursor.rowcount
	# 提交事务
	connect.commit()
	print('影响行数: %d'%affectedRows)
except:
	print('发生错误')
	connect.rollback()	

# 关闭游标
cursor.close()

#关闭数据库连接
connect.close()

