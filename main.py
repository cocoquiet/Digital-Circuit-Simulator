from tkinter import *
import tkinter.ttk as ttk
import tkinter.messagebox as msgbox
import tkinter.font as font

window = Tk()
window.title('digital circuit simulator')
window.geometry('640x400')
window.state('zoomed')
window.resizable(True, True)



# 논리 모델
basicModel = ['AND', 'OR', 'NOT', 'BUFFER', 'NAND', 'NOR', 'XOR', 'XNOR']

btnList = {}                    # 버튼 리스트
btnConnectList = []             # 버튼 연결 리스트
btnConnectWaitList = []         # 버튼 연결 대기 리스트
btnConnectLineList = []         # 버튼 연결 선 리스트



# 버튼 이벤트
def clickMap(event):
    listIndex = logicList.curselection()
    
    if listIndex == ():
        msgbox.showwarning('경고', '논리를 선택하지 않았습니다.')
    else:
        modelBtn = Button(mapCanvas, text=basicModel[listIndex[0]], width=16, height=4, command= lambda: [highlightBtn(modelBtn), connectBtn(event, modelBtn)])
        modelBtn.place(x=event.x, y=event.y, anchor='center')
        btnList[modelBtn] = (event.x, event.y)
        
        

def highlightBtn(btn):
    btn['font'] = font.Font(weight='bold')
        
        
def connectBtn(event, btn):
    global btnConnectWaitList 
    
    btnConnectWaitList.append(btn)
    
    if btnConnectWaitList[0] == btnConnectWaitList[1]:
        btnConnectWaitList = []
    
    else:
        if len(btnConnectWaitList) == 2:
            if btnConnectWaitList in btnConnectList:
                mapCanvas.delete(btnConnectLineList[btnConnectList.index(btnConnectWaitList)])
                del btnConnectLineList[btnConnectList.index(btnConnectWaitList)]
                btnConnectList.remove(btnConnectWaitList)
                btnConnectWaitList = []
                
            elif btnConnectWaitList[::-1] in btnConnectList:
                mapCanvas.delete(btnConnectLineList[btnConnectList.index(btnConnectWaitList[::-1])])
                del btnConnectLineList[btnConnectList.index(btnConnectWaitList[::-1])]
                btnConnectList.remove(btnConnectWaitList[::-1])
                btnConnectWaitList = []
                
            else:
                btnConnectList.append(btnConnectWaitList)
                btnConnectLineList.append(mapCanvas.create_line(btnList[btnConnectWaitList[0]][0], btnList[btnConnectWaitList[0]][1], btnList[btnConnectWaitList[1]][0], btnList[btnConnectWaitList[1]][1], fill='blue', width=5))
                btnConnectWaitList = []



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