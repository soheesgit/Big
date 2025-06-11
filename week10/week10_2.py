import pandas as pd

# GitHub에서 제공하는 파일을 원시(raw)형식으로 읽기 위해 => https://raw.githubusercontent.com/
path = "https://raw.githubusercontent.com/dongupak/BigDataAnalysis/main/"
# df = pd.read_csv(path + "scores.csv", encoding="utf-8") #자동 인덱스번호가 0부터 매겨짐
# df = pd.read_csv(path + "scores.csv", encoding="cp949")
# ---- [방법1] 첫번째(0) 열, 즉 "학번" 열을 인덱스로 사용하고자 하는 경우,
df = pd.read_csv(path + "scores.csv", encoding="utf-8", index_col=0)
# ---- [방법2] 첫번째(0) 열, 즉 "학번" 열을 인덱스로 사용하고자 하는 경우,
df = pd.read_csv(path + "scores.csv", encoding="utf-8").set_index("학번")
print(df)
print(df["국어"])
