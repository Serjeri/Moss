from tkinter import Label, Entry
from tkcalendar import DateEntry
from tkinter.ttk import Combobox


class RegistrationContent():

    def render(self,Lebleframe):
        
        Label(Lebleframe, text = 'Фамилия').grid(row=3, column=0, sticky="w", pady=5)
        Label(Lebleframe, text = 'Имя').grid(row=9, column=0, sticky="w")
        Label(Lebleframe, text = 'Отчество').grid(row=15, column=0, sticky="w")
        Label(Lebleframe, text = 'Дата рождения').grid(row=21, column=0, sticky="w")
        Label(Lebleframe, text = 'Пол').grid(row=27, column=0, sticky="w")
        Label(Lebleframe, text = 'Категория').grid(row=33, column=0, sticky="w")
        Label(Lebleframe, text = 'Группа крови').grid(row=39, column=0, sticky="w")
        Label(Lebleframe, text = 'Резус-фактор').grid(row=3, column=1, sticky="w")
        Label(Lebleframe, text = 'Сведения о прививках').grid(row=9, column=1, sticky="w")
        Label(Lebleframe, text = 'Доза облучения').grid(row=15, column=1, sticky="w")
        Label(Lebleframe, text = 'Хронические заболевания').grid(row=21, column=1, sticky="w")
        Label(Lebleframe, text = 'Документ, удостоверяющий личность').grid(row=27, column=1, sticky="w")
        Label(Lebleframe, text = 'Cерия').grid(row=33, column=1, sticky="w")
        Label(Lebleframe, text = 'Номер').grid(row=39, column=1, sticky="w")

        self.lastname = Entry(Lebleframe)
        self.lastname.grid(row=6, column=0, sticky="w", padx=10, pady=2)

        self.name = Entry(Lebleframe)
        self.name.grid(row=10, column=0, sticky="w",padx=10 ,pady=2)

        self.patronymic = Entry(Lebleframe)
        self.patronymic.grid(row=16, column=0, sticky="w",padx=10,pady=2)

        self.date_of_birth = DateEntry(Lebleframe,width=17,bg="darkblue",fg="white",year=2022)
        self.date_of_birth.delete(0, "end")
        self.date_of_birth.grid(row=22, column=0, sticky="w",padx=10,pady=2)

        self.gender = Combobox(Lebleframe,values=('М','Ж'),width=17, state='readonly')
        self.gender.grid(row=28, column=0, sticky="w",padx=10,pady=2)

        self.category = Combobox(Lebleframe,values=('рядовой К','рядовой П','ержант К','сержант П','прапорщик',
        'младший офицер','старший офицер','генерал'),width=17, state='readonly')
        self.category.grid(row=34, column=0, sticky="w",padx=10,pady=2)

        self.blood_type = Combobox(Lebleframe,values=('I(0)','II(A)','III(B)','IV(AB)'),width=17, state='readonly')
        self.blood_type.grid(row=40, column=0, sticky="w",padx=10,pady=5)

        self.rh_factor = Combobox(Lebleframe,values=('+','-'),width=17, state='readonly')
        self.rh_factor.grid(row=6, column=1, sticky="w",padx=10,pady=2)

        self.information = Entry(Lebleframe)
        self.information.grid(row=10, column=1, sticky="w",padx=10,pady=2)

        self.exposure_dose = Entry(Lebleframe)
        self.exposure_dose.grid(row=16, column=1, sticky="w",padx=10,pady=2)

        self.Chronic_diseases = Entry(Lebleframe)
        self.Chronic_diseases.grid(row=22, column=1, sticky="w",padx=10,pady=2)

        self.Identity_document = Entry(Lebleframe)
        self.Identity_document.grid(row=28, column=1, sticky="w",padx=10,pady=2)

        self.series = Entry(Lebleframe)
        self.series.grid(row=34, column=1, sticky="w",padx=10,pady=2)

        self.number = Entry(Lebleframe)
        self.number.grid(row=40, column=1, sticky="w", pady=5,padx=10)
