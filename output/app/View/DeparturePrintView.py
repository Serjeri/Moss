from tkinter import Label, Tk, Entry, Button,END
from .Models.DeparturePrintModel import DeparturePrintModel
 
 
class DeparturePrintView:

    def __init__(self):

        win = Tk()
        win.title("Карта медицинских данных при убытии")
        win.resizable(False, False)

        Label(win, text = 'Исход').grid(row=0, column=0, pady=5, padx=3)
        Label(win, text = 'Дата убытия').grid(row=1, column=0,pady=5, padx=3)
        Label(win, text = 'Время убытия').grid(row=2, column=0,pady=5, padx=3)
        Label(win, text = 'Диагноз при убытии').grid(row=3, column=0,pady=5, padx=3)
        Label(win, text = 'Код по классификатору при убытии').grid(row=4, column=0,pady=5, padx=3)
        Label(win, text = 'Оказанная медицинская помощь').grid(row=5, column=0,pady=5, padx=3)
        Label(win, text = 'Каким транспортом убыл').grid(row=6, column=0, pady=5, padx=3)

        self.exodus = Entry(win, width=25, font=('Arial',13,'bold'))
        self.exodus.grid(row=0, column=1)
        
        self.date_of_departure = Entry(win, width=25, font=('Arial',13,'bold'))
        self.date_of_departure.grid(row=1, column=1)

        self.time_of_departure = Entry(win, width=25, font=('Arial',13,'bold'))
        self.time_of_departure.grid(row=2, column=1)

        self.diagnosis_on_departure = Entry(win, width=25, font=('Arial',13,'bold'))
        self.diagnosis_on_departure.grid(row=3, column=1)
        
        self.classification_code = Entry(win, width=25, font=('Arial',13,'bold'))
        self.classification_code.grid(row=4, column=1)

        self.medical_care = Entry(win, width=25, font=('Arial',13,'bold'))
        self.medical_care.grid(row=5, column=1)

        self.transport = Entry(win, width=25, font=('Arial',13,'bold'))
        self.transport.grid(row=6, column=1)

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
        