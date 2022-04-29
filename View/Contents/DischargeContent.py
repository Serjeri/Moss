from tkinter import Label,Entry, END
from tkcalendar import DateEntry
from tkinter.ttk import Combobox
from ..Models.DeparturePrintModel import DeparturePrintModel



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
        'летальный исход'),width=35)
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
        'авиационный санитарный транспорт', 'самостоятельно'),width=35)
        self.transport.grid(row=6, column=1, pady=5, padx=3)
        
    def get(self) -> DeparturePrintModel:
            return DeparturePrintModel(self.exodus.get(),self.date_of_departure.get(),self.time_of_departure.get(),
                        self.diagnosis_on_departure.get(),self.classification_code.get(),self.medical_care.get(),self.transport.get())

    def set(self, model: DeparturePrintModel):

        self.exodus.delete(0,END)
        self.exodus.insert(0, model.exodus)

        self.date_of_departure.delete(0,END)
        self.date_of_departure.insert(0, model.date_of_departure)

        self.time_of_departure.delete(0,END)
        self.time_of_departure.insert(0, model.time_of_departure)

        self.diagnosis_on_departure.delete(0,END)
        self.diagnosis_on_departure.insert(0, model.diagnosis_on_departure)

        self.classification_code.delete(0,END)
        self.classification_code.insert(0, model.classification_code)
        
        self.medical_care.delete(0,END)
        self.medical_care.insert(0, model.medical_care)

        self.transport.delete(0,END)
        self.transport.insert(0, model.transport)
