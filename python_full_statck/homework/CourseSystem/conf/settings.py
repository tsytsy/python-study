import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, BASE_DIR)

ADMIN_DIR = os.path.join(BASE_DIR, 'db', 'admin_db')
STUDENT_DIR = os.path.join(BASE_DIR, 'db', 'student_db')
TEACHER_DIR = os.path.join(BASE_DIR, 'db', 'teacher_db')
COURSE_DIR = os.path.join(BASE_DIR, 'db', 'course_db')