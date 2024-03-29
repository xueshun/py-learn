# encoding:utf-8
# urllib 模拟浏览器请求
# 出现这个错误的原因 UnicodeDecodeError: 'utf-8' codec can't decode byte 0x8b in position 1: invalid start by
# 因为返回的内容gzip压缩，所以读取也要解压
from io import BytesIO
from urllib import request, parse
import gzip

url = 'http://httpbin.org/post'

headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate, sdch",
    "Accept-Language": "zh-CN,zh;q=0.8",
    "Connection": "close",
    "Cookie": "_gauges_unique_hour=1; _gauges_unique_day=1; _gauges_unique_month=1; _gauges_unique_year=1; _gauges_unique=1",
    "Referer": "http://httpbin.org/",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.98 Safari/537.36 LBBROWSER"
}

dict = {
    'name': 'value'
}

data = bytes(parse.urlencode(dict), encoding='utf-8')
req = request.Request(url=url, data=data, headers=headers, method='POST')
response = request.urlopen(req)
print(gzip.GzipFile(fileobj=BytesIO(response.read())).read().decode('UTF-8'))
