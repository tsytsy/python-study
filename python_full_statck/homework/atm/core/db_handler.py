# 将DATABASE信息传给conn_parms
def db_handler(con_parms):
    if con_parms['engine'] == 'file_storage':
        return file_db_handler(con_parms)


def file_db_handler(con_parms):
    return con_parms['path']