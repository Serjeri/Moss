from tkinter import Tk, Entry, Button, Label, END
from .Models.MedicalPrintModel import MedicalPrintModel

 
class MedicalPrintView:

    def __init__(self):

        win = Tk()
        win.title("Карта текущей медицинской информации")
        win.resizable(False, False)

        Label(win, text = 'Текущее состояние').grid(row=0, column=0, pady=5, padx=3)
        Label(win, text = 'Дата перевода' ).grid(row=1, column=0, pady=5, padx=3)
        Label(win, text = 'Время перевода').grid(row=2, column=0, pady=5, padx=3)
        Label(win, text = 'Куда переведен(а)').grid(row=3, column=0,pady=5, padx=3)
        
        self.condition = Entry(win, width=25, font=('Arial',13,'bold'))
        self.condition.grid(row=0, column=1)

        self.date = Entry(win, width=25, font=('Arial',13,'bold'))
        self.date.grid(row=1, column=1,padx=10, pady=5)

        self.time = Entry(win, width=25, font=('Arial',13,'bold'))
        self.time.grid(row=2, column=1,padx=10, pady=5)

        self.where = Entry(win, width=25, font=('Arial',13,'bold'))
        self.where.grid(row=3, column=1, padx=10, pady=5)
  
        Button(win, text='Распичатать').grid(row=4, column=1, padx=30,pady=15)

    def get(self) -> MedicalPrintModel:
        return MedicalPrintModel(self.condition.get(), self.date.get(), self.time.get(), self.where.get())

    def set(self, model: MedicalPrintModel):

        self.condition.delete(0,END)
        self.condition.insert(0, model.condition)

        self.date.delete(0,END)
        self.date.insert(0, model.date)

        self.time.delete(0,END)
        self.time.insert(0, model.time)

        self.where.delete(0,END)
        self.where.insert(0, model.where)
