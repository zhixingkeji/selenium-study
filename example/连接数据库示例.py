
from sqlalchemy import create_engine


# 按间距中的绿色按钮以运行脚本。
if __name__ == '__main__':
    engine = create_engine("mysql+pymysql://root:wangle2018@127.0.0.1:3306/zgc?charset=utf8")
    con = engine.connect()
    result = con.execute("select * from student")
    print(result.fetchall())