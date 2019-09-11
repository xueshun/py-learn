# # 读取文件中一行数据
# file1 = open('name.txt')
# print(file1.readline())
# file1.close()
#
# # 逐行处理
# file2 = open('name.txt')
# for line in file2.readlines():
#     print(line)
#     print('----')
#

file3 = open('name.txt', 'r')
# 文件指针
# print(file3.tell())
# file3.read(1)
# print(file3.tell())
# file3.seek(0)
# print(file3.tell())

# 第一个参数代表偏移位置，第二个参数 0：表示从文件开头偏移，1：表示从当前位置偏移；2：从文件结尾
# print('当前指针位置 %d' % file3.tell())
# print('当读取第一个字符，字符的内容是%s' % file3.read(1))
# print('当前指针位置 %d' % file3.tell())
# print('进行seek(0)操作')
# file3.seek(0)
# print('当前指针位置 %d' % file3.tell())
# print('当读取第五个字符，字符的内容是%s' % file3.read(5))
# # print('进行seek(2,0)操作')
# # file3.seek(2, 0)
# # print('当前指针位置 %d' % file3.tell())
# print('进行seek(2,1)操作')
# file3.seek(2, 2)
# print('当前指针位置 %d' % file3.tell())
# file3.close()

# 测试seek(p,0)和seek(p)
# print("文件当前读取到的字符%s" % file3.read(2))
# print("文件当前指针%d" % file3.tell())
# #file3.seek(0)
# file3.seek(1,0)
# print("进行seek()操作之后，文件指针位置%d" % file3.tell())

# 测试seek(p,1) ??
file3.seek(2, 1)
print("文件当前读取到的字符%s" % file3.read(2))
print("文件当前指针%d" % file3.tell())
print("进行seek(0, 2)操作之后，文件指针位置%d" % file3.tell())
