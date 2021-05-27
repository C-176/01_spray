import requests
keyword = input('请输入要搜索的关键字词：')
for index in range(11):
    url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=keyword'
    data = {
    'cname': '',
    'pid': '',
    'keyword': keyword,
    'pageIndex': index,
    'pageSize': 10
    }
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36 Edg/90.0.818.66'
                   }

    response = requests.post(url, data, headers=headers)
    get_text = response.text
    null = ''
    get_dict = eval(get_text)
    data1_list = list(get_dict.values())
    data2_list = data1_list[1]
    for i in data2_list:
        data3_list = list(i.values())
        for index in range(6):
            print(data3_list[index], end='\t')
        print('')


