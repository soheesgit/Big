# 파일 열기 : open()
inF = open(r"C:\Users\chohy\Documents\asdf.txt", "r", encoding="ansi")

# 한 줄씩 읽어와 콘솔에 출력
str1 = inF.readline()
print(str1, end="")
str1 = inF.readline()
print(str1, end="")
str1 = inF.readline()
print(str1, end="")

# 파일 닫기 : close()
inF.close()
