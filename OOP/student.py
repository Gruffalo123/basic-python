class Student(object):
    def __init__(self,name,score):
        self.name = name
        self.score = score
    def print_score(self):
        print('{}的成绩是:{}'.format(self.name, self.score))

    def get_grade(self):
        if self.score >= 90:
            return 'A'
        elif self.score >= 60:
            return 'B'
        else:
            return 'C'
wang = Student('WangDong',92)
liang = Student('LiangMeng',46)

wang.print_score()

print(wang.name,wang.get_grade())
print(liang.name,liang.get_grade())
