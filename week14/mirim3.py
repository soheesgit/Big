import matplotlib.pyplot as plt

# pie 차트: 데이터 값에 따라 원형 비율로 나누어진 그래프
times = [7, 11, 4, 2]
timeLabels = ["Sleep", "Study", "Play", "Eat"]

plt.pie(times, labels=timeLabels, autopct="%.2f")   # 각 조각의 비율(%)을 소수점 2번째자리까지 표시
plt.show()