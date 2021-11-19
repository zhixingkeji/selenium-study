import requests

# 封装的图片下载函数


def request_download(PDF_URL):

    pdf_url_name = str(PDF_URL).replace("/", "")
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36"}

    url_a = requests.get(url=PDF_URL, headers=headers).content
    with open("/Users/wl/Projects/zgc/scrapy/temp/pdf/"+pdf_url_name, "wb+") as fp:
        fp.write(url_a)

    # 返回当前pdf位置
    return "/Users/wl/Projects/zgc/scrapy/temp/pdf/"+pdf_url_name

if __name__ == "__main__":
    request_download("http://www.beijing.gov.cn/gongkai/guihua/wngh/sjzdzxgh/202109/W020211022559298012405.pdf")
