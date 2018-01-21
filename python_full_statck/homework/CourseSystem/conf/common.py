import os
import pickle
import random
from conf import settings

def checkIn(choice, menu_dic):
    if choice in menu_dic:
        menu_dic[choice]()
    else:
        print('invaild input')


def get_list(cls_base_dir):
    List = []
    for i in os.listdir(cls_base_dir):
        if '.py' in i:
            continue
        db_path = os.path.join(cls_base_dir, i)
        with open(db_path, 'rb') as f:
            sample = pickle.load(f)
        List.append(sample)
    return List

# 用此函数表示学习内容
def study_content():
    s = ''
    for i in range(6):
        num = str(random.randint(0, 9))
        alf1 = chr(random.randint(65, 90))
        alf2 = chr(random.randint(97, 122))
        s += random.choice([num, alf1, alf2])
    return s