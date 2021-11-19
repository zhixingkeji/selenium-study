import random

from selenium import webdriver  # 导入自动化模块
import time  # 时间模块
import requests  # 导入网络模块
import os  # 导入文件模块
import re  # 导入正则模块
from lxml import etree  # 导入xpath模块
import json  # json模块
import pandas as pd  # 数据存储模块
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import requests, sys
import ssl
import json
import time
import base64
import urllib.request
import urllib.parse



# 用字典封装了常用的网站
url_dict = {
    "GDP": "http://tjj.beijing.gov.cn/tjsj_31433/yjdsj_31440/gdp_31750/",
    "重点专项规划": "http://www.beijing.gov.cn/gongkai/guihua/wngh/sjzdzxgh/",
    "pdf_url": "http://www.beijing.gov.cn/gongkai/guihua/wngh/qjghgy/201907/t20190701_100208.html",
    "img_url": "http://www.beijing.gov.cn/gongkai/guihua/wngh/sjzdzxgh/202109/t20210908_2488076.html",
    "市级重点专项规划":"http://www.beijing.gov.cn/gongkai/guihua/wngh/sjzdzxgh/",
    "市级一般专项规划": "http://www.beijing.gov.cn/gongkai/guihua/wngh/ybzxgh/",
    "其他规划":"http://www.beijing.gov.cn/gongkai/guihua/wngh/qtgh/",
    "长期规划": "http://www.beijing.gov.cn/gongkai/guihua/wngh/cqgh/",
    "区级规划纲要":"http://www.beijing.gov.cn/gongkai/guihua/wngh/qjghgy/"


}



# 定义日志类函数
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



# 封装了pdf文件的下载
def request_downloadpdf(PDF_URL):

    pdf_url_name = str(PDF_URL).replace("/", "")
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36"}

    url_a = requests.get(url=PDF_URL, headers=headers).content
    return(url_a)


# 封装的orc函数
def orc_func(path):
    image_path = path



    with open(image_path, 'rb') as fp:  # 以二进制读取本地图片
        data = fp.read()
        encodestr = str(base64.b64encode(data), 'utf-8')  # base64编码图片


    # 请求头
    headers = {
        'Authorization': 'APPCODE 0b31dd6902744f508347659d5ea1bb54',  # APPCODE +你的appcod,一定要有空格！！！
        'Content-Type': 'application/json; charset=UTF-8'  # 根据接口的格式来
    }

    def posturl(url, data={}):



        try:
            params = json.dumps(dict).encode(encoding='UTF8')
            req = urllib.request.Request(url, params, headers)
            r = urllib.request.urlopen(req)
            html = r.read()
            r.close()
            return html.decode("utf8")
        except urllib.error.HTTPError as e:
            print(e.code)
            print(e.read().decode("utf8"))
        time.sleep(1)

    if __name__ == "__main__":
        url_request = "https://ocrapi-advanced.taobao.com/ocrservice/advanced"  # 对照官网API改
        dict = {'img': encodestr}
        html = posturl(url_request, data=dict)

        jos = json.loads(html)
        result = jos['content']
        print('***识别结果：', result)
        return(str(result))


# 封装的图片下载函数
def request_download(IMAGE_URL):
    img_url_name = str(IMAGE_URL).replace("/", "")
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36"}
    try:
        url_a = requests.get(url=IMAGE_URL, headers=headers,timeout=5).content
    except requests.exceptions.RequestException as e:
        print(str(e))


    with open("/Users/wl/Projects/zgc/scrapy/temp/img/"+img_url_name, "wb+") as fp:
        fp.write(url_a)
    return "/Users/wl/Projects/zgc/scrapy/temp/img/"+img_url_name

