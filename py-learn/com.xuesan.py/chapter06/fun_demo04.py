# encoding:UTF-8
# 函数的变量作用域

var1 = '123'


def demo1():
    var1 = '456'
    print('方法作用域内：%s' % var1)


demo1()
print('方法作用域外：%s' % var1)

var2 = 'abc'


def demo02():
    global var2
    var2 = 'bcd'
    print('global方法作用域内：%s' % var2)


demo02()
print('global方法作用域外：%s' % var2)
