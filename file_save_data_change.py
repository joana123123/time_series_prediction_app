import csv
import pandas as pd

def file_save_data_change(upload_prefix_path,username,data,file):
    file_path = upload_prefix_path + '/' + username + '/dataset/' + data + '.csv'
    file.save(file_path)

    data = str(data)
    # 存储修改之后的行数据
    #向统一管理用户的表中记录这个信息
    user_path = r'D:\25服创和计设\front_end_3\User_data\user_data_1.csv'

    #读取csv文件
    df = pd.read_csv(user_path)
    #找到username所在的列，添加信息
    for index,row in df[df['username'] == username].iterrows():
        original_data = row['personal_data']
        original_data = str(original_data)
        if pd.isnull(original_data):
            new_data = data
        else:
            new_data = original_data + ',' + data
        df.at[index,'personal_data'] = new_data

    #将修改后的文件存回
    df.to_csv(user_path)
    return 1

# file_save_data_change('1','xiaoming','string','123')
