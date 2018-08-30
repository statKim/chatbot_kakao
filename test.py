import requests
from bs4 import BeautifulSoup
import random

# url = "https://api.thecatapi.com/v1/images/search?mime_types=jpg"

# request = requests.get(url).json()
# print(type(request)) # request는 list 타입
# print(request[0]["url"]) # url만 가져옴

url = "https://movie.naver.com/movie/running/current.nhn"
req = requests.get(url).text
doc = BeautifulSoup(req, "html.parser")
#print(doc)
#val = doc.select("#content > div.article > div > div.lst_wrap > ul > li > dl > dt > a")[0].text
#print(val)

# return_doc = doc.select("dt.tit > a")[0].text
# print(return_doc)

#val = doc.select("div.star_t1 > a > span.num")[0].text
#val = doc.select("div.star_t1.b_star > span.num")[0].text
#print(val)

# list_movie = []
# list_star = []
# list_res = []

# return_doc = doc.select("dt.tit > a")
# for i in return_doc:
#     #print(i.text)
#     list_movie.append(i.text)
# # print(list_movie)

# return_doc = doc.select("div.star_t1 > a > span.num")
# for i in return_doc:
#     #print(i.text)
#     list_star.append(i.text)
# # print(list_star)

# return_doc = doc.select("div.star_t1.b_star > span.num")
# for i in return_doc:
#     #print(i.text)
#     list_res.append(i.text)
# # print(list_res)

#(doc.select("div.thumb > a > img")[0].get("src"))


title_tag = doc.select("dt.tit > a")
star_tag = doc.select("div.star_t1 > a > span.num")
reserve_tag = doc.select("div.star_t1.b_star > span.num")
img_tag = doc.select("div.thumb > a > img")

# lst = []
# for i in range(0,10,1):
#     dic = {}
#     dic["movie"] = title_tag[i].text
#     dic["star"] = star_tag[i].text
#     dic["res"] = reserve_tag[i].text
#     lst.append(dic)
# print(lst)

movie_dic = {}
for i in range(0,10):
    movie_dic[i] ={
        "title" : title_tag[i].text,
        "star" : star_tag[i].text,
        "reserve" : reserve_tag[i].text,
        "img" : img_tag[i].get("src")
    } 

pick_movie = movie_dic[random.randrange(0,10)]
print(pick_movie)


