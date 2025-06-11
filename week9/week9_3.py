import csv

infile = open(r"weather.csv", "r", encoding="cp949")
data = csv.reader(infile)

header = next(data) # 헤더 가져오기
# 최저 기온을 저장하기 위한 변수
temp = 1000

for row in data:
    # print(row)
    if temp > float(row[3]):
        temp = float(row[3])

print("서울이 가장 추웠던 날의 기온: ", temp, "도 입니다.")

infile.close()