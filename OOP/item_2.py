class A(object):
    def __init__(self,start=0,step=1):
        print('call function __init__')
        self.start = start
        self.step = step
        self.mydata = {}
    #定义获取值的方法
    def __getitem__(self, item):
        print('call function __getitem__')
        try:
            return self.mydata[item]
        except KeyError:
            return 'no such key'
    #定义赋值方法
    def __setitem__(self, key, value):
        print('call function __setitem__')
        self.mydata[key] = value
    #定义删除元素的方法
    def __delitem__(self, key):
        print('call function __delitem__')
        del self.mydata[key]

a = A(1,2)
print(a[3])# 这里应该执行 'no such key'，因为没有3这个key
a[3] = 'value3'# 进行赋值
print(a[3])# 前面进行了赋值，那么直接输出赋的值 value3
del a[3]# 删除3这个key
print(a[3])
