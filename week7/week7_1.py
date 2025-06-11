'''
[메뉴 위젯 응용]
[File] 메뉴 - 서브메뉴 [불러오기]/[끝내기]
[불러오기]메뉴 클릭시 => 열기 대화상자, 선택한 이미지의 경로정보 라벨 출력
[끝내기] 메뉴 클릭시 => 윈도우 창 닫고, 자원 반납
'''

from tkinter import *
from tkinter.filedialog import *  # 대화상자 창


# [불러오기] 메뉴 선택 시 동작 함수
def FuncOpen():
    # "열기" 대화상자 실행     => askopenfilename()
    # "save as" 대화상자 실행 => asksaveasfile()
    fname = askopenfilename(parent=window)
    # 선택한 이미지파일이 라벨에 출력되도록
    photo = PhotoImage(file=fname)
    pLabel["image"] = photo
    pLabel.image = photo
    # 경로정보를 라벨에 출력
    pathLabel["text"] = fname


def FuncExit():  # [끝내기] 메뉴 클릭 시 동작 함수 - 외우기
    window.quit()
    window.destroy()


window = Tk()
window.geometry("500x500")
window.title("메뉴 만들기")
# 이미지 라벨 ---------------------------------------------------------
photo = PhotoImage()  # 이미지 담을 객체 생성
pLabel = Label(window, image=photo)  # 이미지 없는 라벨 출력
pLabel.pack(expand=1, anchor="center")  # 위에서 떨어트려 수평 중앙에 출력
# 메뉴 ---------------------------------------------------------------
mainMenu = Menu(window)  # 메뉴 영역 선언
window["menu"] = mainMenu  # 윈도우에 부착될 메뉴 연결
fileMenu = Menu(mainMenu)
mainMenu.add_cascade(label="파일", menu=fileMenu)  # 메뉴 영역에 중첩시켜 부착
# 서브메뉴 만들기
fileMenu.add_command(label="불러오기", command=FuncOpen)  # 파일메뉴에 부착
fileMenu.add_separator() #구분선
fileMenu.add_command(label="끝내기", command=FuncExit)  # 파일메뉴에 부착
# 라벨 생성 부착
pathLabel = Label(window, text="이곳에 선택한 파일의 정보가 출력됩니다.")
pathLabel.pack()

window.mainloop()
