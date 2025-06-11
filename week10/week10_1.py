import csv
from tkinter import *

# 빈 엔트리 위젯으로 형성된 2차원 리스트 만드는 함수
def EmptyMake(r, c):
    resultList = [] #결과로 반환될 빈 리스트 생성

    for i in range(0, r): # 모든 행
        tempList = [] #열 개수만큼 빈 엔트리가 저장될 1차원 리스트
        for j in range(0, c): # 모든 열
            e1 = Entry(window, text="", width=10) # 모든 엔트리의 너비 균일하게
            e1.grid(row=i, column=j) # 윈도우에 부착될 위치
            tempList.append(e1) # 빈 엔트리를 1차원 리스트에 추가
            # 한 행이 완성되었으면 2차원 리스트에 추가
        resultList.append(tempList)

    return resultList # 리스트를 반환

window = Tk()
csvList = []
workSheet = []

with open("singer1.csv", 'r') as inFp:
    # 온전한 csv 파일로 변환하기
    csvFile = csv.reader(inFp)
    header = next(csvFile) #열 제목 읽어와 리스트로 저장
    csvList.append(header)

    for row in csvFile: #파일의 순수 데이터행을 읽어와 리스트에 저장
        csvList.append(row)
    # 원본 csvList 2차원 리스트가 완성됨 ------------------------------------------------

    rowCnt = len(csvList)
    colCnt = len(csvList[0])

    workSheet = EmptyMake(rowCnt, colCnt)

    # 끝에서 두번째 열의 값이 167 이상이면 모든 열의 배경색을 "노랑" 설정
    idx = -2
    # csvList의 데이터를 workSheet 리스트로 옮기기
    for i in range(0, rowCnt):
        for j in range(0, colCnt):
            if csvList[i][idx].isnumeric(): #끝에서 두번째 열이 수치데이터인가
                if int(csvList[i][idx]) >= 167:
                    a = workSheet[i][j] #a = 빈엔트리
                    a.configure(bg="yellow")

            # [2] 인덱스 2번인 값에서 인원이 7명 이상인 셀만 배경을 pink로 설정
            if csvList[i][2].isnumeric(): #2번 열의 값이 수치데이터라면
                if (int(csvList[i][2]) >= 7):
                    b = workSheet[i][2]
                    b.configure(bg="pink")

            # [3] 인덱스 3번인 열, 즉 주소가 "서울"이라면 글씨색 blue로 설정
            # if csvList[i][3] is not None: # 값이 비어있지 않다면
            if csvList[i][3] != None: # 값이 비어있지 않다면
                if (csvList[i][3] == "서울"):
                    c = workSheet[i][3]
                    c.configure(fg="blue")

            workSheet[i][j].insert(0, csvList[i][j])
window.mainloop()