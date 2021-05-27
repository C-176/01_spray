import requests
import json
#TODO:句子翻译未完成
while True:
    print('1.单词翻译\
    2.句子翻译')
    choie = int(input('Make a choice:'))
    data_kw = input('请输入要查询的单词或句子:')
    if choie == 1:
        Request_URL = 'https://fanyi.baidu.com/sug'
        data = {'kw': data_kw}
    # 单词查询
    # url
    else:
        Request_URL = 'https://fanyi.baidu.com/v2transapi?from=zh&to=en'
        data = {'query': data_kw,
                'sign': '124092.329613',
                'token': 'cd0db23f18466694494d0b3d56c9f965'
                }

    # ug
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36 Edg/90.0.818.66'
    }
    response = requests.post(url=Request_URL, data=data, headers=headers)
    response_post = response.json()
    # print(response_post)

    file_name = data_kw + '.json'

    python = eval(json.dumps(response_post, ensure_ascii=False))
    strr = str(python.get('data'))
    if strr == str([]):
        print('未找到相关意思！请重新输入。')
        print('*'*50)
    python1 = eval(strr)
    # with open(file_name, 'w', encoding='utf-8') as file:
    #     json.dump(response_post, file, ensure_ascii=False)
    # print(python1)
    for i in python1:
        python3 = eval(str(i))
        # for x in python3:
        #     print(x.values)
        python3_list = list(python3.values())
        print(python3_list[0], '\t', ':', '\t', python3_list[1])
    print('*'*50)
