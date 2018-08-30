import requests

url = "https://api.thecatapi.com/v1/images/search?mime_types=jpg"

request = requests.get(url).json()
print(type(request)) # request는 list 타입
print(request[0]["url"]) # url만 가져옴


