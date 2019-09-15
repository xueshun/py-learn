# encoding:utf-8
# with调用类
# 自定义with语句 包含__enter__ 和 __exit__ 方法
# 使用with方式，可以省去对异常的抓取
class TestWith(object):
    def __enter__(self):
        print('run now')

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_tb is None:
            print('exit normal')
        else:
            print('exit wit exception %s' % exc_tb)


with TestWith():
    print('test')
    raise NameError('Exception')
