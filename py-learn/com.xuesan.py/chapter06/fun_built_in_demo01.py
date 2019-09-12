# encoding:utf-8
# 内建函数 list map reduce zip
# 查看帮助可以使用help()函数 例：help(list)
from functools import reduce

# list
a = [1, 2, 3, 4, 5, 6]
print("list--------------")
# 输入数组中大于2的元素
print(filter(lambda x: x > 2, a))
print(list(filter(lambda x: x > 2, a)))

# map
# 使用help(map)查看，如果有_iter_这个方法，说明这个对象可以使用for in
b = [1, 2, 3, 4, 5]
print("map--------------")
# print(map(lambda x: x, a))
print(list(map(lambda x: x, b)))
# 将map中每个元素都加1
print(list(map(lambda x: x + 1, b)))
# 将数组中对应位置的数据相加
print(list(map(lambda x, y: x + y, a, b)))

# reduce
# reduce 需要引入 from functools import reduce
print("reduce--------------")
# (((1+2)+3)+4)
print(reduce(lambda x, y: x + y, [2, 3, 4], 1))
print(reduce(lambda x, y: x * y, [2, 3, 4], 1))

# zip 笛卡尔积
print('zip-----------------')
for i in zip((1, 2, 3), (4, 5, 6)):
    print(i)
