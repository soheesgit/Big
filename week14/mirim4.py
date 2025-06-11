# 아시아 국가(kr, jp, ch)의 1인당 국민 소득을 비교
# 연도별로 각 국가의 막대그래프가 하나씩 나타나도록 작성 => 다중 막대 그래프

import matplotlib.pyplot as plt
import numpy as np

years = [1975, 1985, 1995, 2005, 2015]
ko = [650, 2450, 11600, 17700, 28000]
jp = [5100, 15500, 42130, 40560, 38000]
ch = [200, 295, 540, 1760, 8000]

# x_years = range(len(years))
x_years = np.arange(len(years))     # 5개의 실수 범위 값 생성
plt.bar(x_years-0.3, ko, width=0.25)
plt.bar(x_years+0.0, jp, width=0.25)
plt.bar(x_years+0.3, ch, width=0.25)

plt.xticks(x_years, years)

plt.show()