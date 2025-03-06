import pymysql

# 建立数据库连接

conn = pymysql.connect(
    host='localhost',  # 数据库主机地址，本地数据库一般为 'localhost'
    user='root',  # 数据库用户名
    password='1234567',  # 数据库密码，替换为你自己设置的密码
    database='USER',  # 要连接的数据库名，如果不存在需要先创建
    charset='utf8mb4'  # 字符编码
)
try:
    # 创建游标对象
    cursor = conn.cursor()
    # 执行创建数据库的 SQL 语句
    cursor.execute("CREATE DATABASE IF NOT EXISTS test_db")
    print("数据库创建成功！")
except pymysql.Error as e:
    print(f"数据库创建失败：{e}")
finally:
    if conn:
        conn.close()

