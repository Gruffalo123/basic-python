class Foo(object):
    def __init__(self,name):
        self.name = name
    def __getitem__(self, item):
        print('call function __getitem__')
        return self.__dict__[item]
    def __setitem__(self, key, value):
        print('call function __setitem__')
        self.__dict__[key] = value
    def __delitem__(self, key):
        print('call function __delitem__')
        del self.__dict__[key]

f = Foo('libai')
print(f['name'])
f['gender'] = 'male'#新增一个Key
print(f['gender'])
f['gender'] = 'female'#重新赋值
print(f['gender'])
del f['gender']#删除了key
print(f['gender'])#引发异常
