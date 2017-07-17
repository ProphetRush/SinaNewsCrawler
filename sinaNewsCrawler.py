import requests
from bs4 import BeautifulSoup
import json
import time




def run():
    show_num = 30
    page = 15
    newsList = list()
    for i in range(page):
        url = "http://feed.mix.sina.com.cn/api/roll/get?pageid=204&lid=22&num=" + str(show_num) + "&versionNumber=1.2.8" \
            "&page=" + str(i) + "&encode=utf-8"
        content = getJsonReturned(url)
        for k in content:
            newsList.append(k)
    return newsList


def getJsonReturned(url):
    newsList = list()
    newsInfos = (requests.get(url, timeout=30).json())['result']['data']
    for i in range(30):
        newsInfo = dict()
        newsInfo["title"] = newsInfos[i]["title"]
        newsInfo["url"] = newsInfos[i]["url"]
        t = time.localtime(int(newsInfos[i]["ctime"]))
        newsInfo["publishTime"] = time.strftime('%Y-%m-%d %H:%M:%S', t)
        newsInfo["articleKeyword"] = newsInfos[i]['keywords']
        newsInfo["source"] = newsInfos[i]["media_name"]
        if "comment_total" in newsInfos[i]:
            newsInfo["commentCount"] = newsInfos[i]["comment_total"]
        else:
            newsInfo["commentCount"] = 0
        newsList.append(newsInfo)
    return newsList

print(run())






