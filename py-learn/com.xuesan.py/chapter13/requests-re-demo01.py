# encoding:utf-8
# requests和re获取图片地址和名称
import requests
import re

content = requests.get('http://www.cnu.cc/discoveryPage/hot-人像').text

# print('获取到的页面信息为 %s' % content)

# <a href="http://www.cnu.cc/works/332291" class="thumbnail" target="_blank">
#   <div class="title">
#     #On the STREET of daylight.
#   </div>
#   <div class="author">
#     摄影师Gin
#   </div>
# </a>

# 需要抓取的内容为 http://www.cnu.cc/works/332291 On the STREET of daylight.
# 正则表达式 < a href="(.*?)".*?title">(.*?)</div>

pattern = re.compile(r'<a href="(.*?)".*?title">(.*?)</div>', re.S)
results = re.findall(pattern, content)
# print(results)

for result in results:
    url, name = result
    print(url, re.sub('\s', '', name))
