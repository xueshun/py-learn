# encoding:utf-8
# 使用urllib
from urllib import request

url = 'http://www.baidu.com'

respMsg = request.urlopen(url, timeout=1)
print(respMsg.read().decode('utf-8'))
