from selenium import webdriver  # 导入自动化模块
from selenium.webdriver.common.by import By

def isPDF(url):
    driver = webdriver.Chrome(executable_path='/Users/wl/Projects/zgc/scrapy/work/chromedriver')

    driver.get(url)
    pdfA = driver.find_elements(By.XPATH, "//a")

    print("***正在判断是否有pdf文件\n")
    for pdfA_url in pdfA:
        tpdf = pdfA_url.get_attribute("href")
        pdfName = pdfA_url.text
        # 切割.pdf后面的所有字符串
        if '.pdf' in str(tpdf):
            tpdf = str(tpdf).split('.pdf', 1)[0] + '.pdf'
            print("***找到了pdf文件,名称为:" + tpdf + "\n")
            print("***正在保存pdf文件\n")
            print("pdfName= " + pdfName)
            try:
                a = 1/0
            except:
                print("***文件保存失败," + tpdf)

                # 输出日志
                # log_handler("文档下载失败", tpdf, url_input, dir_path)
                # continue

            # 保存文件
            # with open( "./",+ 'wb+', ) as fh:
            #     fh.write("11")
            print("***保存完成\n")


if __name__ == "__main__":
    isPDF("http://www.beijing.gov.cn/gongkai/guihua/wngh/sjzdzxgh/202105/t20210510_2385364.html")
