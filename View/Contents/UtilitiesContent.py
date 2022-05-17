from tkinter import Label, Entry
from tkinter.ttk import Combobox

class UtilitiesContent():
        
    def render(self,Lebleframe):

        Label(Lebleframe, text = 'Ведомственная принадлежность').grid(row=3, column=0, sticky="w", pady=5)
        Label(Lebleframe, text = 'Состав').grid(row=9, column=0, sticky="w")
        Label(Lebleframe, text = 'Воинское звание').grid(row=15, column=0, sticky="w")
        Label(Lebleframe, text = 'Личный номер').grid(row=21, column=0, sticky="w")
        Label(Lebleframe, text = 'Должность').grid(row=27, column=0, sticky="w")
        Label(Lebleframe, text = 'ВУС').grid(row=33, column=0, sticky="w")
        Label(Lebleframe, text = 'Воинская часть').grid(row=39, column=0, sticky="w")

        self.departmental_affiliation = Combobox(Lebleframe,values=('МО','ВНГ','другие'),width=9, state='readonly')
        self.departmental_affiliation.grid(row=6, column=0, sticky="w", padx=10, pady=2)

        self.composition = Combobox(Lebleframe,values=('командный','инженерный',
        'воспитательный','тыловой','медицинский','вете-ринарный'),width=17, state='readonly')
        self.composition.grid(row=10, column=0, sticky="w",padx=10 ,pady=2)

        self.military_rank = Combobox(Lebleframe,values=('рядовой','матрос',
        'ефрейтор','ст. матрос','мл. с-т','ст. 2 статьи','с-т','старшина 1 статьи',
        'ст. сержант','гл. кор. старшина','прапоршик','мичман','ст прапорщик','ст мичман','лейтенант','ст. лейтенант',
        'капитан','капитан-лейтенант','майор','капитан 3 ранга','подполковник',
        'капитан 2 ранга','полковник','капитан 1 ранга','генерал-майор','контр-адмирал',
        'генерал-лейтенант',' вице-адмирал','генерал-полковник','адмирал'),width=17, state='readonly')
        self.military_rank.grid(row=16, column=0, sticky="w",padx=10,pady=2)

        self.personal_number = Entry(Lebleframe)
        self.personal_number.grid(row=22, column=0, sticky="w",padx=10,pady=2)

        self.position = Entry(Lebleframe)
        self.position.grid(row=28, column=0, sticky="w",padx=10,pady=2)

        self.vus = Entry(Lebleframe)
        self.vus.grid(row=34, column=0, sticky="w",padx=10,pady=5)

        self.military_unit = Entry(Lebleframe)
        self.military_unit.grid(row=40, column=0, sticky="w",padx=10,pady=5)