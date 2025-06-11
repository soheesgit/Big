import matplotlib.pyplot as plt

# plt.plot([1, 3, 5, 7], [1, 8, 4, 10], 'g.' )      # (1, 1), (3, 8), (5, 4), (7, 10)의 그래프 생성, 좌표에 초록색 점
plt.bar([1, 3, 5, 7], [1, 8, 4, 10])        # 막대 그래프

plt.title("Graph Ex")
plt.xlabel("month")
plt.ylabel("Count")
plt.axis([0, 8, 0, 12])     # x축 범위 0-8, y축 범위 0-12

plt.show()