# 원본 파일 열기(r), 결과 파일 열기(w)
inFile = open("test.txt", "r", encoding='utf-8')
outFile = open("result.txt", "w", encoding='utf-8')

# 학생수만큼 읽어와 정수형으로 변환해 총점 누적
sum = 0
cnt = 0 # 총점 변수, 학생 수 0으로 초기화
line = inFile.readline()  # 첫 번째 줄 읽어오기 => 문자열
while line != "":
    sum += int(line)  # 총점 누적
    cnt += 1  # 학생 수 누적
    line = inFile.readline()  # 두 번째 줄 읽어오기

# 총점과 평균을 파일에 쓰기
outFile.write("총점 = " + str(sum) + "점\n")
outFile.write("수강자 수 = " + str(cnt) + "명\n")
outFile.write("과목 평균 = " + str(sum / cnt) + "점\n")

# 파일 2개 닫기
inFile.close()
outFile.close()
