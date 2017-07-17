import requests
from bs4 import BeautifulSoup
import json
import time

newsProperties = {"title": "", "url": "", "source": "", "commentCount": "", "articleKeyword": "", "publishTime": ""}
show_num = 30
page = 1
url = "http://feed.mix.sina.com.cn/api/roll/get?pageid=204&lid=22&num=30&versionNumber=1.2.8&page=1"


def getJsonReturned(url):
        r = requests.get(url, timeout=30).json
        r.raise_for_status()
        r.encoding = "unicode_escape"
        newsInfos = (json.loads(r.text.replace('\r\n', ''), strict=False))
        for i in range(page):
            newsInfo = {"title": "", "url": "", "source": "", "commentCount": "", "articleKeyword": "", "publishTime": ""}
            newsInfo["title"] = newsInfos['data'][i]["title"]
            newsInfo["url"] = newsInfos['data'][i]["url"]
            t = time.localtime(newsInfos['data'][i]["createtime"])
            newsInfo["publishTime"] = time.strftime('%Y-%m-%d %H:%M:%S', t)
            newsInfo["articleKeyword"] = newsInfos['data'][i]['keywords']
            newsInfo["source"] = newsInfos['data'][i]["media_name"]
        return newsInfos

getJsonReturned(url)
