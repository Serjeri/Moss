from tkinter import *
from tkinter.ttk import Treeview


class ScrollableTreeViewComponent():

    grid = None

    def __init__(self, frameWin, headers: str, func):

        treeView = Treeview(frameWin, show='headings', columns=headers)
        self.treeView = treeView

        self.lastname_ent = Entry(frameWin)
        self.lastname_ent.pack()

        self.func = func

        view_window_btn1 = Button(frameWin, text='Поиск', command=self.search)
        view_window_btn1.pack()
        
        view_window_btn2 = Button(frameWin, text='Обновить', command=self.reset)
        view_window_btn2.pack()

        for header in headers:
            treeView.heading(header, text=header, anchor='center')
            treeView.column(header, anchor='center', minwidth=50, width=100)

        for row in func():
            treeView.insert('', END, values=row)

        scroll = Scrollbar(frameWin, command=treeView.yview)
        treeView.configure(yscrollcommand=scroll.set)

        scroll.pack(side=RIGHT, fill=BOTH)
        treeView.pack(expand=YES, fill=BOTH)

        self.grid = treeView

    def search(self):

        self.treeView.selection()
        fetchdata = self.treeView.get_children()

        for i in fetchdata:
            self.treeView.delete(i)

        for row in self.func(self.lastname_ent.get()):
            self.treeView.insert('', END, values=row)  

    def reset(self):
        self.lastname_ent.delete(0, END)
        self.lastname_ent.focus()
        self.treeView.selection()
        fetchdata = self.treeView.get_children()

        for i in fetchdata:
            self.treeView.delete(i)
        
        for row in self.func():
            self.treeView.insert("", END, values=row)
