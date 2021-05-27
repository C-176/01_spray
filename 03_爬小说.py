# # requests模块：模拟浏览器发请求
import requests
from tqdm import tqdm
from bs4 import BeautifulSoup


def get_content(target):
    response = requests.get(url=target)
    response.encoding = 'utf-8'
    bs = BeautifulSoup(response.text, 'lxml')
    texts = bs.find('div', id='content')
    content = texts.text.strip().split('\xa0' * 4)
    return content

    # with open('./xiaoshuo.html', 'w', encoding='utf-8') as fp:
    #     fp.write(str(page_text))


if __name__ == "__main__":
    server = 'https://www.xsbiquge.com'
    book_name = '诡秘之主.txt'
    url = 'https://www.xsbiquge.com/15_15338/'
    response1 = requests.get(url=url)
    response1.encoding = 'utf-8'
    bs1 = BeautifulSoup(response1.text, 'lxml')
    texts1 = bs1.find('div', id='list')
    chapters = texts1.find_all('a')
    for chapter in tqdm(chapters):
        target = server + chapter.get('href')
        chapter_name = chapter.string
        content = get_content(target)
        with open(book_name, 'a', encoding='utf-8') as f:
            f.write(chapter_name)
            f.write('\n')
            f.write('\n'.join(content))
            f.write('\n')
