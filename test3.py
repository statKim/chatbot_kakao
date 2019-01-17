import requests
from bs4 import BeautifulSoup
import random

url = "https://sports.news.naver.com/kbaseball/schedule/index.nhn"
req = requests.get(url).text
doc = BeautifulSoup(req, "html.parser")

print( doc.select("div.sch_score > ul.tab > li.on > a > em")[0].text.split(".") )

import time
print( str(time.localtime().tm_mon), str(time.localtime().tm_mday) )

today = doc.select("div.sch_score > ul.tab > li.on > a > em")[0].text.split(".")
if int(today[0])==time.localtime().tm_mon and int(today[1])==time.localtime().tm_mday:
    print("ㄱㄱ")