import requests
from bs4 import BeautifulSoup
import random

url = "https://sports.news.naver.com/kbaseball/schedule/index.nhn"
req = requests.get(url).text
doc = BeautifulSoup(req, "html.parser")

#print(doc)
# print(len(doc.select("#todaySchedule > li")[0]))

test = []
x = doc.select("#todaySchedule > li")
for i in range(len(x)):
    test.append(x[i].select("div.cancel"))
    if len(test[i]) == 0:
        print("ㅋㅋ")
print(test)

# print(doc.select("#todaySchedule > li.before_game.last.before_game > div.cancel")[0].text)
# x = doc.select("#todaySchedule > li.before_game.last.before_game > div.cancel")[0].text
# if "취소" in x:
#     print("굿")
    
#         if len(away) != 0:
#             game_status = doc.select("em.state")
#             for i in range(len(away)): # away 즉, 오늘의 경기 개수
#                 if "취소" in cancel[i].text:
#                     test = test + stadium[home[i].text] + " (우천취소)\n" + away[i].text + "\t:\t" + home[i].text + "\n\n"
#                 else:
#                     if home[i].text in stadium:
#                         test = test + stadium[home[i].text] + " (" + game_status[i].text.strip() + ")\n" + away[i].text + "\t" + away_score[i].text + "\t:\t" + home_score[i].text + "\t" + home[i].text + "\n\n"
#             return_msg = test[:-2]

# info = [[],[],[],[],[],[],[],[]]
# test = "★ 2018 KBO리그 팀순위\n\n순위\t|\t팀\t|\t경기\t|\t승\t|\t패\t|\t무\t|\t게임차\t|\t승률\n"
# for team in range(1,11,1):
#     x = doc.select("table.table.table-striped > tr")[team]
#     for i in range(0,8,1):
#         info[i].append(x.select("td")[i].text)
#         if i == 7:
#             test = test[:-3] + "\n"


# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt
# import six

# df = pd.DataFrame()
# df['순위'] = info[0]
# df['팀'] = info[1]
# df['경기'] = info[2]
# df['승'] = info[3]
# df['패'] = info[4]
# df['무'] = info[5]
# df['게임차'] = info[6]
# df['승률'] = info[7]
# print(df)
# print(doc.select("#_tab_box_kbo > div > ul > li > div.vs_list.vs_list2 > div > div")[0].text.strip())


# away = doc.select("#todaySchedule > li > div.vs_lft > p > strong")
# home = doc.select("#todaySchedule > li > div.vs_rgt > p > strong")
# away_pit = doc.select("#todaySchedule > li > div.vs_lft > p > span > a")
# home_pit = doc.select("#todaySchedule > li > div.vs_rgt > p > span > a")

# test = ""
# for i in range(5):
#     test = test + away[i].text + "\t\tVS\t\t" + home[i].text + "\n" + away_pit[i].text + "\t\tVS\t\t" + home_pit[i].text + "\n\n"
    
# print(test)



#print(doc.select("#mainContents > div.module-wrapper > table.table.table-list.table-bordered.table-week > tbody > tr > td > p.menu"))
#print(doc.find("span"))
# x = doc.select("div.badge")[0].text


# test = "순위\t팀\tG\t승\t패\t무\t승차\t승률\n"
# for team in range(1,11,1):
#     x = doc.select("table.table.table-striped > tr")[team]
#     # x = x.select("td")[1].text
#     for i in range(0,8,1):
#         test = test + x.select("td")[i].text + "\t"
#         if i == 7:
#             test = test + "\n"
# print(test)
# print(len(x))


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

