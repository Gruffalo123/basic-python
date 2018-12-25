class Student(object):
    def __init__(self,name,score):
        self.__name = name
        self.__score = score

    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score

    def set_score(self,score):
        if 0 <= score <= 100:
            self.__score = score
        else:
            raise ValueError('wrong score')

    def get_grade(self):
        if self.__score >= 90:
            return 'A'
        elif self.__score >= 60:
            return 'B'
        else:
            return 'C'

liang = Student('LiangMeng',46)
print(liang.get_name(),liang.get_score())
liang.set_score(88)
print(liang.get_name(),liang.get_score())
print('DO NOT use liang._Student__name:',liang._Student__name)
