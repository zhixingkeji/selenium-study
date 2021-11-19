import os
import time

# 格式化成2016-03-20 11:45:39形式


# 日志类函数封装


# 参数解释
# type 错误类型
#
#

def log_handler(type ,url,name,dir_path):
    # 日志存放位置
    log_path = "/Users/wl/Projects/zgc/scrapy/logging/" + name
    if not os.path.exists(log_path):
        print("===日志路径不存在,正在创建")
        os.makedirs(log_path)

    log_context = "异常类型: " + type + " | " + "url地址: "  + url + " | " + "文件路径: " + dir_path +" | " +"时间: " + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) +"\n"

    if type == "文字识别错误":
        print("===写入日志文件:orc_exception")
        with open(log_path+"/" + name + ".txt", "a+") as fh:
                fh.write(log_context)

    elif type =="文档下载错误":
        print("===写入日志文件:pdf_exception")
        with open(log_path+"/" + name + ".txt","a+") as fh:
                fh.write(log_context)

    elif type == "图片下载错误":
        print("===写入日志文件:img_exception")
        with open(log_path+"/" + name + ".txt","a+") as fh:
                fh.write(log_context)


    # 返回一个文件的地址和该写入的文件路径
    return [url,dir_path]


if __name__ == "__main__":
    log_handler("图片下载错误","http://1223","北京规划","user/path.txt")