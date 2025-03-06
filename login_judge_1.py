import pandas as pd

def login_judge_1(username,password):
    #前端传来的password是str类型，无法和之前存的内容进行匹配
    password = int(password)
    #首先读出用户的数据
    df_1 = pd.read_csv('User_data/user_data_1.csv')
    #转换成字典类型数据(key是username,value是password,实现哈希查找)
    df_1 = pd.DataFrame(df_1)
    user_password_dict = {user:pwd for user,pwd in zip(df_1['username'],df_1['password'])}

    #zip()函数接收两个及以上的可迭代对象作为参数，将它们压缩成一个由元组组成迭代器
    #字典推导式:它的语法是 {key: value for (key, value) in iterable}
    # 其中 iterable 是一个可迭代对象，每次迭代产生一个元素（在这个例子中是一个元组），这些元素被用来生成字典的键值对。
    #一个字典代表一行数据
    # print(user_password_dict)
    if username in user_password_dict:
        if user_password_dict[username] == password:
            #用户名和密码符合，可以返回正确的信息
            return 1
        else:
            #密码不对
            return 0
    else:
        #不存在这个用户
        return 0


login_judge_1('小明',1234)