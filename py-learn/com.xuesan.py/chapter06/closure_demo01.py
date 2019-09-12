# encoding:utf-8
# 闭包 外部函数变量被内部函数引用，称之为‘闭包’


def func():
    num1 = 1
    num2 = 2
    print(num1 + num2)


func()


def sum(a):
    def add(b):
        print(a + b)

    return add


# add 函数名称或函数的引用
# add() 函数的调用
num1 = func()
num2 = sum(2)

# 查看函数返回类型
print(type(num1))
print(type(num2))
print(num2(4))
