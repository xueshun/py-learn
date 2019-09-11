# 文件的基本操作
# 写入
file1 = open('name.txt', 'w')
file1.write('诸葛亮')
file1.close()

# 读入
file2 = open('name.txt')
print(file2.read())
file2.close()

# 追加
file3 = open('name.txt', 'a')
file3.write('刘备')
file3.close()
