def showList(hList):
    for data in hList:
        print(data, end="\t")
    print()

# 엑셀에서 csv로 저장한 파일은 기본적으로 cp949로 저장된다고 함
with open(r"C:\Users\chohy\Desktop\KNU\빅데이터분석실습\파이썬 Beginner 소스\CSV\singer1.csv", "r", encoding="cp949") as inFp:
    with open(r"C:\Users\chohy\Desktop\KNU\빅데이터분석실습\singerOver165.csv", "w", encoding="cp949") as outFp:   # with는 close할 필요 x
        header = inFp.readline()        # 첫 번째 줄 읽어오기
        header = header.strip()     # 열이름 앞뒤의 공백 제거
        headerList = header.split(',')
        # showList(headerList)      # 콘솔에 출력

        # 평균키의 열번호 알아내기
        cmNo = headerList.index("평균 키")
        # 데뷔 일자의 열번호 알아내기
        yearNo = headerList.index("데뷔 일자")

        # 출력할 열 제목만 재구성
        headerList = [headerList[0], headerList[1], headerList[cmNo], headerList[yearNo]]

        headerStr = ",".join(map(str, headerList))      # 콤마로 연결. 헤더리스트를 스트링으로 매핑
        outFp.write(headerStr + "\n")

        for data in inFp:
            inStr = data.strip()
            row = inStr.split(',')
            # showList(row)

            '''
            # 마지막 열의 데뷔년도에서 '.'을 '/'로 교체
            row[-1] = row[-1].replace('.', '/')

            # 끝에서 두번쨰 열(평균키) 소숫점 첫째 자리까지만 출력
            cm = "{0:.1f}".format(float(row[-2])) # 원래 string이니까 float로 실수로 변경해야 함
            row[-2] = cm
            '''

            # 평균 키가 165 이상인 데이터 추출
            if int(row[cmNo]) >= 165:   # sting이니까 int로 변환
                # 출력할 열 데이터 재구성
                rowList = [row[0], row[1], row[cmNo], row[yearNo]]
                rowStr = ",".join(map(str, rowList))
                outFp.write(rowStr + "\n")

