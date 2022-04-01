from tkinter import Label,Entry
from tkcalendar import DateEntry
from tkinter.ttk import Combobox



class DischargeContent():

    def render(self,Lebleframe):

        Label(Lebleframe, text = 'Исход').grid(row=0, column=0, pady=5, padx=3)
        Label(Lebleframe, text = 'Дата убытия').grid(row=1, column=0,pady=5, padx=3)
        Label(Lebleframe, text = 'Время убытия').grid(row=2, column=0,pady=5, padx=3)
        Label(Lebleframe, text = 'Диагноз при убытии').grid(row=3, column=0,pady=5, padx=3)
        Label(Lebleframe, text = 'Код по классификатору при убытии').grid(row=4, column=0,pady=5, padx=3)
        Label(Lebleframe, text = 'Оказанная медицинская помощь').grid(row=5, column=0,pady=5, padx=3)
        Label(Lebleframe, text = 'Каким транспортом убыл').grid(row=6, column=0, pady=5, padx=3)

        self.exodus = Combobox(Lebleframe, values=('выписка в часть', 
        'выписка на амбулаторное лечение', 'перевод в другое лечеб-ное учреждение', 
        'летальный исход'),width=35,state='readonly')
        self.exodus.grid(row=0, column=1,pady=5, padx=3)

        self.date_of_departure = DateEntry(Lebleframe,width=17,bg="darkblue",fg="white",year=2022)
        self.date_of_departure.delete(0, "end")
        self.date_of_departure.grid(row=1, column=1, pady=5, padx=3)

        self.time_of_departure = Entry(Lebleframe)
        self.time_of_departure.grid(row=2, column=1, pady=5, padx=3)

        self.diagnosis_on_departure = Entry(Lebleframe)
        self.diagnosis_on_departure.grid(row=3, column=1, pady=5, padx=3)

        self.classification_code = Entry(Lebleframe)
        self.classification_code.grid(row=4, column=1, pady=5, padx=3)

        self.medical_care = Entry(Lebleframe)
        self.medical_care.grid(row=5, column=1, pady=5, padx=3)

        self.transport = Combobox(Lebleframe,values=('наземный санитарный транспорт', 
        'авиационный санитарный транспорт', 'самостоятельно'),width=35,state='readonly')
        self.transport.grid(row=6, column=1, pady=5, padx=3)
        