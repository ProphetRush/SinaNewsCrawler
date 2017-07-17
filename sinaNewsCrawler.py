import requests
from bs4 import BeautifulSoup
import json
import time
import csv
import collections
import matplotlib.pyplot as plt

def run():
    show_num = 25
    page = 40
    newsList = list()
    for i in range(page):
        url = "http://feed.mix.sina.com.cn/api/roll/get?pageid=204&lid=22&num=" + str(show_num) + "&versionNumber=1.2.8" \
            "&page=" + str(i) + "&encode=utf-8"
        content = getJsonReturned(url)
        for k in content:
            newsList.append(k)
    f = csv.writer(open("news.csv", "w+", encoding="utf"))
    #newsJSON = json.loads(json.dumps(newsList))
    f.writerow(["title", "articleKeyword", "source", "commentCount", "publishTime", "url"])
    for x in newsList:
        f.writerow([x["title"], x["articleKeyword"], x["source"], x["commentCount"], x["publishTime"], x["url"]])
    return newsList


def getJsonReturned(url):
    newsList = list()
    newsInfos = (requests.get(url, timeout=30).json())['result']['data']
    for i in range(25):
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


def wordCount(newsList):
    keywords = list()
    for x in newsList:
        kw = x["articleKeyword"].split(",")
        for i in kw:
            keywords.append(i)
    kw = collections.Counter(keywords)
    s = sorted(kw.items(), key=lambda k: k [1], reverse=True)[:20]
    return s


def sourceCount(newsList):
    sources = list()
    for x in newsList:
        sources.append(x["source"])
    srcCount = collections.Counter(sources)
    scount = sorted(srcCount.items(), key=lambda k: k[1], reverse=True)[:10]
    return scount


def drawTimeDistribution(newsList):
    timePeriod = list()
    for x in newsList:
        timePeriod.append(x["publishTime"][11:13])
    return collections.Counter(timePeriod)




a = run()
print(drawTimeDistribution(a))







