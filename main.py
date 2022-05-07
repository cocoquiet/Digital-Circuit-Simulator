from tkinter import *
import tkinter.ttk as ttk
import tkinter.messagebox as msgbox

window = Tk()
window.title('digital circuit simulator')
window.geometry('640x400')
window.state('zoomed')
window.resizable(True, True)



# 논리 모델
basicModel = ['AND', 'OR', 'NOT', 'BUFFER', 'NAND', 'NOR', 'XOR', 'XNOR']

# 버튼 리스트
btnList = {}

# 버튼 연결 리스트
btnLinkList = []

# 버튼 연결 대기 리스트
btnLinkChkList = []



# 버튼 이벤트
def clickMap(event):
    listIndex = logicList.curselection()
    
    if listIndex == ():
        msgbox.showwarning('경고', '논리를 선택하지 않았습니다.')
    else:
        modelBtn = Button(mapCanvas, text=basicModel[listIndex[0]], width=16, height=4, command= lambda: [btnLinkChkList.append(modelBtn), connectBtn()])
        modelBtn.place(x=event.x, y=event.y, anchor='center')
        btnList[modelBtn] = (event.x, event.y)
        
        
def connectBtn():
    global btnLinkChkList
    if len(btnLinkChkList) == 2:
        btnLinkList.append(btnLinkChkList)
        mapCanvas.create_line(btnList[btnLinkChkList[0]][0], btnList[btnLinkChkList[0]][1], btnList[btnLinkChkList[1]][0], btnList[btnLinkChkList[1]][1], fill='blue')
        btnLinkChkList = []



# GUI 디자인
logicFrame = LabelFrame(window, text='logic', width=150, relief='groove')
logicFrame.pack(side='left', fill='both')

logicList_xScrollbar = Scrollbar(logicFrame, orient=HORIZONTAL)
logicList_yScrollbar = Scrollbar(logicFrame, orient=VERTICAL)
logicList_xScrollbar.pack(side='bottom', fill='x')
logicList_yScrollbar.pack(side='right', fill='y')

logicList = Listbox(logicFrame, selectmode='single', xscrollcommand=logicList_xScrollbar.set, yscrollcommand=logicList_yScrollbar.set)
logicList.pack(side='left', fill='both', expand=True)
logicList_xScrollbar.config(command=logicList.xview)
logicList_yScrollbar.config(command=logicList.yview)

for logic in basicModel:
    logicList.insert(END, logic)


mapFrame = LabelFrame(window, text='map', relief='groove')
mapFrame.pack(side='right', fill='both', expand=True)

mapCanvas_xScrollbar = Scrollbar(mapFrame, orient=HORIZONTAL)
mapCanvas_yScrollbar = Scrollbar(mapFrame, orient=VERTICAL)
mapCanvas_xScrollbar.pack(side='bottom', fill='x')
mapCanvas_yScrollbar.pack(side='right', fill='y')

mapCanvas = Canvas(mapFrame, bg='black', xscrollcommand=mapCanvas_xScrollbar.set, yscrollcommand=mapCanvas_yScrollbar.set)
mapCanvas.pack(side='left', fill='both', expand=True)
mapCanvas_xScrollbar.config(command=mapCanvas.xview)
mapCanvas_yScrollbar.config(command=mapCanvas.xview)
mapCanvas.focus_set()

mapCanvas.bind('<Button-1>', clickMap)


window.mainloop()