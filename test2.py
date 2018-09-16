import requests
from bs4 import BeautifulSoup
import random

url = "http://www.jeju.go.kr/genius/notice/menu.htm"
req = requests.get(url).text
doc = BeautifulSoup(req, "html.parser")

#print(doc)

# print(doc.select("span"))
#print(doc.select("#mainContents > div.module-wrapper > table.table.table-list.table-bordered.table-week > tbody > tr > td > p.menu"))
#print(doc.find("span"))
x = doc.select("#mainContents > div.module-wrapper > table.table.table-list.table-bordered.table-week > tbody > tr > td > p.menu")[13].text
print(x)
print(type(x))


# title_tag = doc.select("dt.tit > a")
# star_tag = doc.select("div.star_t1 > a > span.num")
# reserve_tag = doc.select("div.star_t1.b_star > span.num")
# img_tag = doc.select("div.thumb > a > img")

# movie_dic = {}
# for i in range(0,10):
#     movie_dic[i] ={
#         "title" : title_tag[i].text,
#         "star" : star_tag[i].text,
#         "reserve" : reserve_tag[i].text,
#         "img" : img_tag[i].get("src")
#     } 

# pick_movie = movie_dic[random.randrange(0,10)]
# print(pick_movie)


