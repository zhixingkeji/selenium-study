# coding=gbk


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
if __name__=="__main__":
    driver = webdriver.Chrome(executable_path='../work/chromedriver')


    # 访问网址
    driver.get("http://www.beijing.gov.cn/gongkai/guihua/wngh/cqgh/202004/t20200409_1798426.html")
    # 返回整个页面数据
    response = driver.page_source

    # 打印返回的数据
    # print(response)

    # 创建xpath实例并解析
    tree = etree.HTML(response)
    ul_list = tree.xpath('/html/body/div[5]/div/div[1]/div[2]/div[1]/div/p[2]/text()')[0]
    print(ul_list)


    str2 = str(ul_list).strip("\u3000").replace("、","").replace("。","。\n")
    print(str2)

    with open("./2.txt", 'w+', encoding='utf-8') as fh:
        fh.write(str(str2))
