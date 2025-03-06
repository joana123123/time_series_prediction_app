import csv
import os
import shutil

import pandas as pd
def cancel_account_1(upload_predix_path,username):
    username_to_cancel = username
    # 读取原文件的内容
    data = []
    csv_file_path = 'User_data/user_data_1.csv'
    df = pd.read_csv(csv_file_path)
    for index,row in df.iterrows():
        #iterrows中包含了行索引和行内容,index中包含行索引

        if row['username'] != username_to_cancel:
            username = row['username']
            email = row['email']
            password = row['password']
            personal_data = row['personal_data']
            personal_model = row['personal_model']
            temp = [username, email, password, personal_data, personal_model]
            data.append(temp)

    #将剩余数据重新写回新的文件中去
    data = pd.DataFrame(data)
    # 设置列索引
    data.columns = ["username", "password", "email", "personal_data", "personal_model"]
    data.to_csv('User_data/user_data_1.csv', index=False)

    #将用户文件夹全部都删除
    folder_path = upload_predix_path + '/' +  username_to_cancel
    try:
        #尝试使用递归删除指定文件夹的内容
        shutil.rmtree(folder_path)
    except:
        print(f"指定文件夹无法删除")
    return None

# cancel_account_1('xiaoming')