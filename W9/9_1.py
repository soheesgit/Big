from tkinter import *
import csv

# 총 행의 개수와 총 열의 개수만큼의 빈 엔트리를 갖는 리스트 생성 함수
def makeEmptySheet(r, w):
    resultList = []     # 2차원 빈 엔트리르 갖는 리스트
    for i in range(0, r):
        tempList = []       # 열 개수만큼 1차원 리스트
        for c in range(0, w):
            e = Entry(window, text=" ", width=10)
            e.grid(row=i, column=c)     # 윈도우창에 부착될 위치
            tempList.append(e)      # 1차원 리스트에 빈 엔트리 추가
        resultList.append(tempList)        # 2차원 리스트 완성
    return resultList

window = Tk()
csvList = []        # 읽어온 원본
with open(r"C:\Users\chohy\Desktop\KNU\빅데이터분석실습\파이썬 Beginner 소스\CSV\singer1.csv", "r", encoding="cp949") as inFp:
    # csv 전용 파일로 변환
    csvReader = csv.reader(inFp)
    header = next(csvReader)        # 열제목이 있는 행을 리스트로 변환
    csvList.append(header)

    for row in csvReader:
        csvList.append(row)