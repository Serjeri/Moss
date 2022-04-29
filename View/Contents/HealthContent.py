from tkinter import *
from tkcalendar import DateEntry
from tkinter.ttk import Combobox
from ..Models.MedicalPrintModel import MedicalPrintModel


class HealthContent():

    def render(self,Lebleframe):

        Label(Lebleframe, text = 'Текущее состояние').grid(row=0, column=0, pady=5, padx=3)
        Label(Lebleframe, text = 'Дата перевода').grid(row=1, column=0,pady=5, padx=3)
        Label(Lebleframe, text = 'Время перевода').grid(row=2, column=0,pady=5, padx=3)
        Label(Lebleframe, text = 'Куда переведен(а)').grid(row=3, column=0,pady=5, padx=3)

        self.current_status = Combobox(Lebleframe,values=('удовлетворительное','тяжелое','крайне тяжелое'),width=17)
        self.current_status.grid(row=0, column=1,pady=5, padx=3)

        self.transfer_date = DateEntry(Lebleframe,width=17,bg="darkblue",fg="white",year=2022)
        self.transfer_date.delete(0, "end")
        self.transfer_date.grid(row=1, column=1, pady=5, padx=3)

        self.translation_time = Entry(Lebleframe)
        self.translation_time.grid(row=2, column=1, pady=5, padx=3)

        self.where_transferred = Combobox(Lebleframe,values=('ОАРИТ','ХО','ГО','ИИПИ','амбулаторное лечение'),width=19)
        self.where_transferred.grid(row=3, column=1, pady=5, padx=3)


    def get(self) -> MedicalPrintModel:
        return MedicalPrintModel(self.current_status.get(), self.transfer_date.get(), self.translation_time.get(), self.where_transferred.get())

    def set(self, model: MedicalPrintModel):
        
        self.current_status.delete(0,END)
        self.current_status.insert(0, model.condition)

        self.transfer_date.delete(0,END)
        self.transfer_date.insert(0, model.date)

        self.translation_time.delete(0,END)
        self.translation_time.insert(0, model.time)

        self.where_transferred.delete(0,END)
        self.where_transferred.insert(0, model.where)