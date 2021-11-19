from selenium import webdriver  # 导入自动化模块
import time  # 时间模块
import requests  # 导入网络模块
import os  # 导入文件模块
import re  # 导入正则模块
from lxml import etree  # 导入xpath模块
import json  # json模块
import pandas as pd # 数据存储模块


if __name__ == '__main__':
    driver = webdriver.Chrome(executable_path='../work/chromedriver')

    driver.get("http://www.beijing.gov.cn/gongkai/guihua/wngh/sjzdzxgh/202109/t20210908_2488076.html")
    response = driver.page_source

    # 保存所有文字
    tree = etree.HTML(response)
    text2 = tree.xpath('/html/body/div[5]/div/div[1]//text()')

    str2 = str(text2).replace("\'","").replace("\\u3000","")\
        .replace(" ", "").replace("、", "").replace(",", "")\
        .replace("。", "。\n").replace("\\n", "").replace("\\xa0", "")

    print("***文章文字内容是: " + str2)

    time.sleep(20000)
