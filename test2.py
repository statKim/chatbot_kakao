import requests
from bs4 import BeautifulSoup
import random

url = "http://www.statiz.co.kr/league.php?opt=2018"
req = requests.get(url).text
doc = BeautifulSoup(req, "html.parser")

#print(doc)
# print(len(doc.select("#todaySchedule > li")[0]))

test = "★ 2018 KBO리그 팀순위\n\n순위 │ 팀 │ 경기 │ 승 │ 패 │ 무 │ 게임차 │ 승률\n"
for team in range(1,11,1):
    x = doc.select("table.table.table-striped > tr")[team]
    for i in range(0,8,1):
        test = test + x.select("td")[i].text + " │ "
        if i == 7:
            test = test[:-3] + "\n"
print(test)

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

