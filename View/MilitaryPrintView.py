from tkinter import Label, Tk, Entry,END
from .Models.MilitaryPrintModel import MilitaryPrintModel
 
 
class MilitaryPrintView():
     
    def __init__(self):
    
        win = Tk()
        win.title("Карта исходных данных на военнослужащего")
        win.resizable(False, False)

        Label(win, text = 'Фамилия').grid(row=0, column=0, sticky="w", pady=5)
        Label(win, text = 'Имя').grid(row=1, column=0, sticky="w")
        Label(win, text = 'Отчество').grid(row=2, column=0, sticky="w")
        Label(win, text = 'Дата рождения').grid(row=3, column=0, sticky="w")
        Label(win, text = 'Пол').grid(row=4, column=0, sticky="w")
        Label(win, text = 'Категория').grid(row=5, column=0, sticky="w")
        Label(win, text = 'Группа крови').grid(row=6, column=0, sticky="w")
        Label(win, text = 'Резус-фактор').grid(row=7, column=0, sticky="w")
        Label(win, text = 'Сведения о прививках').grid(row=8, column=0, sticky="w")
        Label(win, text = 'Доза облучения').grid(row=9, column=0, sticky="w")
        Label(win, text = 'Хронические заболевания').grid(row=10, column=0, sticky="w")
        Label(win, text = 'Документ, удостоверяющий личность').grid(row=11, column=0, sticky="w")
        Label(win, text = 'Cерия').grid(row=12, column=0, sticky="w")
        Label(win, text = 'Номер').grid(row=13, column=0, sticky="w")
        Label(win, text = 'Ведомственная принадлежность').grid(row=14, column=0, pady=5, sticky="w")

        Label(win, text = 'Состав').grid(row=0, column=3, sticky="w")
        Label(win, text = 'Воинское звание').grid(row=1, column=3, sticky="w")
        Label(win, text = 'Личный номер').grid(row=2, column=3, sticky="w")
        Label(win, text = 'Должность').grid(row=3, column=3, sticky="w")
        Label(win, text = 'ВУС').grid(row=4, column=3, sticky="w")
        Label(win, text = 'Воинская часть').grid(row=5, column=3, sticky="w")
        Label(win, text = 'Дата ранения (заболевания, поражения)').grid(row=6, column=3, pady=5, padx=3,sticky="w")
        Label(win, text = 'Время ранения (заболевания, поражения)').grid(row=7, column=3,pady=5, padx=3,sticky="w")
        Label(win, text = 'Дата поступления (заболевания, поражения)').grid(row=8, column=3,pady=5, padx=3,sticky="w")
        Label(win, text = 'Время поступления (заболевания, поражения)').grid(row=9, column=3,pady=5, padx=3,sticky="w")
        Label(win, text = 'Обстоятельства ранения (заболевания, поражения)').grid(row=10, column=3,pady=5, padx=3,sticky="w")
        Label(win, text = 'Вид поражения').grid(row=11, column=3,pady=5, padx=3,sticky="w")
        Label(win, text = 'Код по классификатору').grid(row=12, column=3, pady=5, padx=3,sticky="w")
        Label(win, text = 'Предварительный диагноз').grid(row=13, column=3, pady=5, padx=3,sticky="w")
        Label(win, text = 'Тяжесть поражения').grid(row=14, column=3, pady=5, padx=3,sticky="w")
        Label(win, text = 'Медицинская помощь до поступления в омедо СпН').grid(row=15, column=3, pady=5, padx=3,sticky="w")
        Label(win, text = 'Куда направлен(а)').grid(row=16, column=3, pady=5, padx=3,sticky="w")

        self.lastname = Entry(win, width=25, font=('Arial',13,'bold'))
        self.lastname.grid(row=0, column=1)

        self.name = Entry(win, width=25, font=('Arial',13,'bold'))
        self.name.grid(row=1, column=1)

        self.patronymic = Entry(win, width=25, font=('Arial',13,'bold'))
        self.patronymic.grid(row=2, column=1)

        self.date_of_birth= Entry(win, width=25, font=('Arial',13,'bold'))
        self.date_of_birth.grid(row=3, column=1)

        self.gender= Entry(win, width=25, font=('Arial',13,'bold'))
        self.gender.grid(row=4, column=1)

        self.category = Entry(win, width=25, font=('Arial',13,'bold'))
        self.category.grid(row=5, column=1)

        self.blood_type= Entry(win, width=25, font=('Arial',13,'bold'))
        self.blood_type.grid(row=6, column=1)

        self.rh_factor= Entry(win, width=25, font=('Arial',13,'bold'))
        self.rh_factor.grid(row=7, column=1)

        self.information= Entry(win, width=25, font=('Arial',13,'bold'))
        self.information.grid(row=8, column=1)

        self.exposure_dose= Entry(win, width=25, font=('Arial',13,'bold'))
        self.exposure_dose.grid(row=9, column=1)

        self.Chronic_diseases= Entry(win, width=25, font=('Arial',13,'bold'))
        self.Chronic_diseases.grid(row=10, column=1)

        self.Identity_document= Entry(win, width=25, font=('Arial',13,'bold'))
        self.Identity_document.grid(row=11, column=1)

        self.series= Entry(win, width=25, font=('Arial',13,'bold'))
        self.series.grid(row=12, column=1)

        self.number= Entry(win, width=25, font=('Arial',13,'bold'))
        self.number.grid(row=13, column=1)

        self.departmental_affiliation = Entry(win, width=25, font=('Arial',13,'bold'))
        self.departmental_affiliation.grid(row=14, column=1)

        self.composition= Entry(win, width=25, font=('Arial',13,'bold'))
        self.composition.grid(row=0, column=4)

        self.military_rank= Entry(win, width=25, font=('Arial',13,'bold'))
        self.military_rank.grid(row=1, column=4)
 
        self.personal_number= Entry(win, width=25, font=('Arial',13,'bold'))
        self.personal_number.grid(row=2, column=4)

        self.position = Entry(win, width=25, font=('Arial',13,'bold'))
        self.position.grid(row=3, column=4)

        self.vus = Entry(win, width=25, font=('Arial',13,'bold'))
        self.vus.grid(row=4, column=4)

        self.military_unit = Entry(win, width=25, font=('Arial',13,'bold'))
        self.military_unit.grid(row=5, column=4)

        self.date_of_injury = Entry(win, width=25, font=('Arial',13,'bold'))
        self.date_of_injury.grid(row=6, column=4)

        self.time_of_injury= Entry(win, width=25, font=('Arial',13,'bold'))
        self.time_of_injury.grid(row=7, column=4)

        self.date_of_receipt= Entry(win, width=25, font=('Arial',13,'bold'))
        self.date_of_receipt.grid(row=8, column=4)

        self.time_of_arrival= Entry(win, width=25, font=('Arial',13,'bold'))
        self.time_of_arrival.grid(row=9, column=4)

        self.circumstances= Entry(win, width=25, font=('Arial',13,'bold'))
        self.circumstances.grid(row=10, column=4)

        self.type_of_injury= Entry(win, width=25, font=('Arial',13,'bold'))
        self.type_of_injury.grid(row=11, column=4)

        self.classification_code= Entry(win, width=25, font=('Arial',13,'bold'))
        self.classification_code.grid(row=12, column=4)

        self.diagnosis= Entry(win, width=25, font=('Arial',13,'bold'))
        self.diagnosis.grid(row=13, column=4)

        self.severity_lesion= Entry(win, width=25, font=('Arial',13,'bold'))
        self.severity_lesion.grid(row=14, column=4)

        self.medical= Entry(win, width=25, font=('Arial',13,'bold'))
        self.medical.grid(row=15, column=4)

        self.wher= Entry(win, width=25, font=('Arial',13,'bold'))
        self.wher.grid(row=16, column=4)


    def get(self) -> MilitaryPrintModel:
        return MilitaryPrintModel(self.lastname.get(),self.name.get(),self.patronymic.get(),self.date_of_birth.get(),
            self.gender.get(),self.category.get(),self.blood_type.get(),self.rh_factor.get(),self.information.get(),
            self.exposure_dose.get(),self.Chronic_diseases.get(),self.Identity_document.get(),self.series.get(),
            self.number.get(),self.departmental_affiliation.get(),self.composition.get(),self.military_rank.get(),
            self.personal_number.get(),self.position.get(),self.vus.get(),self.military_unit.get(),self.date_of_injury.get(),
            self.time_of_injury.get(),self.date_of_receipt.get(),self.time_of_arrival.get(),self.circumstances.get(),
            self.type_of_injury.get(), self.classification_code.get(),self.diagnosis.get(),self.severity_lesion.get(),
            self.medical.get(),self.wher.get())

    def set(self, model: MilitaryPrintModel):

        self.lastname.delete(0,END)
        self.lastname.insert(0, model.lastname)

        self.name.delete(0,END)
        self.name.insert(0, model.name)

        self.patronymic.delete(0,END)
        self.patronymic.insert(0, model.patronymic)

        self.date_of_birth.delete(0,END)
        self.date_of_birth.insert(0, model.date_of_birth)

        self.gender.delete(0,END)
        self.gender.insert(0, model.gender)
        
        self.category.delete(0,END)
        self.category.insert(0, model.category)

        self.blood_type.delete(0,END)
        self.blood_type.insert(0, model.blood_type)

        self.rh_factor.delete(0,END)
        self.rh_factor.insert(0, model.rh_factor)

        self.information.delete(0,END)
        self.information.insert(0, model.information)

        self.exposure_dose.delete(0,END)
        self.exposure_dose.insert(0, model.exposure_dose)

        self.Chronic_diseases.delete(0,END)
        self.Chronic_diseases.insert(0, model.Chronic_diseases)

        self.Identity_document.delete(0,END)
        self.Identity_document.insert(0, model.Identity_document)

        self.series.delete(0,END)
        self.series.insert(0, model.series)

        self.number.delete(0,END)
        self.number.insert(0, model.number)

        self.departmental_affiliation.delete(0,END)
        self.departmental_affiliation.insert(0, model.departmental_affiliation)

        self.composition.delete(0,END)
        self.composition.insert(0, model.composition)

        self.military_rank.delete(0,END)
        self.military_rank.insert(0, model.military_rank)

        self.personal_number.delete(0,END)
        self.personal_number.insert(0, model.personal_number)

        self.position.delete(0,END)
        self.position.insert(0, model.position)

        self.vus.delete(0,END)
        self.vus.insert(0, model.vus)

        self.military_unit.delete(0,END)
        self.military_unit.insert(0, model.military_unit)

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

        self.diagnosis.delete(0,END)
        self.diagnosis.insert(0, model.diagnosis)

        self.severity_lesion.delete(0,END)
        self.severity_lesion.insert(0, model.severity_lesion)

        self.medical.delete(0,END)
        self.medical.insert(0, model.medical)

        self.wher.delete(0,END)
        self.wher.insert(0, model.wher)
