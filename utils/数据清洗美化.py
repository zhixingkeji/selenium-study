# coding=gbk


from selenium import webdriver  # �����Զ���ģ��
import time  # ʱ��ģ��
import requests  # ��������ģ��
import os  # �����ļ�ģ��
import re  # ��������ģ��
from lxml import etree  # ����xpathģ��
import json  # jsonģ��
import pandas as pd  # ���ݴ洢ģ��
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
if __name__=="__main__":
    driver = webdriver.Chrome(executable_path='../work/chromedriver')


    # ������ַ
    driver.get("http://www.beijing.gov.cn/gongkai/guihua/wngh/cqgh/202004/t20200409_1798426.html")
    # ��������ҳ������
    response = driver.page_source

    # ��ӡ���ص�����
    # print(response)

    # ����xpathʵ��������
    tree = etree.HTML(response)
    ul_list = tree.xpath('/html/body/div[5]/div/div[1]/div[2]/div[1]/div/p[2]/text()')[0]
    print(ul_list)


    str2 = str(ul_list).strip("\u3000").replace("��","").replace("��","��\n")
    print(str2)

    with open("./2.txt", 'w+', encoding='utf-8') as fh:
        fh.write(str(str2))
