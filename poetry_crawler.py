import requests
from bs4 import BeautifulSoup
import re

url = 'https://so.gushiwen.org/mingju/default.aspx?p=%d&c=&t='
ua = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'
max_page = 10


def fetch_data(page):
    headers = {
        'user-agent': ua
    }
    data = requests.get(url % page, headers=headers).content
    return data


def parse_data(page_data):
    sentences = []
    authors = []
    soup = BeautifulSoup(page_data, 'lxml')
    reg1 = r'/mingju/juv_.*?.aspx'
    rs1 = soup.find_all('a', attrs={'href': re.compile(reg1)})
    for ss in rs1:
        sentences.append(ss.get_text())

    reg2 = r'/shiwenv.*?.aspx'
    rs2 = soup.find_all('a', attrs={'href': re.compile(reg2)})
    for au in rs2:
        authors.append(au.get_text())
    # zip operator
    data = zip(sentences, authors)
    poetry = []
    for datum in list(data):
        poetry.append('%s --- %s' % datum)
    return poetry


def main():
    data = []
    for i in (0, max_page):
        datum = parse_data(fetch_data(i))
        data += datum
    with open('poetry.txt', 'w', encoding='utf-8') as f:
        for i in data:
            f.write('%s\n' % i)


if __name__ == '__main__':
    main()
