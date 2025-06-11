'''
[리스트와 6개의 gif 이미지, 버튼 활용]
[이전] 버튼 [다음] 버튼과 리스트의 0번방의 이미지가 출력
[다음] 버튼 => 인덱스번호 0-1-2-3-4-5-0으로 초기화
[이전] 버튼 => 3번방의 이미지 3->2->1->0->5로 설정 ******주는문제*****
'''
from tkinter import *

fname =["7s0.gif", "7s1.gif", "7s2.gif", "7s3.gif", "7s4.gif", "7s5.gif", "7s6.gif"]
num = 0 #초기 인덱스 번호 = 0

def FuncNext(): # [다음] 버튼 눌렀을 때, 동작 함수
    global num
    num += 1 #방번호 증가

    if num>6: #7번째 이미지는 6번방!
        num = 0
    #인덱스 번호에 해당하는 이미지를 라벨에 줄력
    photo = PhotoImage(file="E:/3-1/빅분실/파이썬 모음/week7/" + fname[num])
    pLabel["image"] = photo # 화면에 보여줄
    pLabel.image = photo

def FuncPrev():
    global num
    num -= 1 #방번호 감소

    if num<0:
        num = 6
        #인덱스 번호에 해당하는 이미지를 라벨에 줄력
    photo = PhotoImage(file="E:/3-1/빅분실/파이썬 모음/week7/" + fname[num])
    pLabel["image"] = photo
    pLabel.image = photo

window = Tk()
window.geometry("600x600")
window.title("사진 앨범 만들기")

#[이전] [다음] 버튼 생성하여 부착
prevBtn = Button(window, text="이전", width=10, command=FuncPrev);
nextBtn = Button(window, text="다음", width=10, command=FuncNext);
prevBtn.place(x=200, y=30)
nextBtn.place(x=270, y=30)
#이미지 갖는 라벨 생성하여 부착
photo = PhotoImage(file="E:/3-1/빅분실/파이썬 모음/week7/" + fname[num])
pLabel = Label(window, image=photo)
pLabel.place(x=150, y=80)

window.mainloop()