# 封装 seleenium驱动请求
def driverInit():
    # 创建浏览器实例

    # options = webdriver.ChromeOptions()
    # options.add_argument("--proxy-server=http://110.73.2.248:8123")
    driver_path='/Users/wl/Projects/zgc/scrapy/work/chromedriver'
    driver = webdriver.Chrome(executable_path=driver_path)
    url_input = "长期规划"
    print("***您访问的网站名是:" + url_input )

    # 访问网址
    print("***正在请求网址:" + url_dict[url_input] )
    driver.get(url_dict[url_input])
    print("***网站请求完成" )

    # 得到所有a标签的title和url  且装进列表
    hreflist = []
    txtname = []
    for link in driver.find_elements(By.XPATH,'/ html / body / div[5] / * / * / a'):

        hrefurl = link.get_attribute('href')
        titlename = link.get_attribute('title')
        hreflist.append(hrefurl)
        txtname.append(titlename)
    print("***文章连接列表请求完成"+ str(hreflist) + "\n")
    print("***文章标题列表请求完成"+ str(txtname) + "\n")


    # 文件夹路径
    dr1 = input("***请输入保存的文件夹名称: 如 规划\n")


    # 对列表进行枚举访问, 同时获得下标和对象
    print("***正在循环访问每篇文章" )

    for (index, ali) in enumerate(hreflist):
        print("***正在访问第 ",str(int(index)+1) +" 篇文章")
        driver.get(ali)
        response = driver.page_source

        # 保存所有文字
        tree = etree.HTML(response)
        text = tree.xpath('/html/body/div[5]/div/div[1]/div[2]/div[1]//text()')

        # 对字符串进行格式清洗
        str2 = str(text).replace("\'", "").replace("\\u3000", "") \
            .replace(" ", "").replace("、", "").replace(",", "") \
            .replace("。", "。\n").replace("\\n", "").replace("\\xa0", "")

        print("***当前的文件标题是:" + txtname[index])




        # 判断文件夹是否存在,没有则创建
        path = "./" + dr1 + "/" + url_input + "/" + txtname[index]
        print("***文件夹路径是: " + path)

        if not os.path.exists(path):
            print("***路径不存在,正在创建")
            os.makedirs(path)


        print("***正在写入txt文件中: " + str2)
        # 写入数据强转成str
        with open(path + "/" +txtname[index] + ".txt", 'w+', encoding='utf-8') as fh:
            fh.write(str2)

        print("***当前文章所有文字爬取完成")



        # 判断是否有pdf文件
        pdfA = driver.find_elements(By.XPATH,"//a")
        print("***正在判断是否有pdf文件\n")
        for pdfA_url in pdfA:
            tpdf = pdfA_url.get_attribute("href")
            pdfName = pdfA_url.text
            #切割.pdf后面的所有字符串
            if '.pdf' in str(tpdf):
                tpdf = str(tpdf).split('.pdf', 1)[0] + '.pdf'
                print("***找到了pdf文件,名称为:"+pdfName)
                print("***正在保存pdf文件\n")
                try:
                    pdfcontext = request_downloadpdf(tpdf)
                    # 保存文件
                    with open(path + "/" + pdfName, 'wb+', ) as fh:
                        fh.write(pdfcontext)
                    print("***保存完成\n")

                except:
                    print("***文件保存失败,"+tpdf)

                    # 输出日志 类型 URL 当前网站名 文件原有路径
                    log_handler("文档下载错误", tpdf, url_input, path + "/" + pdfName)
                    continue


        # 判断是否有图片,保存所有图片,文字识别
        print("***正在判断是否存在图片\n")
        imgA = driver.find_elements(By.TAG_NAME,"img")
        for  imgA_url in imgA:
            t_img = imgA_url.get_attribute("src")

            # 切割图片地址后缀后面的无效参数
            if ".png" in t_img:
                # 切割.png后面的所有字符串
                t_img = str(t_img).split('.png', 1)[0] + '.png'
            elif ".jpg" in t_img:
                # 切割.jpg后面的所有字符串
                t_img = str(t_img).split('.jpg', 1)[0] + '.jpg'
            elif ".jpeg" in t_img:
                # 切割.jpg后面的所有字符串
                t_img = str(t_img).split('.jpeg', 1)[0] + '.jpeg'

            print("***当前的图片地址是:"+t_img)
            print("***正在保存图片到 temp/img")
            # 获取图片所在的位置
            try:
                orc_img_local = request_download(t_img)
            except:
                print("***图片下载失败:",t_img)
                # 输出日志 类型 URL 当前网站名 文件应该存在的位置
                log_handler("图片下载错误", t_img, url_input, "temp/img/" + t_img)
                continue

            # 延迟1秒
            time.sleep(1)


            # 小于50kb的图片不进行识别
            print("***正在进行文字识别")

            # 对文件大小进行判断, 小于50kb则直接跳过
            img_size = os.path.getsize(orc_img_local)

            # 如果大于50kb 则进行文字识别 异常处理
            if img_size > 51200:
                try:
                    orc_str = orc_func(orc_img_local)
                    print(orc_str)
                    print("***识别完成\n")
                    # 保存文件
                    with open(path + "/" + t_img.replace("/", "") + ".txt", 'w+', encoding='utf-8') as fh:
                        fh.write(orc_str)
                except:
                    print("图片识别失败"+ orc_img_local)
                    # 获取日志 类型, url , 日志输出目录 , 文件该保存的位置
                    log_handler("文字识别错误", t_img, url_input, path + "/" + t_img.replace("/", "") + ".txt")
                    continue
            else:
                print("***不是关键图片,正在识别下一张图片")





# 入口函数
if __name__ == '__main__':
    driverInit()


    # 判断是否有下一页
    # 关键字清洗



