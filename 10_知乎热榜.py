import requests
from bs4 import BeautifulSoup
import re
from tqdm import tqdm
from lxml import etree
import os

# url
page_url = 'https://www.zhihu.com/hot'
# UA
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/90.0.4430.212 Safari/537.36 Edg/90.0.818.66',
    'cookie': '_zap=b80751ce-69e2-4ab4-afbf-5c02797d1ef9; d_c0="ACAdOT0fAxOPTm_eq5lhv3ZBVBYAlzcKlaE=|1619407030"; '
              'Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1619411048,1619411638,1619447920,1619698366; '
              '_xsrf=EGGUwpmB70BXS1cWv7gGV2Q2bjk5ApXU; '
              'captcha_session_v2="2|1:0|10:1619958345|18:captcha_session_v2|88'
              ':cWdxaVZSbHZLbHRkUWZFWWpEYUZHZUthR0R5SG1aMG15NFIyOWsxc0tnS3FkbEUwU0RBTUZVQkhqc3h3Wmc4aQ'
              '==|3890179b47a3cf894c98075461a14d4511d9759156ee154cc996501ae4989516"; __snaker__id=e4r73ZDJKWyWwr4v; '
              '_9755xjdesxxd_=32; gdxidpyhxdE=zVZt%2BATkREbNgkXD4MNQJop69CbBAevknvkXIJrtAmoU9sAI2as%2B3ks1dxRo%5CKEKa'
              '%2Firql02zfv1%2Fy9jMgdXGMJd5NQuRu3O4D8%2Ba7UdT%2BMn2NVARHZG98CJM2YOAdqImfajS1bc%5CJluI'
              '%2FEocuYMGKwoGrEMK6Za0Vc3LXt2hWXI01rW%3A1619959251724; '
              'YD00517437729195%3AWM_NI=dke0wZfcSYptSDyulTbwYTfjEF2VyK%2FDTHsKcbeh0sYBz7pNuT0ni5sWzqFv3rbt%2FDfb3'
              '%2FGMH5FnnxrAsNk6196douF1sRamXkphKEX%2Bg%2FaOKwQ12K4Imz169pHfoDB6MUw%3D; '
              'YD00517437729195%3AWM_NIKE'
              '=9ca17ae2e6ffcda170e2e6eeaae95a8abd8e99d86da18a8aa7d44a829a9f84b63bf3b7a6b3cc3aa7b2a8aeb62af0fea7c3b92aa8b5abd1f652a6bd9dbaf380919cb796ef60a2a997b5e562879afeb7fc41ed9c9ca9f241a1beab89b3799b9eb6d8f346b78c008fec3fb189b692c57ef1aeae95ae50a6befdd0c6478ceb8a8fed74b29fbdafea3ef3e7fa85ee7f86efbdb3e4679cb5c089ca4f9cf5a9d0e44589a99fd2b141f897a39bb43efbb08887ee5082ea83b6f637e2a3; YD00517437729195%3AWM_TID=wYnPVG%2BS1UVEVQRABVJvwxy3VJjb3lcq; z_c0="2|1:0|10:1619958370|4:z_c0|92:Mi4xOFdrZUJ3QUFBQUFBSUIwNVBSOERFeWNBQUFDRUFsVk5ZaWUyWUFEeEVnOW1fcjZUOUhlc2Z1SmxuTXNkekN1OVVR|f0221e1866935990a630b9c75e2198219a46f9a03b62fdcf5371251f15b4778a"; q_c1=c84139982f394effb76a01367fc814cf|1621176151000|1621176151000; tst=h; tshl=; SESSIONID=zVwtWP0muFZMGXjTKMA9xkhI8Ztj73sy1kk4Nx7UttQ; JOID=V1wSAU9HFmcS1-axHEBWuGGU_rINPEMVYIG3gnQzUT5alr_aSy4ay3XX5LcfeR-N-sBfgtRnyoKW6dT_Br-qWXU=; osd=Ul0dBUtCF2gW0-OwE0RSvWCb-rYIPUwRZIS2jXA3VD9VkrvfSiEez3DW67MbfB6C_sRag9tjzoeX5tD7A76lXXE=; KLBRSID=e42bab774ac0012482937540873c03cf|1622084841|1622084200',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',

}
# Get请求
page_response = requests.get(page_url, headers=headers)
tree_text = etree.HTML(page_response.text)
# 准备列表存放标题与地址
# text_url_list = []
# title_list = []
title_list = tree_text.xpath('.//div[@class="HotList-list"]/section/div[@class="HotItem-content"]/a/@title')
text_url_list = tree_text.xpath('.//div[@class="HotList-list"]/section/div[@class="HotItem-content"]/a/@href')

for text_url, title in zip(text_url_list, title_list):
    print(text_url, title)
    with open('./知乎文章./排行榜.doc', 'at', encoding='utf-8') as file:
        file.write(text_url+' '+title+'\n')
        text_response = requests.get(url=text_url, headers=headers).text
        text_tree = etree.HTML(text_response)
        for Num in tqdm(range(1, 3)):
            text_list = text_tree.xpath('.//div[@class="List"]//div[@class="List-item"][%d]//div[@class="RichContent '
                                        'RichContent--unescapable"]//span[@class="RichText ztext '
                                        'CopyrightRichText-richText"]//text()' % Num)
            title = title.replace('?', "？")
            with open("./知乎文章/%s.doc" % title, 'at', encoding='utf-8') as fp:
                fp.truncate(0)
                fp.write(title+'\n')
                fp.write(str(Num) + '-.' * 20 + '\n')
                for index in range(len(text_list)):
                    fp.write(text_list[index]+'\n')
print('全部写入完毕')
