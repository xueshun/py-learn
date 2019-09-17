# encoding:utf-8
# requests get/post 请求
import requests

# GET
print('requests 模拟 GET 请求')
url = 'http://httpbin.org/get'
data = {'key': 'value', 'abc': 'xyz'}
response1 = requests.get(url, data)
print(response1.text)

# POST
print('requests 模拟 POST 请求')
url_post = 'http://httpbin.org/post'
data_post = {'key': 'value', 'abc': 'xyz'}
resp_post = requests.post(url_post, data_post)
print(resp_post.text)
