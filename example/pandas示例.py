import pandas as pd

if __name__ == '__main__':
    data = {
        'a': [1,2,3],
        'b': [4,5,6],
        'c': [7,8,9],
    }
    #创建DataFrame
    data_frame1 = pd.DataFrame(data)
    print(data_frame1)

    # 创建DataFrame,只要a,b列
    data_frame2 = pd.DataFrame(data,columns=['a','b'])
    print(data_frame2)

    # 为DataFrame添加d列
    data_frame2['d'] = [11,12,13]
    print(data_frame2)

    #删除数据
        #删除行
    data_frame2.drop([0],inplace=True)

        #删除前三行
    # data_frame2.drop(labels=range(0,3), axis=0, inplace=True)

        #删除列
    # data_frame2.drop(labels='a', axis=1, inplace=True)

    #修改数据 , 把a列第1行的数据改为10
    data_frame2['a'][0] =10
    data_frame2['b'] = [1,2]
    data_frame2['b'] = 1

    # 查询数据
        # 查询列
    data_frame2.b
    data_frame2['b']

        #查询行
    data_frame2[0:3]

    #文件的存取
    #存储为csv文件
    data_frame2.to_csv('test.csv')


    # 读取csv文件
    data_frame3 = pd.read_csv('test.csv')

