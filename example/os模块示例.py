import os

if __name__ == '__main__':

    # 创建单级目录 且只能创建一个文件夹 ,创建多个要用循环语句
    # path = "./可爱"
    # if not os.path.exists(path):
    #     os.mkdir(path +"./22")


    # 创建多级目录
    path = "./可爱"
    if not os.path.exists(path):
        os.makedirs(path + "/22")