from conf import common
from models import admin_cls
from models import teacher_cls
from models import course_cls
from conf import settings

import pickle
import os


class admin_view:
    def __init__(self):
        self.admin_list = os.listdir(settings.ADMIN_DIR)
        self.course_list = common.get_list(settings.COURSE_DIR)
        self.teacher_list = common.get_list(settings.TEACHER_DIR)
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
            # back_flag = True

    def register(self):
        flag = False
        while not flag:
            name = input('register name:')
            passwd = input('passwd:')
            sex = input('sex:')
            age = input('age:')
            if name in self.admin_list:
                print('account exist, try another name')
                continue
            admin_db_path = os.path.join(settings.ADMIN_DIR, name)
            with open(admin_db_path, 'wb') as f:
                pickle.dump(admin_cls.admin(name, passwd, sex, age), f)
            flag = True

    def login(self):
        print('login')
        retry = 0
        flag = False
        while retry < 3 and not flag:
            name = input('>>name:')
            passwd = input('>>passwd:')
            if name not in self.admin_list:
                print('account no exist')
                continue
            db_path = os.path.join(settings.ADMIN_DIR, name)
            with open(db_path, 'rb') as f:
                admin_obj = pickle.loads(f.read())
            if name == admin_obj.name and passwd == admin_obj.passwd:
                print('login succssful')
                self.menu_func()
                flag = True
            else:
                print('account or passwd wrong')
                retry += 1
                if retry == 3:
                    print('you have try three times, try it later')

    def menu_func(self):
            menu = '''
            1. 创建课程
            2. 创建老师
            3. 查看课程列表
            4. 查看老师列表
             
            '''
            menu_dic = {
                '1': self.create_course,
                '2': self.create_teacher,
                '3': self.search_courselist,
                '4': self.search_teacherlist,
            }
            back_flag = False
            while not back_flag:
                print(menu)
                choice = input('choice:')
                if choice == 'b':
                    back_flag = True
                    continue
                common.checkIn(choice, menu_dic)

    def create_course(self):
        course_name = input('input course name:')
        course_price = input('input course price:')
        course_period = input('input course period:')
        print('\nchoose teacher to teach the course:\n')
        self.search_teacherlist()
        name = []
        for t in self.teacher_list:
            name.append(t.name)
        while True:
            choice = input('which teacher you choose(name):')
            if choice not in name:
                print('input wrong, please input teacher name')
                continue
            db_path = os.path.join(settings.TEACHER_DIR, choice)
            with open(db_path, 'rb') as f:
                teacher = pickle.load(f)
            break

        c1 = course_cls.course(course_name, course_price, course_period, teacher)
        course_db_path = os.path.join(settings.COURSE_DIR, course_name)
        with open(course_db_path, 'wb') as f:
            pickle.dump(c1, f)

        teacher.course.append(c1)
        teacher_db_path = os.path.join(settings.TEACHER_DIR, teacher.name)
        with open(teacher_db_path, 'wb') as f:
            pickle.dump(teacher, f)
        self.course_list.append(c1)

    def create_teacher(self):
        name = input('name:')
        passwd = input('passwd')
        sex = input('sex:')
        age = input('age:')
        salary = input('salary:')
        if name in os.listdir(settings.TEACHER_DIR):
            print('teacher exist')
            return
        t = teacher_cls.teacher(name, passwd, sex, age, salary)
        teacher_db_path = os.path.join(settings.TEACHER_DIR, name)
        with open(teacher_db_path, 'wb') as f:
            pickle.dump(t, f)
        self.teacher_list.append(t)

    def search_courselist(self):
        print('name  price  period teacher')
        for c in self.course_list:
            print('%s %s %s %s' % (c.name, c.price, c.period, c.teacher.name))


    def search_teacherlist(self):
        print('name  sex  age')
        for t in self.teacher_list:
            print('%s %s %s' % (t.name, t.sex, t.age))
