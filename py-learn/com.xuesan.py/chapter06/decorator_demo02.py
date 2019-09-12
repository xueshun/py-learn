# encoding:utf-8
# 装饰器使用

# 装饰有参数的方法
# def tips(func):
#     def wapper(a, b):
#         print('start')
#         func(a, b)
#         print('end')
#
#     return wapper
#
#
# @tips
# def add(a, b):
#     print(a + b)
#
#
# print(add(1, 2))

# 装饰器传入参数
def new_tips(argv):
    def tips(func):
        def wapper(a, b):
            print('start %s %s' % (argv, func.__name__))
            func(a, b)
            print('end')

        return wapper

    return tips


@new_tips('add_module')
def add(a, b):
    print(a + b)


@new_tips('sub_module')
def sub(a, b):
    print(a - b)


print(add(4, 5))
print(sub(5, 4))
