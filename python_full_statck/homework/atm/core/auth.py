import json
import os
from core import db_handler
from conf import settings
from core import logger
def auth():
    retry_count = 0
    while retry_count < 3:
        account = input('>>account:')
        password = input('>>passwd:')
        path1 = db_handler.db_handler(settings.DATABASE)
        account_file = os.path.join(path1, 'accounts', account + '.json')
        if os.path.exists(account_file):
            account_data = json.load(open(account_file))

            if password == account_data['password']:
                print('login succssful')
                return account_data
            else:
                print('account or password wrong')
                retry_count += 1
        else:
            print('the account no exist')
            retry_count += 1
    else:
        print('you has try three times,try it later')
        exit()


def acc_login(user_data, logger):
    account_data = auth()
    user_data['account_id'] = account_data['id']
    user_data['is_authenticated'] = True
    user_data['account_data'] = account_data
    logger.info('%s login succssful' % account_data['id'])
    return (True, account_data)