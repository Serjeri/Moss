from tkinter import *
from tkinter.ttk import Notebook


class TabsComponent():

    frameContent = []

    def __init__(self,tab_one, title:str, header: list):
        
        labelFrame = LabelFrame(tab_one, text= title)
        labelFrame.pack(side=LEFT, fill=BOTH, expand=TRUE)
        notebook = Notebook(labelFrame)

        for i in range(len(header)) :
            frameWin = Frame(notebook)
            notebook.add(frameWin, text=header[i])
            self.frameContent.append(frameWin)
        notebook.pack( fill=BOTH, expand=TRUE )
