# encoding:UTF-8
# 函数的可变长参数

def howlong(a, b, c):
    print('a参数：%s' % a)
    print('b参数：%s' % b)
    print('c参数：%s' % c)


howlong(1, 2, 3)


def demo01(a, *b):
    print(1 + len(b))


demo01(1, 2, 3)
