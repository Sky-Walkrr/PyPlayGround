import requests
import time
import re

url = 'https://cn.bing.com'
time_stamp = time.strftime('%Y-%m-%d-%H-%M-%S')

def main():
    data = requests.get(url)
    content = data.text
    reg = r'(/az/hprichbg/rb/.*?.jpg)'
    matched = re.search(reg, content)
    full_url = 'https://cn.bing.com' + matched.group()
    print(full_url)
    img_data = requests.get(full_url)
    # 文件读写操作
    # try:
    #     f = open('%s.jpg' % time_stamp, 'wb')
    #     f.write(img_data.content)
    # finally:
    #     if f:
    #         f.close()

    # 使用with语句，不必调用close，代码更简洁
    with open('%s.jpg' % time_stamp, 'wb') as f:
        f.write(img_data.content)


if __name__ == '__main__':
    main()

