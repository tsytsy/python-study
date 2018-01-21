from conf import common
from conf import settings
from models import student_cls
import os
import pickle
import random
import sys

class student_view:
    def __init__(self):
        self.student_obj = None   # 登录成功后会得到学生对象
        self.all_course_list = common.get_list(settings.COURSE_DIR)
        self.student_list = common.get_list(settings.STUDENT_DIR)
        print(self.student_list)
        self.welcome()


    def welcome(self):
        menu = '''
        1. 注册
        2. 登录
        b. 返回上一层
        '''
        menu_dic = {
            '1': self.register,
            '2': self.login,
        }
        back_flag = False
        while not back_flag:
            print(menu)
            choice = input('input your choice:')
            if choice == 'b':
                back_flag = True
                continue
            common.checkIn(choice, menu_dic)

    def register(self):
        flag = False
        while not flag:
            name = input('register name:')
            passwd = input('passwd:')
            sex = input('sex:')
            age = input('age:')
            if name in self.student_list:
                print('account exist, try another name')
                continue
            student_db_path = os.path.join(settings.STUDENT_DIR, name)
            with open(student_db_path, 'wb') as f:
                pickle.dump(student_cls.student(name, passwd, sex, age), f)
            flag = True

    def login(self):
        print('login')
        retry = 0
        flag = False
        while retry < 3 and not flag:
            name = input('>>name:')
            passwd = input('>>passwd:')
            if name not in os.listdir(settings.STUDENT_DIR):
                # print(self.admin_list)
                print('account no exist')
                continue
            db_path = os.path.join(settings.STUDENT_DIR, name)
            with open(db_path, 'rb') as f:
                student_obj = pickle.loads(f.read())
            if name == student_obj.name and passwd == student_obj.passwd:
                print('login succssful')
                self.student_obj = student_obj
                self.menu_func()
                flag = True
            else:
                print('account or passwd wrong')
                retry += 1
                if retry == 3:
                    print('you have try three times, try it later')

    def menu_func(self):
        menu = '''
            1. 上课
            2. 选课
            3. 查看上课记录
            4. 查看已选课程
            5. 评价

            '''
        menu_dic = {
            '1': self.study,
            '2': self.course_select,
            '3': self.search_studyrecord,
            '4': self.search_course,
            '5': self.evaluate_teacher
        }
        back_flag = False
        while not back_flag:
            print(menu)
            choice = input('choice:')
            if choice == 'b':
                back_flag = True
                continue
            common.checkIn(choice, menu_dic)

    def study(self):
        print('you have choose these course:')
        for i in self.student_obj.course:
            print(i.name, end='\t')
        print('\n')
        while True:
            choice = input('input the course name you want to study:')
            if choice == 'b':
                return
            for i in self.student_obj.course:
                if choice == i.name:
                    study_course = i
                    break

            else:
                print('invaild input')
                continue
            break
        study_data = input('input your study data(like 2017-1-1):')
        course_teacher = study_course.teacher.name
        study_content = common.study_content()
        self.student_obj.studyrecord[study_course.name] = list([study_data, course_teacher, study_content])
        student_db_path = os.path.join(settings.STUDENT_DIR, self.student_obj.name)
        with open(student_db_path, 'wb') as f:
            pickle.dump(self.student_obj, f)


    def course_select(self):
        print('name  price  period teacher')
        name = []
        for c in self.all_course_list:
            # print('{} {} {}'.format([t.name, t.sex, t.age]))
            print('%s %s %s %s' % (c.name, c.price, c.period, c.teacher.name))
            name.append(c.name)

        while True:
            choice = input('which course you choose(name):')
            if choice not in name:
                print('input wrong, please input course name')
                continue
            db_path = os.path.join(settings.COURSE_DIR, choice)
            with open(db_path, 'rb') as f:
                course = pickle.load(f)
            break
        self.student_obj.course.append(course)
        student_db_path = os.path.join(settings.STUDENT_DIR, self.student_obj.name)
        with open(student_db_path, 'wb') as f:
            pickle.dump(self.student_obj, f)

    def search_studyrecord(self):
        d = self.student_obj.studyrecord
        print('these are study record:')
        print('{:<18}\t{:<18}\t{:<18}\t{:<18}'.format('course_name', 'study_data', 'course_teacher', 'course_content'))
        for i in self.student_obj.studyrecord:
            print('{:<18}\t{:<18}\t{:<18}\t{:<18}'.format(i, d[i][0], d[i][1], d[i][2]))

    def search_course(self):
        print('I have choose these course:')
        for i in self.student_obj.course:
            print(i.name, i.price, i.period, i.teacher.name)

    def evaluate_teacher(self):
        print('these your course teacher:')
        for i in self.student_obj.course:
            print(i.teacher.name)
        teacher_name = input('input teahcer name and evaluate he/she:')
        level = ['S', 'A', 'B', 'C', 'D']
        for i in level:
            print(i, end='\t')
        print('\n')
        while True:
            teacher_level = input('the teacher score:')
            if teacher_level not in level:
                print('invaild input')
                continue
            break
        if teacher_level in ['C', 'D']:
            teacher_db_path = os.path.join(settings.TEACHER_DIR, teacher_name)
            with open(teacher_db_path, 'rb') as f:
                t = pickle.load(f)
            t.salary = str(int(t.salary) - 50)
            print(t.salary)
            with open(teacher_db_path, 'wb') as f:
                pickle.dump(t, f)

