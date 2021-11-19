import requests, sys
import ssl
import json
import time
import base64
import urllib.request
import urllib.parse
import os


def orc_func(path):
    image_path = path
    img_size =  os.path.getsize(path)

    # 如果小于50kb 则跳过
    if img_size<51200:
        return "***该文件太小 不是关键图片"

    print("***文件大小为: "+ str(img_size))
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

        # 返回查询的结果
        return(str(result))


if __name__=="__main__":
    res = orc_func("/Users/wl/Projects/zgc/scrapy/utils/img.png")
    print(res)
