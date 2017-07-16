import requests
from bs4 import BeautifulSoup
import json
import time

newsProperties = {"title": "", "url": "", "source": "", "commentCount": "", "articleKeyword": "", "publishTime": ""}
show_num = 30
page = 1
url = "http://api.roll.news.sina.com.cn/zt_list?channel=news&cat_1=shxw&cat_2==zqsk||=qwys||=shwx||=fz-shyf&level==1" \
      "||=2&show_ext=1&show_all=1&show_num=" + str(show_num) + "&tag=1&format=json&page="+str(page)
newsList = list()


def getJsonReturned(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = "unicode_escape"
        newsInfos = (json.loads(r.content))['result']
        for i in range(page):
            newsInfo = {"title": "", "url": "", "source": "", "commentCount": "", "articleKeyword": "", "publishTime": ""}
            newsInfo["title"] = newsInfos['data'][i]["title"]
            newsInfo["url"] = newsInfos['data'][i]["url"]
            t = time.localtime(newsInfos['data'][i]["createtime"])
            newsInfo["publishTime"] = time.strftime('%Y-%m-%d %H:%M:%S', t)
            newsInfo["articleKeyword"] = newsInfos['data'][i]['keywords']
            newsInfo["source"] = newsInfos['data'][i]["media_name"]

    except:
        return ""

def getCommentCount(url):
    r = requests.get(url, timeout=30)
    r.raise_for_status()
    r.encoding = "unicode_escape"




def getNewsInfo(text):
    s = BeautifulSoup(text, "html.parser")

    return s


print(getJsonReturned(url))






