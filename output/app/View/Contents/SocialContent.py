from tkinter import Label,Entry
from tkinter.ttk import Combobox


class SocialContent():

    def render(self,Lebleframe):

        Label(Lebleframe, text = 'Семейное положение').grid(row=3, column=0, pady=5, sticky="w")
        Label(Lebleframe, text = 'Категория гражд. лица').grid(row=9, column=0, sticky="w")
        Label(Lebleframe, text = 'Место проживания').grid(row=15, column=0, sticky="w")
        Label(Lebleframe, text = 'Должность').grid(row=21, column=0, sticky="w")
        Label(Lebleframe, text = 'Специальность').grid(row=27, column=0, sticky="w")

        self.Marital_status = Entry(Lebleframe)
        self.Marital_status.grid(row=6, column=0, sticky="w", padx=10, pady=2)

        self.Category = Combobox(Lebleframe,values = ('ЧСВ','военный пенсионер',
        'военнопленный','ГП МО РФ','прочие'), state='readonly',width=20)
        self.Category.grid(row=10, column=0, sticky="w",padx=10 ,pady=2)

        self.Place_of_residence = Entry(Lebleframe)
        self.Place_of_residence.grid(row=16, column=0, sticky="w",padx=10,pady=2)

        self.Position = Entry(Lebleframe)
        self.Position.grid(row=22, column=0, sticky="w",padx=10,pady=2)

        self.Specialty = Entry(Lebleframe)
        self.Specialty.grid(row=28, column=0, sticky="w",padx=10,pady=5)
