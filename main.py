from tkinter import *
import tkinter.ttk as ttk

window = Tk()
window.title('digital circuit simulator')
window.geometry('640x400')
window.state('zoomed')
window.resizable(True, True)

logicBox = LabelFrame(window, text='logic', takefocus=True, width=200, relief='groove').pack(side='left', fill='y')


mapBox = LabelFrame(window, text='map', takefocus=True, relief='groove').pack(fill='both', expand=True)




window.mainloop()