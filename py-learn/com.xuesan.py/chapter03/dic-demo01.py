# 使用字典存储
chinese_zodiac = '猴鸡狗猪鼠牛虎兔龙蛇马羊'

zodiac_name = (u'摩羯座', u'水瓶座', u'双鱼座', u'白羊座', u'金牛座', u'双子座', u'巨蟹座', u'狮子座', u'处女座', u'天秤座',
               u'天蝎座', u'射手座')

zodiac_days = ((1, 20), (2, 19), (3, 21), (4, 21), (5, 21), (6, 22),
               (7, 23), (8, 23), (9, 23), (10, 23), (11, 23), (12, 23))

# 年份字典初始化
cz_num = {}
for i in chinese_zodiac:
    cz_num[i] = 0

# 星座字典初始化
zn_num = {}
for i in zodiac_name:
    zn_num[i] = 0

while True:
    # 用户输入出生年月和日期
    year = int(input("请输入年份："))
    month = int(input("请输入月份："))
    day = int(input("请输入日期："))

    # 计算生肖
    n = 0
    while zodiac_days[n] < (month, day):
        if month == 12 and day > 25:
            break
        n += 1

    # 输出星座
    print(zodiac_name[n])

    # 输出生肖
    print("%s 年的生肖是 %s " % (year, chinese_zodiac[year % 12]))

    # 存入字典
    cz_num[chinese_zodiac[year % 12]] += 1
    zn_num[zodiac_name[n]] += 1

    # 输出字典内容
    for each_key in cz_num.keys():
        print('生肖 %s 有 %d 个' % (each_key, cz_num[each_key]))

    for each_key in zn_num.keys():
        print('星座 %s 有 %d 个' % (each_key, zn_num[each_key]))
