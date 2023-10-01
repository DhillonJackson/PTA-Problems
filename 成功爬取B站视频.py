import requests
import json
import pprint
import re
url='https://www.bilibili.com/video/BV11h4y1u71L/'
headers={
    'referer':'https://www.bilibili.com/',
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.51'
}
response=requests.get(url=url,headers=headers)
result=re.findall('<script>window.__playinfo__=(.*?)</script>',response.text)[0]   #注意一定要有? ？表示非贪婪匹配  即匹配尽量少的字符
#print(type(result))
json_data=json.loads(result)  #字典类型数据
#print(type(json_data))
#pprint.pprint(json_data)
audiourl=json_data['data']['dash']['audio'][0]['baseUrl']
videourl=json_data['data']['dash']['video'][0]['baseUrl']
url2=audiourl
headers={
    'referer':'https://www.bilibili.com/',
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.51'
}
response2=requests.get(url=url2,headers=headers)
with open(r"C:\Users\86183\Desktop\audio.mp3",'wb') as file:
    file.write(response2.content)

url3=videourl
headers={
    'referer':'https://www.bilibili.com/',
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.51'
}
response3=requests.get(url=url3,headers=headers)
with open(r"C:\Users\86183\Desktop\video.mp4",'wb') as file:
    file.write(response3.content)
print('complete')