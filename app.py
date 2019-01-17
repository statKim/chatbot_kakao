import os
import json # json으로 바꾸기 위한 라이브러리
import random
import requests
from flask import Flask, request, jsonify
from bs4 import BeautifulSoup
import time # 영재관 메뉴에서 오늘의 요일 찾을 때 사용

app = Flask(__name__)

@app.route("/") # "https://python-chatbot-hyunsung1021.c9users.io" : c9 ip주소(root page)
def hello():
    return "챗봇 페이지입니다!!!"
    
# keyboard API
@app.route("/keyboard")
def keyboard():
    # keyboard 딕셔너리 생성
    keyboard = {
        "type" : "buttons",
        "buttons" : ["야구", "영재관 메뉴", "영화", "고양이", "학식 메뉴"]
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
    kbo_bool = False
    
    if msg == "야구":
        kbo_bool = True
    elif msg == "학식 메뉴":
        menu_bool = True
    elif msg == "영재관 메뉴":
        jeju_bool = True
    # elif msg == "로또":
    #     pick = random.sample(range(1,46),6)
    #     return_msg = "로또번호 : " + str(sorted(pick))
    elif msg == "고양이":
        img_bool = True
        url = "https://api.thecatapi.com/v1/images/search?mime_types=jpg"
        req = requests.get(url).json()
        img_url = req[0]["url"] # ex) https://24.media.tumblr.com/tumblr_lq46ox3kqA1qmjao5o1_500.jpg
        # print(img_url)
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
        
        pick_rank = random.randrange(0,7)
        pick_movie = movie_dic[pick_rank]
        #print(pick_movie)
        return_msg = "영화제목 : {}\n평점 : {}\n예매율 : {}\n예매순위 : {}".format(pick_movie["title"], pick_movie["star"], pick_movie["reserve"], pick_rank + 1)
        img_url = pick_movie["img"]
    
    # "학식 메뉴" 선택시    
    elif msg == "경경관":
        return_msg = "경경식"
    elif msg == "기숙사":
        return_msg = "기식"
    elif msg == "법학관":
        return_msg = "법식"
        
    # "영재관 메뉴" 선택시
    elif msg in ["오늘의 메뉴", "내일의 메뉴", "월", "화", "수", "목", "금", "토", "일"]:
        url = "http://www.jeju.go.kr/genius/notice/menu.htm"
        req = requests.get(url).text
        doc = BeautifulSoup(req, "html.parser")
        menu_list = doc.select("#mainContents > div.module-wrapper > table.table.table-list.table-bordered.table-week > tbody > tr > td > p.menu")
        week = ["월", "화", "수", "목", "금", "토", "일"]
        
        if len(menu_list) != 0:
            tommorow_sunday = False
            if msg == "오늘의 메뉴":
                today = week[time.localtime().tm_wday]
                if today == "월":
                    ind_breakfast = 1
                    ind_dinner = 8
                elif today == "화":
                    ind_breakfast = 2
                    ind_dinner = 9
                elif today == "수":
                    ind_breakfast = 3
                    ind_dinner = 10            
                elif today == "목":
                    ind_breakfast = 4
                    ind_dinner = 11
                elif today == "금":
                    ind_breakfast = 5
                    ind_dinner = 12            
                elif today == "토":
                    ind_breakfast = 6
                    ind_dinner = 13            
                elif today == "일":
                    ind_breakfast = 0
                    ind_dinner = 7     
            elif msg == "내일의 메뉴":
                if week[time.localtime().tm_wday] != "토":
                    if week[time.localtime().tm_wday] == "일":
                        tomorrow = week[0]
                    else:
                        tomorrow = week[time.localtime().tm_wday + 1]
                    if tomorrow == "월":
                        ind_breakfast = 1
                        ind_dinner = 8
                    elif tomorrow == "화":
                        ind_breakfast = 2
                        ind_dinner = 9
                    elif tomorrow == "수":
                        ind_breakfast = 3
                        ind_dinner = 10            
                    elif tomorrow == "목":
                        ind_breakfast = 4
                        ind_dinner = 11
                    elif tomorrow == "금":
                        ind_breakfast = 5
                        ind_dinner = 12            
                    elif tomorrow == "토":
                        ind_breakfast = 6
                        ind_dinner = 13            
                    elif tomorrow == "일":
                        ind_breakfast = 0
                        ind_dinner = 7
                else:
                    tommorow_sunday = True  # 내일이 일요일일 경우에는 다른 메시지 날릴 것!!
            # 원하는 요일 선택할 때     
            elif msg in week:
                if msg == "월":
                    ind_breakfast = 1
                    ind_dinner = 8
                elif msg == "화":
                    ind_breakfast = 2
                    ind_dinner = 9
                elif msg == "수":
                    ind_breakfast = 3
                    ind_dinner = 10            
                elif msg == "목":
                    ind_breakfast = 4
                    ind_dinner = 11
                elif msg == "금":
                    ind_breakfast = 5
                    ind_dinner = 12            
                elif msg == "토":
                    ind_breakfast = 6
                    ind_dinner = 13            
                elif msg == "일":
                    ind_breakfast = 0
                    ind_dinner = 7     
                    
            # return_msg 표현하는 부분
            if tommorow_sunday == True:
                return_msg = "죄송합니다. 일요일 메뉴를 클릭해서 이용해주시기 바랍니다."
            else:
                breakfast = menu_list[ind_breakfast].text
                dinner = menu_list[ind_dinner].text
                if msg in week:
                    return_msg = "■ {}요일의 메뉴\n\n★아침\n{}\n\n★저녁\n{}".format(msg, breakfast, dinner)  
                else:
                    return_msg = "■ {}\n\n★아침\n{}\n\n★저녁\n{}".format(msg, breakfast, dinner)  
        else:
            return_msg = "죄송합니다. 아직 메뉴가 업데이트되지 않았습니다."  
            
    # "야구" 선택시
    elif msg in ["오늘의 매치업", "오늘의 경기"]:
        url = "https://sports.news.naver.com/kbaseball/schedule/index.nhn"
        req = requests.get(url).text
        doc = BeautifulSoup(req, "html.parser")  
        today = doc.select("div.sch_score > ul.tab > li.on > a > em")[0].text.split(".")    # 오늘 날짜 체크
        
        # 오늘 날짜와 크롤링해온 날짜가 같으면 경기하는 날!
        if (int(today[0]) == time.localtime().tm_mon) and (int(today[1]) == time.localtime().tm_mday):
            away = doc.select("#todaySchedule > li > div.vs_lft > p > strong")
            home = doc.select("#todaySchedule > li > div.vs_rgt > p > strong")
            away_pit = doc.select("#todaySchedule > li > div.vs_lft > p > span > a")
            home_pit = doc.select("#todaySchedule > li > div.vs_rgt > p > span > a")  
            game_status = doc.select("em.state")
            stadium = {"키움":"고척", "SK":"문학", "두산":"잠실", "LG":"잠실", "KIA":"광주",
                        "롯데":"사직", "삼성":"대구", "NC":"마산", "한화":"대전", "KT":"수원"}
            if len(away) != 0:  # 진행되는 경기가 있으면            
                if msg == "오늘의 매치업":
                    test = "★ 오늘의 매치업\n\n"
                    for i in range(len(away)):
                        game_status = doc.select("em.state")
                        if home[i].text in stadium:
                            test = test + stadium[home[i].text] + " (" + game_status[i].text.strip() + ")\n" + away[i].text + "\tVS\t" + home[i].text + "(♠)\n" + away_pit[i].text + "\tVS\t" + home_pit[i].text + "\n\n"
                    return_msg = test[:-2]
                elif msg == "오늘의 경기":
                    cancel = doc.select("#todaySchedule > li")  # 각 블럭 별로 취소인지 확인할 것임
                    test = "★ 오늘의 경기\n\n"
                    for i in range(len(away)): # away 즉, 오늘의 경기 개수
                        if len(cancel[i].select("div.cancel")) != 0:    # 경기 취소시
                            test = test + stadium[home[i].text] + " (취소)\n" + away[i].text + "\tVS\t" + home[i].text + "(♠)\n\n"
                        else:
                            if home[i].text in stadium:
                                test = test + stadium[home[i].text] + " (" + game_status[i].text.strip() + ")\n" + away[i].text + "\t" + away_score[i].text + "\t:\t" + home_score[i].text + "\t" + home[i].text + "(♠)\n\n"
                    return_msg = test[:-2] 
                else:
                    return_msg = "잘못 누르셨습니다."
            else:
                return_msg = "오늘은 경기가 없습니다."        
        else:
            return_msg = "오늘은 경기가 없습니다."
    elif msg == "팀순위":
        url = "http://www.statiz.co.kr/league.php?opt=" + str(time.localtime().tm_year)
        req = requests.get(url).text
        doc = BeautifulSoup(req, "html.parser")
        test = "★ 2018 KBO리그 팀순위\n\n순위 │ 팀 │ 경기 │ 승 │ 패 │ 무 │ 게임차 │ 승률\n\n"
        ranking = doc.select("table.table.table-striped > tr")
        
        if "div" in str(ranking):   # div태그가 있으면 순위표가 아님
            return_msg = "아직 시즌이 시작하지 않았습니다."
        else:
            for team in range(1,11,1):
                for i in range(0,8,1):
                    test = test + ranking[team].select("td")[i].text + " │ "
                    if i == 7:
                        test = test[:-3] + "\n\n"
            return_msg = test            

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
                "buttons" : ["야구", "영재관 메뉴", "영화", "고양이", "학식 메뉴"]
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
                "text" : "언제 메뉴가 궁금하세요?"
            },
            "keyboard" : {
                "type" : "buttons",
                "buttons" : ["오늘의 메뉴", "내일의 메뉴", "일", "월", "화", "수", "목", "금", "토"]
            }
        }
    elif kbo_bool == True:
        json_return = {
            "message" : {
                "text" : "어떤 것이 궁금하세요?"
            },
            "keyboard" : {
                "type" : "buttons",
                "buttons" : ["오늘의 매치업", "오늘의 경기", "팀순위"]
            }
        }        
    else:
        json_return = {
            "message" : {
                "text" : return_msg
            },
            "keyboard" : {
                "type" : "buttons",
                "buttons" : ["야구", "영재관 메뉴", "영화", "고양이", "학식 메뉴"]
            }
        }        
        
    # json.dumps()와 같은 기능 - json으로 바꿔주는 기능
    return jsonify(json_return)

app.run(host=os.getenv('IP', '0.0.0.0'), port=int(os.getenv('PORT', 8080)))
# app.run(host="0.0.0.0", port="8080", debug=True)