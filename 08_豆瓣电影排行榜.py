from bs4 import BeautifulSoup as bs
import requests
import re
if __name__ == '__main__':

    # url
    ori_url = 'https://movie.douban.com/chart'
    Request_URL = 'https://movie.douban.com/j/chart/top_list'
    pattern1 = re.compile(r'(?<=type_name=).{,4}(?=&)')
    pattern2 = re.compile(r'(?<=;type=)\d{,2}(?=&amp)')
    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36 Edg/90.0.818.66'
    }
    theme_get = requests.get(url=ori_url, headers=headers)
    theme_get.encoding = 'utf-8'
    page_get = bs(theme_get.text, 'lxml')
    theme_get1 = page_get.find('div', class_="types")
    i_list = []
    j_list = []
    for i in theme_get1:
        if i == '\n':
            continue

        j = re.findall(pattern2, str(i))
        i = re.findall(pattern1, str(i))
        i_list.append(i[0])
        j_list.append(j[0])
    for index1 in range(len(i_list)):

        if index1 == (len(i_list)+1)/2:
            print(i_list[index1], j_list[index1], end='|')
            print('')
        print(i_list[index1], j_list[index1], end='|')
    print('\n')
    type = int(input('请选择想要查看的排行榜的电影类型：'))
    # 迭代器、合成器？
    # type_dict = {name: index for name, index in zip(i_list, j_list)}
    # print(type_dict)

    data = {
    'type': type,
    'interval_id': '100:90',
    'action':'',
    'start': 0,
    'limit': 100
    }
    pattern = re.compile(r"(?<=').*(?=')")
    response = requests.post(Request_URL, data=data, headers=headers)
    data1_list = response.json()
    for item in data1_list:
        item_dict = eval(str(item))
        data2_list = list(item_dict.values())
        with open('豆瓣百强喜剧.txt', 'a', encoding='utf-8') as file:
            for i in data2_list:
                file.writelines(str(i))
                file.writelines('\n')
        # print(data2_list)
        get_country = re.findall(pattern, str(data2_list[6]))
        print(data2_list[1], '\t片名:', data2_list[7], '\t', data2_list[6][0], '\t豆瓣评分：', data2_list[0][0])
        # print()
    # print(data_list)