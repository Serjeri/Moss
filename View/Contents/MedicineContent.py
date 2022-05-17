from tkinter import Label,Entry, END
from tkinter.ttk import Combobox
from tkcalendar import DateEntry
from ..Models.MedicineInfoModel import MedicineInfoModel

class MedicineContent():

    def __init__(self, MKB):
        self.MKB = MKB

    def render(self,Lebleframe):

        Label(Lebleframe, text = 'Дата ранения (заболевания, поражения)').grid(row=0, column=0, pady=5, padx=3)
        Label(Lebleframe, text = 'Время ранения (заболевания, поражения)').grid(row=1, column=0,pady=5, padx=3)
        Label(Lebleframe, text = 'Дата поступления (заболевания, поражения)').grid(row=2, column=0,pady=5, padx=3)
        Label(Lebleframe, text = 'Время поступления (заболевания, поражения)').grid(row=3, column=0,pady=5, padx=3)
        Label(Lebleframe, text = 'Обстоятельства ранения (заболевания, поражения)').grid(row=4, column=0,pady=5, padx=3)
        Label(Lebleframe, text = 'Вид поражения').grid(row=5, column=0,pady=5, padx=3)
        Label(Lebleframe, text = 'Код по классификатору').grid(row=0, column=2, pady=5, padx=3)
        Label(Lebleframe, text = 'Предварительный диагноз').grid(row=1, column=2, pady=5, padx=3)
        Label(Lebleframe, text = 'Окончательный диагноз').grid(row=2, column=2, pady=5, padx=3)
        Label(Lebleframe, text = 'Тяжесть поражения').grid(row=3, column=2, pady=5, padx=3)
        Label(Lebleframe, text = 'Медицинская помощь до поступления в омедо СпН').grid(row=4, column=2, pady=5, padx=3)
        Label(Lebleframe, text = 'Куда направлен(а)').grid(row=5, column=2, pady=5, padx=3)
      
        self.date_of_injury = DateEntry(Lebleframe, width=17,year=2022)
        self.date_of_injury.delete(0, "end")
        self.date_of_injury.grid(row=0, column=1,pady=5, padx=3)
    
        self.time_of_injury = Entry(Lebleframe)
        self.time_of_injury.grid(row=1, column=1, pady=5, padx=3)

        self.date_of_receipt = DateEntry(Lebleframe,width=17,bg="darkblue",fg="white",year=2022)
        self.date_of_receipt.delete(0, "end")
        self.date_of_receipt.grid(row=2, column=1, pady=5, padx=3)

        self.time_of_arrival = Entry(Lebleframe)
        self.time_of_arrival.grid(row=3, column=1, pady=5, padx=3)

        self.circumstances = Entry(Lebleframe)
        self.circumstances.grid(row=4, column=1, pady=5, padx=3)

        self.type_of_injury = Combobox(Lebleframe,values=('ранение','заболевание',
        'травма','термическое','поражение химическое','поражение радиационное','комбинированное поражение'),width=22)
        self.type_of_injury.grid(row=5, column=1, pady=5, padx=3) 

        self.classification_code = Combobox(Lebleframe, values=self.MKB,width=30)
        self.classification_code.grid(row=0, column=3,pady=5, padx=3)   

        self.preliminary_diagnosis = Entry(Lebleframe)
        self.preliminary_diagnosis.grid(row=1, column=3,pady=5, padx=3)

        self.diagnosis = Entry(Lebleframe)
        self.diagnosis.grid(row=2, column=3,pady=5, padx=3) 

        self.severity_lesion = Combobox(Lebleframe,values=('легкая', 'средняя', 'тяжелая','крайне тяжелая'),width=17)
        self.severity_lesion.grid(row=3, column=3,pady=5, padx=3)  

        self.medical = Entry(Lebleframe)
        self.medical.grid(row=4, column=3,pady=5, padx=3)

        self.wher = Combobox(Lebleframe,values=('ОАРИТ','ХО','ГО','ИИ','ПИ','амбулаторное лечение'))
        self.wher.grid(row=5, column=3,pady=5, padx=3)
      

    def get(self) -> MedicineInfoModel:
        return MedicineInfoModel(self.date_of_injury.get(),self.time_of_injury.get(),self.date_of_receipt.get(),
            self.time_of_arrival.get(),self.circumstances.get(),self.type_of_injury.get(), self.classification_code.get(),
            self.preliminary_diagnosis.get(),self.diagnosis.get(), self.severity_lesion.get(),
            self.medical.get(),self.wher.get())

    def set(self, model: MedicineInfoModel):

        self.date_of_injury.delete(0,END)
        self.date_of_injury.insert(0, model.date_of_injury)

        self.time_of_injury.delete(0,END)
        self.time_of_injury.insert(0, model.time_of_injury)

        self.date_of_receipt.delete(0,END)
        self.date_of_receipt.insert(0, model.date_of_receipt)

        self.time_of_arrival.delete(0,END)
        self.time_of_arrival.insert(0, model.time_of_arrival)

        self.circumstances.delete(0,END)
        self.circumstances.insert(0, model.circumstances)

        self.type_of_injury.delete(0,END)
        self.type_of_injury.insert(0, model.type_of_injury)

        self.classification_code.delete(0,END)
        self.classification_code.insert(0, model.classification_code)

        self.preliminary_diagnosis.delete(0,END)
        self.preliminary_diagnosis.insert(0, model.preliminary_diagnosis)

        self.diagnosis.delete(0,END)
        self.diagnosis.insert(0, model.diagnosis)

        self.severity_lesion.delete(0,END)
        self.severity_lesion.insert(0, model.severity_lesion)

        self.medical.delete(0,END)
        self.medical.insert(0, model.medical)

        self.wher.delete(0,END)
        self.wher.insert(0, model.wher)