import requests
url='https://baike.baidu.com/item/%E9%80%9A%E7%94%A8%E5%BC%82%E6%AD%A5%E6%94%B6%E5%8F%91%E5%99%A8/9196744?fromtitle=UART&fromid=4429746&fr=aladdin'
headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.58'}
response=requests.get(url=url,headers=headers)
with open(r'D:\北京邮电大学\Python\数据结构\data.txt','w',encoding='utf-8') as file:
    file.write(response.text)