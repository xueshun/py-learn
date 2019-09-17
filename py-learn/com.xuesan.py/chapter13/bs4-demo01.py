# encoding:utf-8
# beautifulSoup使用

html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

from bs4 import BeautifulSoup

# 当执行报错，需要下载pip install lxml
soup = BeautifulSoup(html_doc, 'lxml')

print(soup.prettify())

# 找到title标签
print('获取页面titil标签：%s' % soup.title)

# title标签的内容
print('title标签的内容：%s' % soup.title.string)

# 找到p标签
print('获取页面p标签：%s' % soup.p)

# 找到p标签class的名字
print('找到p标签class的名字：%s' % soup.p['class'])

# 找到第一个a标签
print('找到第一个a标签: %s' % soup.a)

# 找到所有的a标签
print('找到所有的a标签：%s' % soup.find_all('a'))

# 找到id为link3的标签
print('找到id为link3的标签：%s' % soup.find(id='link3'))

# 找到所有的a标签
a_all = soup.find_all('a')
print('找到所有a标签：%s' % a_all)
for a_lable in a_all:
    print(a_lable.get('href'))

# 找到文档中所有的文本内容
print('找到文档中所有的文本内容：%s' % soup.get_text())
