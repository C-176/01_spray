import requests
import re
from tqdm import tqdm
from bs4 import BeautifulSoup


def get_content(target):
    passage = requests.get(url=target)
    passage.encoding = 'utf-8'
    bs = BeautifulSoup(passage.text, 'lxml')
    texts = bs.find('div', id='content')
    texts = texts.text.split('\xa0' * 4)
    return texts


headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36 Edg/90.0.818.66'
               }
book_name = '我真的不是科技巨星啊.txt'
server = 'https://www.book900.com'
target1 = 'https://www.book900.com/18_18803.html'


# 正则表达式
pattern1 = re.compile(r'\d{3}\s\w+')
pattern2 = re.compile(r'\d{3}')
pattern3 = re.compile(r'"\S*"')
pattern4 = re.compile(r'(?<=").*(?=")')
passage1 = requests.get(url=target1, headers=headers)
passage1.encoding = 'utf-8'
bs1 = BeautifulSoup(passage1.text, 'lxml')
texts1 = bs1.find('div', id='list')  # 获取章条
letter = texts1.find('div', id='newchapter')

chapters = texts1.find_all('a')  # 获取章网址与章名
chapters_list = list(chapters)



#
# for chapter in tqdm(chapters_list):  # 遍历获得网址与章名
gett = re.findall(pattern1, str(chapters))
gettt = re.findall(pattern2, str(gett))

for index, i in tqdm(list(enumerate(gettt, 0))):

    if int(i) > int(gettt[index+1]) and int(index) != 392:
        continue

    getttt = re.findall(pattern3, str(chapters_list[index]))
    # target_back = getttt  # 网址
    gatt1 = re.findall(pattern4, str(getttt[0]))

    target = server + str(gatt1[0])  # 网址
    chapter_name = chapters_list[index].string  # 章名
    # print(chapter_name)
    content = get_content(target)  # 调用函数获得内容

    with open(book_name, 'a', encoding='utf-8') as f:
        f.write('*'*50)
        f.write('\n')
        f.write(chapter_name)
        f.write('\n')
        f.write('*' * 50)
        f.write('\n')
        f.write('*' * 50)
        f.write('\n'.join(content))
        f.write('\n')
        f.write('*'*50)
        f.write('\n')
# print('')