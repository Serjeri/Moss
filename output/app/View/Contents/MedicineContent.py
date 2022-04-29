from tkinter import Label,Entry
from tkinter.ttk import Combobox
from tkcalendar import DateEntry


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

      self.time_of_injury = Entry(Lebleframe, textvariable='hhhh')
      self.time_of_injury.grid(row=1, column=1, pady=5, padx=3)

      self.date_of_receipt = DateEntry(Lebleframe,width=17,bg="darkblue",fg="white",year=2022)
      self.date_of_receipt.delete(0, "end")
      self.date_of_receipt.grid(row=2, column=1, pady=5, padx=3)

      self.time_of_arrival = Entry(Lebleframe)
      self.time_of_arrival.grid(row=3, column=1, pady=5, padx=3)

      self.circumstances = Entry(Lebleframe)
      self.circumstances.grid(row=4, column=1, pady=5, padx=3)

      self.type_of_injury = Combobox(Lebleframe,values=('ранение','заболевание',
      'травма','термическое','поражение химическое','поражение радиационное','поражение микст'),width=17, state='readonly')
      self.type_of_injury.grid(row=5, column=1, pady=5, padx=3)

      self.classification_code = Combobox(Lebleframe, values=self.MKB,width=17)
      self.classification_code.grid(row=0, column=3,pady=5, padx=3)

      self.preliminary_diagnosis = Entry(Lebleframe)
      self.preliminary_diagnosis.grid(row=1, column=3,pady=5, padx=3)

      self.diagnosis = Entry(Lebleframe)
      self.diagnosis.grid(row=2, column=3,pady=5, padx=3)

      self.severity_lesion = Combobox(Lebleframe,values=('легкая', 'средняя', 'тяжелая','крайне тяжелая'),width=17, state='readonly')
      self.severity_lesion.grid(row=3, column=3,pady=5, padx=3)

      self.medical = Entry(Lebleframe)
      self.medical.grid(row=4, column=3,pady=5, padx=3)

      self.wher = Combobox(Lebleframe,values=('ОАРИТ','ХО','ГО','ИИ','ПИ','амбулаторное лечение'),state='readonly')
      self.wher.grid(row=5, column=3,pady=5, padx=3)
      