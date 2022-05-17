from tkinter import END, Tk, Entry, Button,Label
from .Models.SpravkaSModel import SpravkaSModel
from View.DocumentView.PrintDocumentView import PrintDocumentView
 
 
class SpravkaSView:
     
    def __init__(self):
    
        win = Tk()
        title = "Экранная форма справки о гражданском лице, проходившем лечение в медо СпН"
        win.title(title)
        win.resizable(False, False)
        
        title = " СПРАВКА \n на лицо, проходившее лечение в медо СпН "

        header = ['№ п/п','Фамилия','Имя','Отчество','Окончательный диагноз','Категория гражданского лица',
        'Дата поступления ','Дата убытия ','Исход (состоя-ние) ']

        Label(win, text = '№ п/п').grid(row=0, column=0, sticky="w", pady=5)
        Label(win, text = 'Фамилия').grid(row=1, column=0, sticky="w", pady=5)
        Label(win, text = 'Имя').grid(row=2, column=0, sticky="w")
        Label(win, text = 'Отчество').grid(row=3, column=0, sticky="w")
        Label(win, text = 'Окончательный диагноз').grid(row=4, column=0, pady=5, padx=3,sticky="w")
        Label(win, text = 'Категория гражданского лица').grid(row=5, column=0, sticky="w")
        Label(win, text = 'Дата поступления ').grid(row=6, column=0,pady=5, padx=3,sticky="w")
        Label(win, text = 'Дата убытия ').grid(row=7, column=0,pady=5, padx=3,sticky="w")
        Label(win, text = 'Исход (состоя-ние) ').grid(row=8, column=0,pady=5, padx=3,sticky="w")


        self.id = Entry(win, width=25, font=('Arial',13,'bold'))
        self.id.grid(row=0, column=1)

        self.lastname = Entry(win, width=25, font=('Arial',13,'bold'))
        self.lastname.grid(row=1, column=1)

        self.name = Entry(win, width=25, font=('Arial',13,'bold'))
        self.name.grid(row=2, column=1)

        self.patronymic= Entry(win, width=25, font=('Arial',13,'bold'))
        self.patronymic.grid(row=3, column=1)

        self.diagnosis= Entry(win, width=25, font=('Arial',13,'bold'))
        self.diagnosis.grid(row=4, column=1)

        self.category = Entry(win, width=25, font=('Arial',13,'bold'))
        self.category.grid(row=5, column=1)

        self.date_of_receipt= Entry(win, width=25, font=('Arial',13,'bold'))
        self.date_of_receipt.grid(row=6, column=1)

        self.date_of_departure= Entry(win, width=25, font=('Arial',13,'bold'))
        self.date_of_departure.grid(row=7, column=1)

        self.exodus= Entry(win, width=25, font=('Arial',13,'bold'))
        self.exodus.grid(row=8, column=1)

        Button(win, text='Печать', command= lambda:PrintDocumentView().print_document(self.get_list,header, title)).grid(row=31, column=1, padx=10, sticky='se', pady=10)

    def get(self) -> SpravkaSModel:
        return SpravkaSModel( self.id.get(),self.lastname.get(),self.name.get(),self.patronymic.get(),
    self.diagnosis.get(),self.category.get(),self.date_of_receipt.get(),self.date_of_departure.get(),
    self.exodus.get())

    def get_list(self)-> list:
        return [self.id.get(),self.lastname.get(),self.name.get(),self.patronymic.get(),
    self.diagnosis.get(),self.category.get(),self.date_of_receipt.get(),self.date_of_departure.get(),
    self.exodus.get()]


    def set(self, model:SpravkaSModel):

        self.id.delete(0,END)
        self.id.insert(0, model.id)

        self.lastname.delete(0,END)
        self.lastname.insert(0, model.lastname)

        self.name.delete(0,END)
        self.name.insert(0, model.name)

        self.patronymic.delete(0,END)
        self.patronymic.insert(0, model.patronymic)

        self.diagnosis.delete(0,END)
        self.diagnosis.insert(0, model.diagnosis)

        self.category.delete(0,END)
        self.category.insert(0, model.category)

        self.date_of_receipt.delete(0,END)
        self.date_of_receipt.insert(0, model.date_of_receipt)

        self.date_of_departure.delete(0,END)
        self.date_of_departure.insert(0, model.date_of_departure)

        self.exodus.delete(0,END)
        self.exodus.insert(0, model.exodus)
