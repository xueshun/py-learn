# encoding:UTF-8
# 迭代器与生成器


# 迭代器
list1 = [1, 2, 3]


# it = iter(list1)
#
# i = 0
# while i < len(list1):
#     print(next(it))
#     i += 1

# 生成器

# for i in range(10, 20, 0.5):
#     print(i)

# 自定义

def frange(start, stop, step):
    x = start
    while x < stop:
        yield x
        x += step


for i in frange(10, 20, 0.5):
    print(i)


# yield 使用
def gen_example():
    print('before any yield')
    yield 'first yield'
    print('between yield')
    yield 'second yield'
    print('no yield anymore')



