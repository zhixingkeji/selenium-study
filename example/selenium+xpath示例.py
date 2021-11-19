from selenium import webdriver  # 导入自动化模块
import time  # 时间模块
import requests  # 导入网络模块
import os  # 导入文件模块
import re  # 导入正则模块
from lxml import etree  # 导入xpath模块
import json  # json模块
import pandas as pd # 数据存储模块

# 按间距中的绿色按钮以运行脚本。
if __name__ == '__main__':
    bro = webdriver.Chrome(executable_path='../work/chromedriver')
    # 显式等待

    # 隐式等待
    # bro.implicitly_wait(5)
    # 访问网址

    bro.get('https://www.baidu.com')
    time.sleep(3)
    # 返回整个页面数据
    response = bro.page_source


    # 创建xpath实例并解析
    tree = etree.HTML(response)
    li_list = tree.xpath('/ html / body / div[1] / div[1] / div[5] / div / div / div[3] / ul / li')
    print(li_list)
    for li in li_list:
        name = li.xpath('./a / span[2]/text()')[0]
        print(name)


    # 退出浏览器
    time.sleep(20)
    bro.quit()
