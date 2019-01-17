import requests
from bs4 import BeautifulSoup
import random
import time

url = "http://www.statiz.co.kr/league.php?opt=" + str(time.localtime().tm_year)
req = requests.get(url).text
doc = BeautifulSoup(req, "html.parser")

ranking = doc.select("table.table.table-striped > tr")
print( doc.select("table.table.table-striped > tr")[1] )
if "div" in str(ranking[1]):
    print("ㄱㄱ")
else:
    print("ㄴㄴ")