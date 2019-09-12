# encoding:UTF-8
# lambda表达式

# def true():
#     return True
#
#
# def true1(): return True
#
#
# lambda: True

# def add(x, y):
#     return x + y
#
#
# print(add(1, 2))

# add = lambda x, y: x + y
#
# print(add(1, 2))

def make_repeater(n):
    return lambda s: s * n


twice = make_repeater(2)

print(twice('word'))
print(twice(5))
