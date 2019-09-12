# encoding:utf-8
# 闭包函数，相对于普通函数。
#       闭包函数       普通函数
#       传递函数       传递参数

# a * x + b = y
# def a_line(a, b):
#     def arg_y(x):
#         return a * x + b
#
#     return arg_y

# 使用lambda

def a_line(a, b):
    return lambda x: a * x + b


line1 = a_line(3, 5)
line2 = a_line(4, 6)
print(line1(10))
print(line2(10))
