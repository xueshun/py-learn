# encoding:utf-8
# urllib 测试get/post请求，和抓取连接异常
from urllib import request
from urllib import parse
import urllib
import socket

# GET
print('GET 请求测试')
response1 = request.urlopen('http://httpbin.org/get?hello=world', timeout=1)
print(response1.read().decode('utf-8'))

# POST 需要引入parse
print('POST 请求测试')
data = bytes(parse.urlencode({'hell0': 'world'}), encoding='utf-8')
print('POST 请求数据 %s' % data)
response02 = request.urlopen('http://httpbin.org/post', data=data, timeout=1)
print(response02.read().decode('utf-8'))

# 异常抓取
print('测试抓取请求超时异常')
try:
    response3 = urllib.request.urlopen('http://httpbin.org/get', timeout=0.1)
except urllib.error.URLError as e:
    if isinstance(e.reason, socket.timeout):
        print('TIME OUT')
