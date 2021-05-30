import requests
from lxml import etree
import tqdm

# 网页url,可更改index_的索引值获取多个界面
# 1：风景  6：美女  9：科幻
page_url = 'https://bizhi.ijinshan.com/1/index_1.shtml'

# UA
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/90.0.4430.212 Safari/537.36 Edg/90.0.818.66',
}
# 获取图片下载地址
page_get = requests.get(page_url, headers).text
page_get.encode(encoding='utf-8')

page_tree = etree.HTML(page_get)
pic_url_list = page_tree.xpath('.//div[@class="wallpaper-item "]//button/@data-src')
for index, url in tqdm.tqdm(zip(range(1, len(pic_url_list)+1), pic_url_list)):
    pic = requests.get(url, headers=headers).content
    pic_name = str(index)+'.jpg'
    with open(r'./4K壁纸/%s' % pic_name, 'wb') as file:
        file.write(pic)
print('下载完毕!')