import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from numpy.ma.extras import unique

# path = ""
# raw_df = pd.read_csv(path+"owid-covid-data.csv")

raw_df = pd.read_csv("owid-covid-data.csv")

# 원하는 열 만들기 : 국가 코드, 국가 이름, 일자, 전체확진자수, 인구
sel_Columns = ["iso_code", "location", "date", "total_cases", "population"]
df = raw_df[sel_Columns]

# 유일한 데이터 추출하기 : unique()
# unique_location = df["location"]
# print(unique_location.unique())

# 대한민국 데이터 추출
kor_df = df[df.location == "South Korea"]
# 무의미한 인덱스 번호 대신 date 의 값을 인덱스로 설정 : set_index
kor_date_index_df = kor_df.set_index("date")
# 미국 데이터 추출
usa_df = df[df.location == "United States"]
usa_date_index_df = usa_df.set_index("date")

# 그래프의 x축: 날짜, y축: 대한민국 확진자 수, 미국 확진자 수
kor_total_case = kor_date_index_df["total_cases"]  # 결과 시리즈로 반환
usa_total_case = usa_date_index_df["total_cases"]  # 결과 시리즈로 반환
print(kor_total_case.head(10))  # 인덱스인 날짜 & 확진자 수만 출력
print(usa_total_case.head(10))  # 인덱스인 날짜 & 확진자 수만 출력

#그래프로 시각화하려면? 데이터프레임 필요! (x축 : 날짜가 출력)
#index = kor_date_index_df.inedx ---> x축
final_df = pd.DataFrame(
    {"KOR": kor_total_case,
     "USA": usa_total_case, },
    index=kor_date_index_df.index
)

#2022년도의 데이터만 그래프에 출력
final_df["2022-01-01": ].plot.line(rot=30)
plt.show()

#인구 대비 확진자 비율 구하기
kor_population = kor_date_index_df["population"]["2020-01-22"]
usa_population = usa_date_index_df["population"]["2020-01-22"]
print("미국 입구:", usa_population, ", 한국 인구: ", kor_population)
rate = round(usa_population / kor_population)
# 대한민국 확진자수에 rate만큽 곱하기 => 최종 데이터프레임 생성 => 그래프 출력
final_df = pd.DataFrame(
    {"KOR": kor_total_case * rate,
     "USA": usa_total_case},
    index=kor_date_index_df.index
)
final_df["2022-01-01":].plot.line(rot=30)
plt.show()

raw_hawaii_df = pd.read_csv("hawaii-covid-data.csv")
print(raw_hawaii_df.info())
filter_hawaii_df = raw_hawaii_df[["submission_date", "tot_cases"]]
# 날짜순 정렬: filter_hawaii_df.sort_values(by="정렬")
sorted_hawaii_df = filter_hawaii_df.sort_values(by="submission_date")
print(sorted_hawaii_df.head())

# 날짜를 "년-월-일"로 변환하여 마지막에 'date' 열 추가: pd.to_datetime(원본[열])
sorted_hawaii_df['date'] = pd.to_datetime(filter_hawaii_df["submission_date"])
print(sorted_hawaii_df.head())

# 'date' 열 기준 정렬 ==> 새로운 변수 생성X, 바로 객체 값을 변경
# inplace=True 속성 지정
sorted_hawaii_df.sort_values(by="date", inplace=True)
print(sorted_hawaii_df)

# 대한민국 데이터처럼 'date' 열 인덱스로 설정
sorted_hawaii_df.set_index('date', inplace=True)

# 그래프로 시각화
hawaii_total_cases = sorted_hawaii_df['tot_cases']
print(hawaii_total_cases.head())

hawaii_population = 1_440_359
hawaii_rate = round(hawaii_population / kor_population, 2)

final_hawaii_df = pd.DataFrame(
    {"KOR": kor_total_case * hawaii_rate,
     "HAWAII": hawaii_total_cases},
    index=kor_date_index_df.index
)

print(str(kor_total_case.index.dtype))
print(str(hawaii_total_cases.index.dtype))
hawaii_total_cases.index = hawaii_total_cases.index.astype("string")

final_hawaii_revise_df = pd.DataFrame(
    {"KOR": kor_total_case * hawaii_rate,
     "HAWAII": hawaii_total_cases},
    index=kor_date_index_df.index
)

final_hawaii_revise_df["2022-01-01":].plot.line(rot=45)

plt.show()
