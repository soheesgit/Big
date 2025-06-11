import pandas as pd
import matplotlib.pyplot as plt

raw_data = pd.read_csv("C:/Users/gram15/KnuUniv/3-1/빅데이터분석실습/수업 자료/survey_results_public.csv")
print(raw_data.info())
print()

# [1] 필요한 열 추출: Age(나이), Country(국가), LanguageHaveWorkedWith(다룰 줄 아는 언어), LearnCode(배운 방법)
revise_data = raw_data[["Age", "Country", "LanguageHaveWorkedWith", "LearnCode"]]
print(revise_data)
print()

# [2] 설문 조사에 응한 개발자의 연령대 조회
print(revise_data["Age"])
print()

# [3] 연령대 중복 데이터 제거
print(revise_data["Age"].drop_duplicates())
print()

# [4] 데이터 프레임 값 집계 => 데이터 그룹화 groupby()
print(revise_data.groupby(["Age"]))
print()

# [5] 그룹별(연령대별) 응답자 수 확인: size
size_by_age = revise_data.groupby(["Age"]).size()
print(size_by_age)
print()

# [6] 국가별(Country) 응답자 수 확인
size_by_country = revise_data.groupby(["Country"]).size()
print(size_by_country)
print()

# ------------------------------------------------
# 데이터 시각화
# ------------------------------------------------
# size_by_age.plot.line(rot=45)
# 색인 조정
reindex_size_by_age = size_by_age.reindex(index=
                                          ["Prefer not to say", "65 years or older",
                                           "55-64 years old", "45-54 years old",
                                           "35-44 years old", "25-34 years old",
                                           "18-24 years old", "Under 18 years old"])
# reindex_size_by_age.plot.barh(rot=45)

# 국가별 응답자 수를 파이 그래프로 출력
# size_by_country.plot.pie()
# size_by_country.plot.pie(figsize=(10,10))     # figsize: 파이그래프의 너비와 높이를 10, 10으로 조정
# 미세하게 나뉘어진 국가는 제외하고 상위 20개 국가에 대한 파이 그래프 출력: nlargest()
size_by_country.nlargest(20).plot.pie(figsize=(10,10))
plt.show()

language = revise_data["LanguageHaveWorkedWith"]
language = language.str.split(";")
# 리스트의 항목 갯수만큼 항목을 행으로 쪼개기
explode_language = language.explode()
# 프로그래밍별 응답자 수 구하기
size_by_language = explode_language.groupby(explode_language).size()
# size_by_language.nlargest(10).plot.pie(figsize=(10,10))

# 고민자와 비슷한 연령대(25 ~ 34)의 개발자들이 다룬 언어 중 상위 10개를 추출하여 그래프로 그리기
language_25_34 = revise_data[revise_data.Age=="25-34 years old"]["LanguageHaveWorkedWith"].str.split(";").explode()
language_25_34.groupby(language_25_34).size().nlargest(10).plot.pie(figsize=(10,10))

plt.show()
