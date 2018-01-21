# 视频爬取
import requests
import re
import os

def getHTTPText(url):
    try:
        kv = {'user-agent': 'Mozilla/5.0'}
        r = requests.get(url, headers=kv)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return "产生异常"


def getPage(urlList, html):
    reg = r'data-mp4="(.*?)"'
    for i in re.findall(reg, html):
        urlList.append(i)


def downVedio(urlList, num):
    root = 'D:\\vedio\\'
    if not os.path.exists(root):
            os.mkdir(root)
    for i in range(num):
        path = root + urlList[i].split("/")[-1]
        if not os.path.exists(path):
            r1 = requests.get(urlList[i])
            print("-----------正在下载第%s个视频----------" % i)
            with open(path, 'wb') as f:
                f.write(r1.content)
        else:
            print("文件存在")


def main():
    vidUrlList = []
    depth = 2
    for i in range(1,depth+1):
        try:
            url = 'http://www.budejie.com/video/' + str(i)
            html = getHTTPText(url)
            getPage(vidUrlList, html)
        except:
            continue
    downVedio(vidUrlList, 20)

main()

