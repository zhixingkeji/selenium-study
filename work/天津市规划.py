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

guanwang = "http://www.tj.gov.cn/searchsite/tjzww/search.html?siteId=34&searchWord=%E8%A7%84%E5%88%92&pageSize=10&type1=1051&pageNumber="

# # 文章的链接
# xpathURL =   ""

# a标签
xpath_a = "/html/body/div[2]/div[1]/div[3]/div/div/div[3]/div/*/div/div/div/a"

# 时间
xpath_time = "/html/body/div[2]/div[1]/div[3]/div/div/div[3]/div/*/div/div/table/tbody/tr[2]/td/span[2]"

# 文章内容
xpath_text = "/html/body/div[3]/div/div[2]/div[2]//text()"


# # 搜索input输入框
# xpath_input = "/html/body/div[4]/div[1]/div[4]/div/div[2]/div/form/table/tbody/tr[1]/td[1]/label/input"
#
# # 搜索按钮
# xpath_search = "/html/body/div[4]/div[1]/div[4]/div/div[2]/div/form/table/tbody/tr[1]/td[2]/img"
#
# # 分页输入框
# xpath_page = "/html/body/div[4]/div[1]/div[4]/div/div[2]/table[2]/tbody/tr[2]/td/div[3]/input[1]"
#
# # 跳转按钮
# xpath_btn = "/html/body/div[4]/div[1]/div[4]/div/div[2]/table[2]/tbody/tr[2]/td/div[3]/input[2]"

def driverInit():
    # 创建浏览器实例

    # options = webdriver.ChromeOptions()
    # options.add_argument("--proxy-server=http://110.73.2.248:8123")
    driver_path = './chromedriver'
    driver = webdriver.Chrome(executable_path=driver_path)


    href_list = []
    txt_name = []
    time_list = []

    # 得到所有文章的连接和标题(文件名),和时间(文件夹名)
    for indexl in range(1, 118):
        # 1-119
        driver.get(guanwang + str(indexl))
        print("正在访问第" + str(indexl) + "页")
        time.sleep(random.randint(2,4))
        time.sleep(1)

        for link in driver.find_elements(By.XPATH,xpath_a):

            # 得到a的连接
            lin = link.get_attribute("href")
            print("链接:"+lin)

            # 压入链接的列表
            href_list.append(lin)


            # 得到a的标题
            title_name = link.get_attribute('title')
            title_name = title_name.replace(" ","")
            print("标题"+title_name)
            # 将标题压入列表
            txt_name.append(title_name)

        for tim in driver.find_elements(By.XPATH,xpath_time):
            ti = str(tim.text)
            print("时间"+ti)
            time_list.append(str(ti))

    for (index, context) in enumerate(href_list):
        driver.get(context)
        time.sleep(random.randint(2,4))
        time.sleep(2)
        response = driver.page_source
        tree = etree.HTML(response)
        text = tree.xpath(xpath_text)

        # 判断文件夹是否存在,没有则创建
        path = "./12个市规划" + "/天津市规划/" + time_list[index][0:4] + "/" + time_list[index][5:7] +"/" + txt_name[index]

        print("***文件夹路径是: " + path)

        if not os.path.exists(path):
            print("***路径不存在,正在创建")
            os.makedirs(path)

        print("***正在写入txt文件中: " + str(text))
        str2 = str(text).replace("\'", "").replace("\\u3000", "").replace("\\u2002", "") \
            .replace(" ", "").replace("、", "").replace(",", "") \
            .replace("。", "。\n").replace("\\n", "").replace("\\xa0", "")

        # 写入数据强转成str
        with open(path +"/"+txt_name[index]+".txt", 'w+', encoding='utf-8') as fh:
            fh.write(str2)

        print("***当前文章所有文字爬取完成")
        time.sleep(1)



if __name__ == "__main__":
    driverInit()
