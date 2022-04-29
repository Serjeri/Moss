from tkinter import *
from tkinter.ttk import Treeview


class ScrollableTreeViewComponent():

    grid = None

    def __init__(self, frameWin, headers: str, func, deleteMethod):

        treeView = Treeview(frameWin, show='headings', columns=headers)
        self.treeView = treeView

        frameButton = LabelFrame(frameWin)
        frameButton.pack(fill=X)

        self.lastname_ent = Entry(frameButton)
        self.lastname_ent.pack(side=LEFT, padx=10, pady=10)

        self.func = func
        self.deleteMethod = deleteMethod

        searchButton = Button(frameButton, text='Поиск', command=self.search)
        searchButton.pack(side=LEFT,padx=10, pady=10)
        
        updateButton  = Button(frameButton, text='Обновить', command=self.reset)
        updateButton.pack(side=LEFT,padx=10, pady=10)

        deleteButton = Button(frameButton, text='Удалить', command=self.delete)
        deleteButton.pack(side=LEFT,padx=10, pady=10)
        
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

    def delete(self):
        self.treeView.selection()
        fetchdata = self.treeView.get_children()

        values = self.treeView.item(self.treeView.focus(), option="values")

        for i in fetchdata:
            self.treeView.delete(i)

        for row in self.func(self.deleteMethod(values[0])):
            self.treeView.insert("", END, values=row)
