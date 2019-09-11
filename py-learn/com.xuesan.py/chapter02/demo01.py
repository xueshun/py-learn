# 条件与循环

x = 'abc'

if x == 'abc':
    print('x的值与abc相等')

if x == 'abc':
    print('111')
else:
    print('222')

if x == 'abc':
    print('111')
elif x == 'bcc':
    print('222')
else:
    print('333')

chinese_zodiac = '猴鸡狗猪鼠牛虎兔龙蛇马羊'

year = int(input('请用户输入出生年份'))

if chinese_zodiac[year % 12] == '狗':
    print('狗年的运势：')

print(chinese_zodiac[year % 12])
