# encoding:utf-8
# 上下文

# 未使用上下文，需要抓取异常
# fd = open('name.txt', encoding='UTF-8')
# try:
#     for line in fd:
#         print(line)
# except Exception as e:
#     print(e)
# finally:
#     fd.close()

# 使用上下文，with会自动抓取异常

with open('name.txt', encoding='utf-8') as f:
    for line in f:
        print(line)
