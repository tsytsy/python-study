from core import admin_view
from core import student_view
from core import teacher_view
from conf import common
class start:
    def welcome(self):
        menu = '''
        1. 管理员视图
        2. 学生视图
        3. 老师视图
        q. 退出
        '''
        menu_dic = {
            '1': admin_view.admin_view,
            '2': student_view.student_view,
            '3': teacher_view.teacher_view,
            'q': exit
        }
        while True:
            print(menu)
            choice = input('choose your view:')
            common.checkIn(choice, menu_dic)
