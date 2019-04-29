class ClassA(object):
    num = 1
    dic = {'key1':'value1','key2':'value2'}
    def __init__(self,name):
        self.name = name
    def value1(self):
        print('this is value1')
    def value2(self):
        print('this is value2')
    def normal_method(self,m):
        print(m*3)
    @classmethod
    def cls_method(cls):
         print('this is classmethod')
    @staticmethod
    def static_method(value):
        print('this is staticmethod','this is input value:'+value)

#获取类静态属性、类方法、静态方法
if hasattr(ClassA,'num'):
    print(ClassA.num)
if hasattr(ClassA,'cls_method'):
    f = getattr(ClassA,'cls_method')
    f()
if hasattr(ClassA,'static_method'):
    f1 = getattr(ClassA,'static_method')
    f1('input_value')
#获取实例属性、实例方法
c = ClassA('c_er')
c.age = 18
if hasattr(c,'age'):
    a = getattr(c,'age')
    print(a)
if hasattr(c,'__init__'):
    print(c.name)
if hasattr(c,'normal_method'):
    f2 = getattr(c,'normal_method')
    f2('three ')
#
for k in ClassA.dic:
    print(k)
key = input('please input one key:')
if hasattr(c,c.dic[key]):
    f3 = getattr(c,c.dic[key])
    f3()
