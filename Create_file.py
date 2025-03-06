#我的文件夹需要用python代码创建才可以写入
#不知道为什么不这样创建就会只能读不能写
import os
import csv

import pandas as pd
import os
import subprocess

# 定义要创建的文件夹路径
folder_path = r"D:/25_fwwb/upload/"

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

#
# new_user = {
#             'username':'xiaoming',
#             'password':123456,
#             'email':'794817030@qq.com',
#             'personal_data':'',   #显示设为空的字符串，因为用户一开始没有传入数据
#             'personal_model':'',  #显示设为空的字符串，因为用户一开始没有传入数据
#         }
# # 以追加模式写入一个新的用户数据
# file_path = r'D:\25服创和计设\front_end_3\User_data\user_data_1.csv'
# with open(file_path, 'a', newline='', encoding='utf-8') as file:
#     fieldnames = ['username', 'password', 'email', 'personal_data', 'personal_model']
#     writer = csv.DictWriter(file, fieldnames=fieldnames)
#     writer.writerow(new_user)