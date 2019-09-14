# encoding:utf-8
# 类与示例

# 不使用类
# user1 = {'name': 'tom', 'hp': 100}
# user2 = {'name': 'jerry', 'hp': 80}
#
#
# def print_role(rolename):
#     print('name is %s  ,hp is %s' % (rolename['name'], rolename['hp']))
#
#
# print_role(user1)


class Player():  # 定义一个类
    def __init__(self, name, hp):
        self.name = name  # 变量被称作属性
        self.hp = hp

    def print_role(self):  # 定义一个方法
        print('%s: %s' % (self.name, self.hp))


user1 = Player('tom', 100)  #类的实例化
user1.print_role()
