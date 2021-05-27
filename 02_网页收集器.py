# requests模块：模拟浏览器发请求


import requests
from bs4 import BeautifulSoup

if __name__ == "__main__":
    kw = input('请输入要搜索的信息：')
    url = 'https://cn.bing.com/search?q=%s' % kw
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36 Edg/90.0.818.66'
               }
    response = requests.get(url=url, headers=headers)
    response.encoding = 'utf-8'
    # bs = BeautifulSoup(response.text, 'lxml')
    page_text = response.text

    # print(page_text)
    filename = kw + '.html'
    with open(filename, 'w', encoding='utf-8') as fp:
        fp.write(page_text)
    print('爬取数据结束！')