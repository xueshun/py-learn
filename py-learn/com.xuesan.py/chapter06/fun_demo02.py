# encoding:UTF-8
# 函数使用
# 通过文件操作读取并匹配相关文字出现的次数
import re


def find_item(char):
    with open('sanguo_utf8.txt', encoding='UTF-8') as f:
        data = f.read().replace('\n', '')
        name_num = re.findall(char, data)
        # print('主角 %s  出现 %s  次' %(hero, len(name_num)))

    return char, len(name_num)


# 读取人物的信息
name_dict = {}
with open('name.txt', encoding='UTF-8') as f:
    for line in f:
        names = line.split('|')
        for n in names:
            char_name, char_num = find_item(n)
            name_dict[char_name] = char_num

# 读取武器的信息
weapon_dict = {}
with open('weapon.txt', encoding='UTF-8') as f:
    i = 1
    for line in f:
        if i % 2 == 1:
            weapon_name, weapon_number = find_item(line.strip())
            weapon_dict[weapon_name] = weapon_number
        i += 1

name_sorted = sorted(name_dict.items(), key=lambda item: item[1], reverse=True)
print(name_sorted[0:10])

weapon_sorted = sorted(weapon_dict.items(), key=lambda item: item[1], reverse=True)
print(weapon_sorted[0:10])
