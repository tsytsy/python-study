'选课：老师，课程，学生'
'''
老师有性别，年龄，课程，学生数据属性，有教学函数属性
学生有性别，年龄，课程属性，有学习函数属性
课程有课程名，课程价格，课程周期数据属性，有更新函数属性
'''


class People:
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex
        self.course = []


class Teacher(People):
    def __init__(self, name, age, sex, job_title):
        super(Teacher, self).__init__(name, age, sex)
        self.job_title = job_title
        self.student = []

    def teach(self):
        print('%s is teacher' % self.name)


class Student(People):
    def study(self):
        print('study')


class Course:
    def __init__(self, name, price, period):
        self.name = name
        self.price = price
        self.period = period

    def update(self):
        print('course update')


s1 = Student('tsy', 21, 'male')
s2 = Student('lyt', 21, 'female')
t1 = Teacher('eggon', 31, 'male', 'profersson')
c1 = Course('Python', 7000, '4m')
s1.course.append(c1)
s2.course.append(c1)
t1.course.append(c1)
t1.student.append(s1)
t1.student.append(s2)
for i in t1.student:
    print(i.name)
print(s1.course[0].name)




