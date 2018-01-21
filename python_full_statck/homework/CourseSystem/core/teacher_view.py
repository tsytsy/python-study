from conf import common
from conf import settings
from models import teacher_cls
import os
import pickle

class teacher_view:
    def __init__(self):
        self.teacher_obj = None
        self.welcome()
    def welcome(self):
        menu = '''
        1. 登录
        b. 返回上一层
        '''
        menu_dic = {
            '1': self.login,
        }
        back_flag = False
        while not back_flag:
            print(menu)
            choice = input('input your choice:')
            if choice == 'b':
                back_flag = True
                continue
            common.checkIn(choice, menu_dic)

    def login(self):
        print('login')
        retry = 0
        flag = False
        while retry < 3 and not flag:
            name = input('>>name:')
            passwd = input('>>passwd:')
            if name not in os.listdir(settings.TEACHER_DIR):
                # print(self.admin_list)
                print('account no exist')
                continue
            db_path = os.path.join(settings.TEACHER_DIR, name)
            with open(db_path, 'rb') as f:
                teacher_obj = pickle.loads(f.read())
            if name == teacher_obj.name and passwd == teacher_obj.passwd:
                print('login succssful')
                self.teacher_obj = teacher_obj
                self.menu_func()
                flag = True
            else:
                print('account or passwd wrong')
                retry += 1
                if retry == 3:
                    print('you have try three times, try it later')

    def menu_func(self):
        menu = '''
            1. 教课
            2. 查看课程列表
            3. 查看工资

            '''
        menu_dic = {
            '1': self.teach,
            '2': self.search_course,
            '3': self.search_salary,
        }
        back_flag = False
        while not back_flag:
            print(menu)
            choice = input('choice:')
            if choice == 'b':
                back_flag = True
                continue
            common.checkIn(choice, menu_dic)


    def teach(self):
        print('you teach these course:')
        name = []
        for i in self.teacher_obj.course:
            print(i.name, end='\t')
            name.append(i.name)
        print('\n')
        while True:
            choice = input('input the course name you teach:')
            if choice == 'b':
                return
            if choice not in name:
                print('invaild input')
                continue
            break
        num = int(self.teacher_obj.salary)
        money_for_course = 50
        new_salary = str(num + money_for_course)
        self.teacher_obj.salary = new_salary
        teacher_db_path = os.path.join(settings.TEACHER_DIR, self.teacher_obj.name)
        with open(teacher_db_path, 'wb') as f:
            pickle.dump(self.teacher_obj, f)

    def search_course(self):
        for i in self.teacher_obj.course:
            print(i.name)

    def search_salary(self):
        print(self.teacher_obj.salary)