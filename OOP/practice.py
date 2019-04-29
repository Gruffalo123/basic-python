class Student(object):
    def __init__(self,name,gender):
        self.__name = name
        self.__gender = gender
    def get_gender(self):
        return self.__gender
    def set_gender(self,gender):
        self.__gender = gender

li = Student('libai','male')
if li.get_gender() != 'male':
    print('测试失败！')
else:
    li.set_gender('female')
    if li.get_gender() != 'female':
        print('测试失败！')
    else:
        print('测试成功!')
