import requests
from bs4 import BeautifulSoup
import random

url = "https://sports.news.naver.com/wbaseball/schedule/index.nhn"
req = requests.get(url).text
doc = BeautifulSoup(req, "html.parser")

print(doc)

# print(doc.select("span"))
print(doc.select("tr.today > td > div.inner > span.team_left.winner > span.name"))
print(doc.find("span"))

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


