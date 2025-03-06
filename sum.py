import pandas as pd
from flask import Flask,request,jsonify,render_template
from login_judge_1 import login_judge_1
from register_judge_1 import register_judge_1
from file_save_data_change import file_save_data_change
from cancel_account_1 import cancel_account_1
from create_config import create_config
import os
app = Flask(__name__)

global_username = 'username'
#这个字段用来记录现在登录的是哪个用户,把用户上传的数据传到它自己的文件夹底下
upload_prefix_path = r"D:/25_fwwb/upload"
#存放上传文件的指定路径前缀(就是这个前缀是固定的，不管是谁传都传到这个前缀底下)
#但不同的用户会传到不同用户自己的文件夹底下
#主页支持的后端路由
@app.route('/')
def index():
    return render_template('index.html')

#支持前端登录界面
@app.route('/login',methods=['POST','GET'])
def login():
    return render_template('login.html')


#后端判断是否登录
@app.route('/login_judge',methods=['POST','GET'])
def login_judge():
    global global_username
    #提取相应的字段
    username = request.form.get('username')
    global_username = username
    #用来记录已经有用户登录了
    password = request.form.get('password')
    flag = login_judge_1(username,password)

    if(flag == 1):      #密码或者用户名正确
        return jsonify({"success":True,"message":"登录成功"})
    else:
        return jsonify({"success":False,"message":"用户名或者密码错误"})


#个人主页支持后端
@app.route('/own',methods=['POST','GET'])
def own():
    return render_template('own.html')

#读出已经存在后端的数据
@app.route('/my_data',methods=['POST','GET'])
def my_data():
    #读取文件
    df = pd.read_csv('D:\\25服创和计设\\front_end_3\\User_data\\user_data_1.csv')
    print(df)
    #找到相应用户已经存放的数据
    data = df[df['username'] == global_username]['personal_data'].values[0] if not df[df['username'] == global_username]['personal_data'].empty else False
    if isinstance(data,str):
        #去除字符串中的'nan'
        data = data.replace('nan,','')
    return render_template('my_data.html',data=data)


#注册支持界面
@app.route('/register',methods=['POST','GET'])
def register():
    return render_template('register.html')

#进行注册的判断
@app.route('/register_judge',methods=['POST','GET'])
def register_judge():

    #提取相应的字段
    username = request.form.get('username')
    password = request.form.get('password')
    email = request.form.get('email')
    flag = register_judge_1(username,password,email)
    if flag == 1:
        #表明注册成功了
        return jsonify({"success":True,"message":"注册成功"})
    else:
        #表明出现了重名
        return jsonify({"success":False,"message":"出现重名,请更改用户名"})


@app.route('/upload',methods=['POST','GET'])
def upload():
    return render_template('upload.html')

#用户登出
@app.route('/logout',methods=['POST','GET'])
def logout():
    global global_username
    # 前端发送消息说明用于已经登出了
    global_username = 'username'
    #重新把记录登录状态的变量置成无
    print(global_username)
    return "1"


# 账号的注销
@app.route('/cancel_account',methods=['POST','GET'])
def cancel_account():
    global global_username
    cancel_account_1(upload_prefix_path,global_username)
    return jsonify({"success":True})


#支持文件的上传
@app.route('/upload_deal',methods=['POST','GET'])
def upload_deal():
    #要自动获得user的名字，将上传的文件存在user自己的文件夹底下
    global global_username
    global upload_prefix_path
    if global_username == 'username':
      #此时表明用户还没有登录是不可以上传数据的
        return jsonify({'error':'请先登录'})


    #提取模型训练字段
    #获取key-value中的value字段
    # is_training = request.form.get('is_training')
    # model = request.form.get('model')
    data = request.form.get('data')
    #target = request.form.get('target')
    #pred_len = request.form.get('pred_len')
    file = request.files['file']

    #有些类型的数据要进行转换
    #if is_training == '是':
     #   is_training = 1
    #else:
    #    is_training = 0
    #pred_len = int(pred_len)

    # 检查是否有文件上传
    if 'file' not in request.files:
        #检查request.files中是否存在键'file',这个file对应表单提交中的name字段
        return jsonify({'error':'没有包含文件信息'}),400

    # 检测是否上传了文件
    if file.filename == '':
        return jsonify({'error':'没有选择文件'}),400

    #保存文件z
    if file and file.filename.endswith('.csv'):
        # 检查上传的文件是否是.csv文件
        # 首先保存上传的文件
        # 用户上传的文件保存在它自己的文件夹底下
        flag = file_save_data_change(upload_prefix_path,global_username,data,file)
        if flag == 1:
            return jsonify({'massage':'文件上传成功'}),200
        else:
            return jsonify({'error':'文件上传失败'}),404



if __name__ == '__main__':
    app.run(debug=True,port=3940)