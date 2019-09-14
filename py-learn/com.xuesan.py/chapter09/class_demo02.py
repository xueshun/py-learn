# encoding:utf-8
# 如何增加类的属性与方法
# 类的封装


class Player():  # 定义一个类
    def __init__(self, name, hp, occu):
        self.__name = name  # 变量被称作属性
        self.hp = hp
        self.occu = occu

    def print_role(self):  # 定义一个方法
        print('%s: %s %s ' % (self.__name, self.hp, self.occu))

    def updateName(self, newName):
        self.__name = newName


user1 = Player('tom', 100, 'war')
user1.print_role()
# 使用upateName 修改user1的名称概念
user1.updateName('joker')
user1.print_role()
# 使用这个更改user1的name
user1.name = 'lina'
user1.print_role()
# 将name 改为__name，就不能修改，称之为类的封装
