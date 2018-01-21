# CrawUnivRankingA.py
import requests
from bs4 import BeautifulSoup
import bs4


def getHTMLText(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""


def fillUnivList(ulist, html):
    soup = BeautifulSoup(html, "html.parser")
    # print(">>>>>>>>>>"+soup.td.parent.name)
    # print(soup.find('tbody').children)
    for tr in soup.find('tbody').children:
        if isinstance(tr, bs4.element.Tag):
            tds = tr('td')
            # print(tr('td'))
            ulist.append([tds[0].string, tds[1].string, tds[3].string])


def printUnivList(ulist, num):
    print("{0:{3}<3}\t{1:{3}<10}\t{2:<10}".format("排名", "学校名称", "总分", chr(12288)))
    for i in range(num):
        u = ulist[i]
        print("{0:{3}<5}\t{1:{3}<10}\t{2:<10}".format(u[0], u[1], u[2], chr(12288)))


def main():

    uinfo = []
    url = 'http://www.zuihaodaxue.cn/zuihaodaxuepaiming2016.html'
    html = getHTMLText(url)
    fillUnivList(uinfo, html)
    printUnivList(uinfo, 20)  # 20 univs


main()
