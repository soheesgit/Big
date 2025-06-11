import matplotlib.pyplot as plt

# 우리나라 연간 1인당 국민 소득을 각각 years, gdp에 저장
years = [1950, 1960, 1970, 1980, 1990, 2000, 2010, 2020]
gdp = [67.0, 80.0, 257.0, 1686.0, 6505, 11865.3, 21204.7, 23000]

# 선 그래프 그리기
# plt.plot(years, gdp, marker='d', color='blue', linestyle='-.')

# 막대 그래프
plt.bar(range(len(years)), gdp)     # 굵은 막대, y축: 0-7 8개 항
plt.xticks(range(len(years)), years)    # 가로축 범위 눈금마다 years 항목 출력

plt.title("GDP per capita")
plt.xlabel("year")
plt.ylabel("dollars")

# plt.savefig("gdp_per_capita.png", dpi=600)  # dpi: 화질
plt.show()