import requests
import bs4
from bs4 import BeautifulSoup
import re
import os
# def getHTMLText(url):
#     try:
#         r = requests.get(url, timeout=30)
#         r.raise_for_status()
#         r.encoding = r.apparent_encoding
#         return r.headers
#     except:
#         return '产生异常'
#
#
# url = 'http://www.baidu.com'
# print(getHTMLText(url))
# kv = {'key1': 'value1', 'key2': 'value2'}
# r = requests.post("http://www.baidu.com", params=kv)
# print(r.text)
# kv = {'user-agent': 'Mozilla/5.0'}
#
# r = requests.get('https://www.amazon.cn/gp/product/B01M8L5Z3Y', headers=kv)
# print(r.status_code)
# print(r.request.headers)
# print(r.text[1000:2000])


# kv = {'wd': 'python'}
# r = requests.get("http://www.baidu.com/s", params=kv)
# print(r.status_code)
# print(r.url)
# print(len(r.text))
# print(r.text[0:1000])

#图片爬取
# root = 'D://picture//'
# url = 'http://image.nationalgeographic.com.cn/2017/0211/20170211061910157.jpg'
# path = root + url.split('/')[-1]
# try:
#     r = requests.get(url)
#     if not os.path.exists(root):
#         os.mkdir(root)
#     if not os.path.exists(path):
#         with open(path, 'wb') as f:
#             f.write(r.content)
#     else:
#         print("文件存在")
# except:
#     print("文件爬取失败")


# # 视频爬取
# root = 'D://vedio//'
# # url = 'http://mvideo.spriteapp.cn/video/2017/1218/5a376c3461bed_wpcco.mp4'
# url = 'http://www.budejie.com/video/1'
# path = root + url.split('/')[-1]
# try:
#     r = requests.get(url)
#     r.raise_for_status()
#     demo = r.text
#     soup = BeautifulSoup(demo, 'html.parser')
#     ls = re.findall(r'.mp4$', soup)
#     print(ls)
#     # for line in soup.find_all('a'):
#     # print(soup)
#     # if not os.path.exists(root):
#     #     os.mkdir(root)
#     # if not os.path.exists(path):
#     #     with open(path, 'wb') as f:
#     #         f.write(r.content)
#     # else:
#     #     print("文件存在")
# except:
#     print("文件爬取失败")


#IP地址查询
# root = 'D://vedio//'
# url = 'https://python123.io/ws/demo.html'
# path = root + url.split("/")[-1]
# r = requests.get(url)
# # print(r.status_code)
# # print(r.text)
# demo = r.text
# # with open(path, 'w', encoding='utf8') as f:
# #     f.write(demo)
# soup = BeautifulSoup(demo, 'html.parser')
# # print(soup.prettify())
# print(soup.title)
# tag = soup.body
# print(tag.name)
# print("************************")
# soup = BeautifulSoup(demo, "html.parser")
#
# for tr in soup.find('body').children:
#     if isinstance(tr, bs4.element.Tag):
#         print(tr.attrs)



#爬取大学排名
# def getHTMLText(url):
#     return ""
# def fillUnivList
url = 'http://www.budejie.com/video/1'
r = requests.get(url)
r.raise_for_status()
demo = r.text
soup = BeautifulSoup(demo, 'html.parser')
ls = re.findall(r'.mp4$', demo)
print(ls)