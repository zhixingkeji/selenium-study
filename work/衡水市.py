


from selenium import webdriver  # 导入自动化模块
import os  # 导入文件模块

from lxml import etree  # 导入xpath模块

from selenium.webdriver.common.by import By

import time
import random



guanwang = "http://www.hengshui.gov.cn/jrobot/search.do?webid=1&pg=12&p="
guanwang2 = "&tpl=&category=%E5%B8%82%E6%94%BF%E5%BA%9C&q=%E8%A7%84%E5%88%92&pos=&od=&date=20100101&date=20211030"


# # 文章的链接
# xpathURL =   ""

# a标签
xpath_a = "/html/body/form/div[3]/div/div/div[3]/div/div[7]/*/div[2]/a"

# a的文本
xpath_a_text = "/html/body/form/div[3]/div/div/div[3]/div/div[7]/*/div[2]/a//text()"

# 时间
xpath_time = "/html/body/form/div[3]/div/div/div[3]/div/div[7]/*/div[3]/div[1]/span"


# 文章内容
xpath_text = "/html/body/div[2]/div[4]/div//text()"


# 下载图片,注意a标题的提取,注意时间的截取

def driverInit():
    # 创建浏览器实例
    driver_path = './chromedriver'
    driver = webdriver.Chrome(executable_path=driver_path)

    # a连接列表
    href_list = []
    # 标题列表
    txt_name = []
    # 时间列表
    time_list = []

    # 得到所有文章的连接和标题(文件名),和时间(文件夹名)
    for indexl in range(1, 17):
        # 1-17

        driver.get(guanwang + str(indexl)+ guanwang2)
        print("正在访问第" + str(indexl) + "页\n\n")
        time.sleep(random.randint(1, 3))
        time.sleep(1)
        response = driver.page_source

        tree = etree.HTML(response)
        a_text = tree.xpath(xpath_a)

        # 循环所有标题a标签
        for link in driver.find_elements(By.XPATH, xpath_a):
            # 得到a的连接
            lin = link.get_attribute("href")
            print("链接:" + lin)
            # 压入链接的列表
            href_list.append(lin)

        # 循环所有标题
        for lit in a_text:
            li = lit.xpath(".//text()")
            li = str(li).replace(" ", "").replace(",", "").replace("\'", "").replace("[", "").replace("]", "").replace("\\t", "").replace("/", "").replace("\"","").replace("\'", "")
            print("标题" + li)
            # 将标题压入列表
            txt_name.append(li)

        for tim in driver.find_elements(By.XPATH, xpath_time):
            ti = str(tim.text)
            print("时间" + ti)
            time_list.append(str(ti))
        time.sleep(1)

    for (index, context) in enumerate(href_list):
        driver.get(context)
        time.sleep(random.randint(2, 4))
        time.sleep(2)
        response = driver.page_source
        tree = etree.HTML(response)
        text = tree.xpath(xpath_text)

        # 判断文件夹是否存在,没有则创建
        path = "./12个市规划" + "/衡水市规划/" +time_list[index][0:4] + "/" + time_list[index][5:7]

        print("***文件夹路径是: " + path)

        if not os.path.exists(path):
            print("***路径不存在,正在创建")
            os.makedirs(path)

        print("***正在写入txt文件中: " + str(text))
        str2 = str(text).replace("\'", "").replace("\\u3000", "").replace("\\u2002", "") \
            .replace(" ", "").replace("、", "").replace(",", "").replace("\\t", "") \
            .replace("。", "。\n").replace("\\n", "").replace("\\xa0", "")

        # 写入数据强转成str
        with open(path + "/" + txt_name[index] +".txt", 'w+', encoding='utf-8') as fh:
            fh.write(str2)

        print("***当前文章所有文字爬取完成")
        time.sleep(1)
        time.sleep(1)
        # print("开启爬取图片")
        #
        # # 判断是否有图片,保存所有图片,文字识别
        # print("***正在判断是否存在图片\n")
        # imgA = driver.find_elements(By.TAG_NAME, "img")
        # for imgA_url in imgA:
        #     t_img = imgA_url.get_attribute("src")
        #
        #     # 切割图片地址后缀后面的无效参数
        #     if ".png" in t_img:
        #         # 切割.png后面的所有字符串
        #         t_img = str(t_img).split('.png', 1)[0] + '.png'
        #     elif ".jpg" in t_img:
        #         # 切割.jpg后面的所有字符串
        #         t_img = str(t_img).split('.jpg', 1)[0] + '.jpg'
        #     elif ".jpeg" in t_img:
        #         # 切割.jpg后面的所有字符串
        #         t_img = str(t_img).split('.jpeg', 1)[0] + '.jpeg'
        #
        #     print("***当前的图片地址是:" + t_img)
        #
        #     # 封装的图片下载函数
        #
        #     img_url_name = str(t_img).replace("/", "")
        #     headers = {
        #         "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36"}
        #     try:
        #         url_a = requests.get(url=t_img, headers=headers, timeout=5).content
        #         with open(path + "/" + img_url_name, "wb+") as fp:
        #             fp.write(url_a)
        #         time.sleep(1)
        #
        #         # 如果图片小于100kb 则删除
        #         stat_info = os.stat(path + "/" + img_url_name)
        #         size = stat_info.st_size
        #
        #         if(size<102400):
        #             print("图片太小正在删除")
        #             os.remove(path + "/" + img_url_name)
        #
        #     except requests.exceptions.RequestException as e:
        #         print(str(e))
        #         continue







if __name__ == "__main__":
    driverInit()
