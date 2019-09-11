# for 序列

chinese_zodiac = '猴鸡狗猪鼠牛虎兔龙蛇马羊'

for cz in chinese_zodiac:
    print(cz)

for i in range(13):
    print(i)

for i in range(1, 13):
    print(i)

for year in range(2000, 2019):
    print('%s 年的生肖是 %s' % (year, chinese_zodiac[year % 12]))
