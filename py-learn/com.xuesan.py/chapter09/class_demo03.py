# encoding:utf-8
# 类的继承

class Monster():
    '定义怪物类'

    def __init__(self, hp=100):
        self.hp = hp

    def run(self):
        print('移动到某个位置')

    def whoami(self):
        print('我是怪物父类')


class Animals(Monster):
    '普通怪物'

    def __init__(self, hp=10):
        super().__init__(hp)


class Boss(Monster):
    'Boss类怪物'

    def __init__(self, hp=1000):
        super().__init__(hp)

    def whoami(self):
        print('我是怪物我怕谁')


a1 = Monster(200)
print(a1.hp)
print(a1.run())
a2 = Animals(1)
print(a2.hp)
print(a2.run())

a3 = Boss(800)
a3.whoami()

# 查看类型
print('a1的类型 %s' % type(a1))
print('a2的类型 %s' % type(a2))
print('a3的类型 %s' % type(a3))

# 查看a2是否为 Monster类型
print(isinstance(a2, Monster))
