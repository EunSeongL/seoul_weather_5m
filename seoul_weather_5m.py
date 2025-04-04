# os.mkdir("폴더 이름")    ->  햔재 작업위치에 파일 생성
# 5분마다 한 번씩 서울의 기온 정보를 csv형태로 저장
#os.getcwd()

import requests
import csv
from datetime import datetime
import os

MY_API_KEY = os.getenv("OPENWEATHER_API_KEY")
CITY = "Seoul"
URL = f"https://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={MY_API_KEY}&units=metric"

response = requests.get(URL)
data = response.json()
# 서울 기온 하나!
temp = data["main"]["temp"]
time = datetime.now().strftime("%y-%m-%d %H:%M:%S")

csv_filename ="seoul_weather.csv"
header = ["time", "temp"]

#seoul_weather.csv가 없다면 새로 생성 -> 만약 없다면 갱신
#ex) 2025년 04월 04일 10시56분 : 12 도

file_exist = os.path.isfile(csv_filename)

# a mode => 없으며 쓰기, 있으면 쓰기 모드로 불러오기
# w mode => 무조건 덮어쓰기
with open(csv_filename, "a", newline="\n") as file:
    writer = csv.writer(file)

    #만약 csv가 없다면 헤더도 없음
    if not file_exist:
        writer.writerow(header)
        
    writer.writerow([time, temp])
    print("서울 기온 저장 완료!")
