import requests
import bs4
from bs4 import BeautifulSoup

def getHTTPText(url):
    try:
        r = requests.get(url)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ''

def fillUnivList(html, ulist):
    soup = BeautifulSoup(html, 'html.parser')
    for tr in soup.find('tbody').children:
        if isinstance(tr, bs4.element.Tag):    #这个是必要的，因为
            tds = tr('td')
            ulist.append([tds[0].string, tds[1].string, tds[3].string])

def printUnivList(ulist, num):
    print("{:<2}\t{:<10}\t{:<4}".format("排名", "学校名称", "综合分数"))
    for i in range(num):
        # print('%-4s%-15s%-4s' % (ulist[i][0], ulist[i][1], ulist[i][2]))
        print("{:<3}\t{:<10}\t{:<10}".format(ulist[i][0], ulist[i][1], ulist[i][2]))
def main():
    uinfo = []
    url = 'http://www.zuihaodaxue.cn/zuihaodaxuepaiming2016.html'
    html = getHTTPText(url)
    fillUnivList(html, uinfo)
    printUnivList(uinfo, 20)

main()