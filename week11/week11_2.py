import pandas as pd

data = {
    "이름": ["여자친구", "소녀시대", "레드벨벳", "에이핑크", "마마무"],
    "인원": [6, 8, 4, 6, 4],
    "데뷔일자": ["2020.05.05", "2006.01.01", "2010.03.01", "2017.12.13", "2013.06.17"]
}
indexList = ["WMN", "GRL", "RED", "APN", "MMU"]
df = pd.DataFrame(data, index=indexList)

# [1번] 인원 열 삭제 => .drop()
df = df.drop(columns=["인원"])

# [2번] 인덱스 "GRL", "RED" 인 행 삭제 => .drop()
df = df.drop(index=["GRL", "RED"])

# [3번] 인덱스 "ABC" 행 "이름": "에스파", "데뷔일자":"2022.07.17" 삽입
df.loc["ABC"] = {"이름": "에스파", "데뷔일자": "2022.07.17"}

# 최종 결과 출력
print(df)
