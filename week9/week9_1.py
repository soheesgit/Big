inF = open('class.txt', 'r', encoding='utf-8')

str1 = inF.read()
print(str1, end="")
str2 = inF.readline()
print(str2, end="")
str3 = inF.readline()
print(str3, end="")
inF.close()