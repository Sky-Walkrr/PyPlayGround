import requests
from bs4 import BeautifulSoup
import pymysql

target_url = 'https://www.zhihu.com/explore/recommendations'
config = {
    'host': '127.0.0.1',
    'port': 3306,
    'user': 'root',
    'password': '123456',
    'charset': 'utf8mb4'
}
conn = pymysql.connect(**config)


def load_page(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36',
        # 'Connection': 'Close'
    }
    return requests.get(url, headers=headers).content


def parse_page(page):
    # soup = BeautifulSoup(page, 'html.parser')
    soup = BeautifulSoup(page, 'lxml')
    # print(soup.prettify())
    items = soup.find_all('div', attrs={'class': 'zm-item'})
    cursor = conn.cursor()

    for item in items:
        title = item.find('a', attrs={'data-za-element-name': 'Title'}).get_text()
        upvote = item.find('div', attrs={'class': 'zm-item-vote'}).a.get_text()
        comment = item.find('div', attrs={'class': 'zm-meta-panel'}).find('a', attrs={'class': 'meta-item toggle-comment js-toggleCommentBox'}).get_text()
        title = remove_carriage_return_sign(title)
        upvote = remove_carriage_return_sign(upvote)
        comment_text = remove_carriage_return_sign(comment)
        if comment_text == '添加评论':
            comment_text = '0条评论'
        comment = comment_text
        v = title, upvote, comment
        cursor.execute('insert into zhihu(title, upvote_count, comment_count) value(%s, %s, %s)', v)


def init_db():
    # conn = pymysql.connect(**config)
    conn.autocommit(1)
    cursor = conn.cursor()
    db_name = 'test'
    table_name = 'zhihu'
    cursor.execute('create database if not exists %s' % db_name)
    conn.select_db(db_name)
    cursor.execute('create table if not exists %s(id INT AUTO_INCREMENT NOT NULL, title VARCHAR(128), upvote_count VARCHAR(30), comment_count VARCHAR(30), primary key (id))' % table_name)


def main():
    init_db()
    data = load_page(target_url)
    parse_page(data)


def remove_carriage_return_sign(text):
    return text.replace('\n', '')


if __name__ == '__main__':
    main()
