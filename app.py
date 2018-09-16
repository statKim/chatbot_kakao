import os
import json # json으로 바꾸기 위한 라이브러리
import random
import requests
from flask import Flask, request, jsonify
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route("/")
def hello():
    return "챗봇 페이지입니다!!!"
    
# keyboard API
@app.route("/keyboard")
def keyboard():
    # keyboard 딕셔너리 생성
    keyboard = {
        "type" : "buttons",
        "buttons" : ["학식 메뉴", "영재관 메뉴", "로또", "고양이", "영화"]
    }
    
    # 딕셔너리를 json으로 바꿔서 return
    json_keyboard = json.dumps(keyboard)
    return json_keyboard

# message API
@app.route("/message", methods=["POST"])
def message():
    # content라는 key의 value를 msg에 저장
    msg = request.json["content"] 
    img_bool = False
    menu_bool = False
    jeju_bool = False
    
    if msg == "학식 메뉴":
        # menu = ["경경관", "기숙사", "법학관", "카우버거"]
        # return_msg = random.choice(menu)
        menu_bool = True
        # json_return = {
        #     "message" : {
        #         "text" : "어디 학식이 궁금하세요?"
        #     },
        #     "keyboard" : {
        #         "type" : "buttons",
        #         "buttons" : ["경경관", "기숙사", "법학관", "교직원식당"]
        #     }
        # }

        # msg = request.json["content"]
        # if msg=="경경관":
        #     return_msg = "오오오오옹"
    elif msg == "영재관 메뉴":
        jeju_bool = True
    elif msg == "로또":
        pick = random.sample(range(1,46),6)
        return_msg = "로또번호 : " + str(sorted(pick))
    elif msg == "고양이":
        img_bool = True
        url = "https://api.thecatapi.com/v1/images/search?mime_types=jpg"
        req = requests.get(url).json()
        img_url = req[0]["url"]
        return_msg = "고양이"
    elif msg == "영화":
        img_bool = True
        
        url = "https://movie.naver.com/movie/running/current.nhn"
        req = requests.get(url).text
        doc = BeautifulSoup(req, "html.parser")
        
        title_tag = doc.select("dt.tit > a")
        star_tag = doc.select("div.star_t1 > a > span.num")
        reserve_tag = doc.select("div.star_t1.b_star > span.num")
        img_tag = doc.select("div.thumb > a > img")
        
        movie_dic = {}
        for i in range(0,7):
            movie_dic[i] ={
                "title" : title_tag[i].text,
                "star" : star_tag[i].text,
                "reserve" : reserve_tag[i].text,
                "img" : img_tag[i].get("src")
            } 
        
        pick_movie = movie_dic[random.randrange(0,7)]
        #print(pick_movie)
        return_msg = "영화제목 : {} \n별점 : {} \n예매율 : {}".format(pick_movie["title"], pick_movie["star"], pick_movie["reserve"])
        img_url = pick_movie["img"]
    elif msg == "경경관":
        return_msg = "경경식"
    elif msg == "기숙사":
        return_msg = "기식"
    elif msg == "법학관":
        return_msg = "법식"
    elif msg == "월":
        url = "http://www.jeju.go.kr/genius/notice/menu.htm"
        req = requests.get(url).text
        doc = BeautifulSoup(req, "html.parser")
        menu_list = doc.select("#mainContents > div.module-wrapper > table.table.table-list.table-bordered.table-week > tbody > tr > td > p.menu")
        breakfast = menu_list[1].text
        dinner = menu_list[8].text
        return_msg = "★아침\n{}\n★저녁\n{}".format(breakfast, dinner)
    elif msg == "화":
        url = "http://www.jeju.go.kr/genius/notice/menu.htm"
        req = requests.get(url).text
        doc = BeautifulSoup(req, "html.parser")
        menu_list = doc.select("#mainContents > div.module-wrapper > table.table.table-list.table-bordered.table-week > tbody > tr > td > p.menu")
        breakfast = menu_list[2].text
        dinner = menu_list[9].text
        return_msg = "★아침\n{}\n★저녁\n{}".format(breakfast, dinner)
    elif msg == "수":
        url = "http://www.jeju.go.kr/genius/notice/menu.htm"
        req = requests.get(url).text
        doc = BeautifulSoup(req, "html.parser")
        menu_list = doc.select("#mainContents > div.module-wrapper > table.table.table-list.table-bordered.table-week > tbody > tr > td > p.menu")
        breakfast = menu_list[3].text
        dinner = menu_list[10].text
        return_msg = "★아침\n{}\n★저녁\n{}".format(breakfast, dinner)
    elif msg == "목":
        url = "http://www.jeju.go.kr/genius/notice/menu.htm"
        req = requests.get(url).text
        doc = BeautifulSoup(req, "html.parser")
        menu_list = doc.select("#mainContents > div.module-wrapper > table.table.table-list.table-bordered.table-week > tbody > tr > td > p.menu")
        breakfast = menu_list[4].text
        dinner = menu_list[11].text
        return_msg = "★아침\n{}\n★저녁\n{}".format(breakfast, dinner)
    elif msg == "금":
        url = "http://www.jeju.go.kr/genius/notice/menu.htm"
        req = requests.get(url).text
        doc = BeautifulSoup(req, "html.parser")
        menu_list = doc.select("#mainContents > div.module-wrapper > table.table.table-list.table-bordered.table-week > tbody > tr > td > p.menu")
        breakfast = menu_list[5].text
        dinner = menu_list[12].text
        return_msg = "★아침\n{}\n★저녁\n{}".format(breakfast, dinner)
    elif msg == "토":
        url = "http://www.jeju.go.kr/genius/notice/menu.htm"
        req = requests.get(url).text
        doc = BeautifulSoup(req, "html.parser")
        menu_list = doc.select("#mainContents > div.module-wrapper > table.table.table-list.table-bordered.table-week > tbody > tr > td > p.menu")
        breakfast = menu_list[6].text
        dinner = menu_list[13].text
        return_msg = "★아침\n{}\n★저녁\n{}".format(breakfast, dinner)
    elif msg == "일":
        url = "http://www.jeju.go.kr/genius/notice/menu.htm"
        req = requests.get(url).text
        doc = BeautifulSoup(req, "html.parser")
        menu_list = doc.select("#mainContents > div.module-wrapper > table.table.table-list.table-bordered.table-week > tbody > tr > td > p.menu")
        breakfast = menu_list[0].text
        dinner = menu_list[7].text
        return_msg = "★아침\n{}\n★저녁\n{}".format(breakfast, dinner)
    else:
        return_msg = "현재 메뉴만 지원합니다."
    
    # 카카오톡에서 명령어 입력시 "text"에 있는 문구가 출력됨!!
    # 현재 이 단계에서는 사용자가 입력한 값을 그대로 답해줌

    if img_bool == True:
        json_return = {
            "message" : {
                "text" : return_msg,
                "photo" : {
                    "url" : img_url,
                    "width" : 720,
                    "height" : 640
                }
            },
            "keyboard" : {
                "type" : "buttons",
                "buttons" : ["학식 메뉴", "영재관 메뉴", "로또", "고양이", "영화"]
            }
        }
    elif menu_bool == True:
        json_return = {
            "message" : {
                "text" : "어디 학식이 궁금하세요?"
            },
            "keyboard" : {
                "type" : "buttons",
                "buttons" : ["경경관", "법학관", "기숙사"]
            }
        }          
    elif jeju_bool == True:
        json_return = {
            "message" : {
                "text" : "요일을 선택하세요"
            },
            "keyboard" : {
                "type" : "buttons",
                "buttons" : ["월", "화", "수", "목", "금", "토", "일"]
            }
        }  
    else:
        json_return = {
            "message" : {
                "text" : return_msg
            },
            "keyboard" : {
                "type" : "buttons",
                "buttons" : ["학식 메뉴", "영재관 메뉴", "로또", "고양이", "영화"]
            }
        }        
        
    # json.dumps()와 같은 기능 - json으로 바꿔주는 기능
    return jsonify(json_return)

app.run(host=os.getenv('IP', '0.0.0.0'),port=int(os.getenv('PORT', 8080)))
