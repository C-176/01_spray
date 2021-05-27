# requests模块：模拟浏览器发请求
import requests

if __name__ == "__main__":
    url='https://jingyan.baidu.com/article/7c6fb428d84f9480642c90d1.html'
    response = requests.get(url=url)
    page_text = response.text
    print(page_text)
    with open('qingning.html', 'w', encoding='utf-8') as fp:
        fp.write(page_text)
    print('爬取数据结束！')