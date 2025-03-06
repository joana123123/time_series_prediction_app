import csv
import subprocess

import pandas as pd
import numpy as np
import os
import pymysql
def register_judge_1(username,password,email):
    #前端传来的password是str类型，需要转成int再存
    password = int(password)
    #前端传来的是html对象的email转成字符串存
    email = str(email)
    #首先读出用户的数据，检测这个用户名是否使用过
    df_1 = pd.read_csv('User_data/user_data_1.csv')
    #转换成字典型，检测是否已经使用过这个用户名
    df_1 = pd.DataFrame(df_1)
    user_password_dict = {user:pwd for user,pwd in zip(df_1['username'],df_1['password'])}
    if username in user_password_dict or username == 'username':
        #表明这个用户名已经使用过了，所以不可以再用了
        #这个用户名也不可以是username,因为username是被我用来标记未登录的全局变量
        return 0
    else:
        #将新用户的数据存入统一管理user数据的user_data_1.csv文件中
        new_user = {
            'username':username,
            'password':password,
            'email':email,
            'personal_data':'',   #显示设为空的字符串，因为用户一开始没有传入数据
            'personal_model':'',  #显示设为空的字符串，因为用户一开始没有传入数据
        }

        conn = pymysql.connect(
            host='localhost',  # 数据库主机地址，本地数据库一般为 'localhost'
            user='root',  # 数据库用户名
            password='1234567',  # 数据库密码，替换为你自己设置的密码
            database='test_db',  # 要连接的数据库名，如果不存在需要先创建
            charset='utf8mb4'  # 字符编码
        )
        # try:
        #     # 创建游标对象
        #     cursor = conn.cursor()
        #     # 执行创建数据库的 SQL 语句
        #     cursor.execute("CREATE DATABASE IF NOT EXISTS test_db")
        #     print("数据库创建成功！")
        # except pymysql.Error as e:
        #     print(f"数据库创建失败：{e}")

        try:
            cursor = conn.cursor()
            # 定义插入数据的 SQL 语句
            insert_sql = "INSERT INTO user (username, password,email) VALUES (%s, %s,%s)"
            data = (username, password, email)
            cursor.execute(insert_sql, data)
            # 提交事务
            conn.commit()
            print("数据插入成功！")
        except pymysql.Error as e:
            # 回滚事务
            conn.rollback()
            print(f"数据插入失败：{e}")
        finally:
            if conn:
                conn.close()

        #以追加模式写入一个新的用户数据
        file_path = r'.\User_data\user_data_1.csv'
        with open(file_path,'a',newline='',encoding='utf-8') as file:
            fieldnames = ['username','password','email','personal_data','personal_model']
            writer = csv.DictWriter(file,fieldnames=fieldnames)
            writer.writerow(new_user)


        #为用户建立一个新的文件夹，保存每个用户自己的数据和模型以及配置
        folder_path = r"./" + username
        # 创建文件夹
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
        # 设置文件夹权限为任何用户可写
        try:
            # 使用 icacls 命令设置权限
            command = f'icacls "{folder_path}" /grant Everyone:(OI)(CI)F /T'
            subprocess.run(command, shell=True, check=True)
            print(f"文件夹 {folder_path} 已创建并设置为任何用户可写。")
        except subprocess.CalledProcessError as e:
            print(f"设置权限时出错: {e}")


        #创建保存配置的文件夹(cfg)
        folder_path = r"D:/25_fwwb/upload/" + username + "/cfg"
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
        #设置权限为任何用户可写
        try:
            #使用icacls命令设置权限
            command = f'icacls "{folder_path}" /grant Everyone:(OI)(CI)F /T'
            subprocess.run(command, shell=True, check=True)
            print(f"文件夹 {folder_path} 已创建并设置为任何用户可写。")
        except subprocess.CalledProcessError as e:
            print(f"设置权限时出错: {e}")


        #创建一个保存数据集的文件夹(dataset)
        folder_path = r"D:/25_fwwb/upload/" + username + "/dataset"
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
        # 设置权限为任何用户可写
        try:
            # 使用icacls命令设置权限
            command = f'icacls "{folder_path}" /grant Everyone:(OI)(CI)F /T'
            subprocess.run(command, shell=True, check=True)
            print(f"文件夹 {folder_path} 已创建并设置为任何用户可写。")
        except subprocess.CalledProcessError as e:
            print(f"设置权限时出错: {e}")


        #创建一个保存模型结果的文件夹(checkpoints)
        folder_path = r"D:/25_fwwb/upload/" + username + "/checkpoints"
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
        # 设置权限为任何用户可写
        try:
            # 使用icacls命令设置权限
            command = f'icacls "{folder_path}" /grant Everyone:(OI)(CI)F /T'
            subprocess.run(command, shell=True, check=True)
            print(f"文件夹 {folder_path} 已创建并设置为任何用户可写。")
        except subprocess.CalledProcessError as e:
            print(f"设置权限时出错: {e}")


            # 创建一个保存测试结果的文件夹"results"
        folder_path = r"D:/25_fwwb/upload/" + username + "/results"
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
        # 设置权限为任何用户可写
        try:
            # 使用icacls命令设置权限
            command = f'icacls "{folder_path}" /grant Everyone:(OI)(CI)F /T'
            subprocess.run(command, shell=True, check=True)
            print(f"文件夹 {folder_path} 已创建并设置为任何用户可写。")
        except subprocess.CalledProcessError as e:
            print(f"设置权限时出错: {e}")


        #创建一个保存测试结果的文件夹"test_results"
        folder_path = r"D:/25_fwwb/upload/" + username + "/test_results"
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
        # 设置权限为任何用户可写
        try:
            # 使用icacls命令设置权限
            command = f'icacls "{folder_path}" /grant Everyone:(OI)(CI)F /T'
            subprocess.run(command, shell=True, check=True)
            print(f"文件夹 {folder_path} 已创建并设置为任何用户可写。")
        except subprocess.CalledProcessError as e:
            print(f"设置权限时出错: {e}")


        return 1

# register_judge_1('admin','123456','794817030@qq.com')