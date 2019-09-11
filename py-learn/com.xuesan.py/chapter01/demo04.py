# 记录生肖，根据年份判断生肖

chinese_zodiac = '猴鸡狗猪鼠牛虎兔龙蛇马羊'

year = 2018

print(year % 12)

print(chinese_zodiac[2018 % 12])

# 序列的基本操作
# 成员关系操作符（in、not in）; 连接操作符（+）；重复操作符（*）；切片操作（[:]）

print('狗' in chinese_zodiac)
print('猫' in chinese_zodiac)

print(chinese_zodiac + chinese_zodiac)

print(chinese_zodiac*3)

print(chinese_zodiac[0:4])

