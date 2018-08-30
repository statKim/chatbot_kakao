# 파이썬 챗봇 만들기!!!

### 원리

- 입력 : 카톡에서 입력 -> 카카오톡 서버(API) -> 내 서버(카톡 서버에서 para 넘겨줌)
- 답변 : 내 서버(카톡 서버로 답변내용 para로 넘겨줌) -> 카카오톡 서버(API) -> 카톡 창으로 답변

### 카카오톡 플러스친구 관리자센터

- 플러스 친구 생성 후 공개설정 해줄 것(공개 안하면 검색 안됨!!)
- 스마트 채팅 -> API형 사용

### c9 개발

- 우측 상단의 톱니바퀴에 들어가서 python3로 설정 변경
- `sudo pip3 install flask` 플라스크 설치

### keyboard

```python
import os
import json # json으로 바꾸기 위한 라이브러리
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "챗봇 페이지입니다!!!"
    
@app.route("/keyboard")
def keyboard():
    # keyboard 딕셔너리 생성
    keyboard = {
        "type" : "buttons",
        "buttons" : ["메뉴", "로또", "고양이", "영화"]
    }
    
    # 딕셔너리를 json으로 바꿔서 return
    json_keyboard = json.dumps(keyboard)
    return json_keyboard

app.run(host=os.getenv('IP', '0.0.0.0'),port=int(os.getenv('PORT', 8080)))
```

### API

- request
    - url : 어떤 경로로 보낼지?
    - method : 어떤 방식으로 보낼지?
    - parameter : 어떤 정보를 담을지?
    
- response
    - data type : 어떤 형식으로 답할지?