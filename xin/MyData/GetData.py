import jieba
#应用
#只为获取用户数据，训练时直接使用traindata就好了,本脚本就是为了使userdata变成标准形式，数据预处理要处理的数据也是标准形式的，一句话说，训练是训练，应用是应用
def get_user_data():
    print("Begin")
    userdata=[0,0,0]
    with open(r"C:\Python\xin\userdata.txt",encoding='utf-8') as f:
        for line in f.readlines():
            line = line.strip('\n')  #去掉列表中每一个元素的换行符
            print(line)
            str1=line.split(' ',1)
            print(str1)
            moudlename=str1[1]
            print(moudlename)
            #查询该数据在数据库中的类别,统计数量
            if str1[1]=="蜻蜓":
                userdata[0] +=1
            if str1[1]=="火车":
                userdata[1] +=1
            if str1[1]=="消防员":
                userdata[2] +=1
            #模拟数据库操作
    return userdata
            
