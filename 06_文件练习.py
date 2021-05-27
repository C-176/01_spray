import requests
from bs4 import BeautifulSoup

url = 'https://tech.sina.com.cn/digi/2020-07-02/doc-iirczymm0117113.shtml'
req = requests.get(url=url)
req.encoding = 'utf-8'
bs = BeautifulSoup(req.text, 'lxml')
texts = bs.find_all('p')
for i in texts:
    if i is None:
        continue
    else:
        i_text = str(i.string)
        print(i_text)

        with open('file1.txt', 'wt', encoding='utf-8') as fl:
            fl.writelines(i_text)
