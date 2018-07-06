from openpyxl import load_workbook
import pymysql

config = {
    'host': '127.0.0.1',
    'port': 3306,
    'user': 'root',
    'password': '123456',
    'charset': 'utf8mb4'
}


def xls2db():
    conn = pymysql.connect(**config)  # double asterisk

    conn.autocommit(1)
    cursor = conn.cursor()
    db_name = 'test'
    cursor.execute('create database if not exists %s' % db_name)
    conn.select_db(db_name)

    table_name = 'movie'
    # sql syntax, be aware of reserved words!
    cursor.execute(
        'create table if not exists %s(id MEDIUMINT not null auto_increment,movie_name varchar(64),rank_value varchar(64),primary key(id))' % table_name)

    wb = load_workbook('电影.xlsx')
    wx = wb.get_sheet_names
    for row in wb:
        print('read row...')
        for cell in row:
            # get cell value
            v = (cell[0].value, cell[2].value)
            # string format
            cursor.execute('insert into movie(movie_name, rank_value) value(%s,%s)', v)
    print('finished')


if __name__ == '__main__':
    xls2db()

