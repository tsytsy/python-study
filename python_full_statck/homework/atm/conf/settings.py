import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

LOG_TYPES = {
    'transaction': 'transactions.log',
    'access': 'access.log',
}

DATABASE = {
    'engine': 'file_storage', #support mysql,postgresql in the future
    'name': 'accounts',
    # 'path': "%s/db" % BASE_DIR,
    'path': os.path.join(BASE_DIR, 'db')
}