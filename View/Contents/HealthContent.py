from tkinter import *
from tkcalendar import DateEntry
from tkinter.ttk import Combobox


class HealthContent():

    def render(self,Lebleframe):

        Label(Lebleframe, text = 'Текущее состояние').grid(row=0, column=0, pady=5, padx=3)
        Label(Lebleframe, text = 'Дата перевода').grid(row=1, column=0,pady=5, padx=3)
        Label(Lebleframe, text = 'Время перевода').grid(row=2, column=0,pady=5, padx=3)
        Label(Lebleframe, text = 'Куда переведен(а)').grid(row=3, column=0,pady=5, padx=3)

        self.current_status = Combobox(Lebleframe,values=('удовлетворительное','тяжелое','крайне тяжелое'),width=17, state='readonly')
        self.current_status.grid(row=0, column=1,pady=5, padx=3)

        self.transfer_date = DateEntry(Lebleframe,width=17,bg="darkblue",fg="white",year=2022)
        self.transfer_date.delete(0, "end")
        self.transfer_date.grid(row=1, column=1, pady=5, padx=3)

        self.translation_time = Entry(Lebleframe)
        self.translation_time.grid(row=2, column=1, pady=5, padx=3)

        self.where_transferred = Combobox(Lebleframe,values=('ОАРИТ','ХО','ГО','ИИПИ','амбулаторное лечение'),width=19, state='readonly')
        self.where_transferred.grid(row=3, column=1, pady=5, padx=3)
