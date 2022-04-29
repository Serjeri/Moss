from tkinter import Button
from View.CivilPrintView import CivilPrintView
from View.MilitaryPrintView import MilitaryPrintView
from View.MedicalPrintView import MedicalPrintView
from View.DeparturePrintView import DeparturePrintView
from View.SpravkaSView import SpravkaSView
from View.SpravkaMView import SpravkaMView
from Service.Service import Service


class ButtonPrintView():

    def __init__(self, id: int, service: Service):
        self.id = id
        self.service = service

    def render(self, Lebleframe):

        Button(Lebleframe, text='Карта исходных данных\n на гражданское лицо', command= lambda: CivilPrintView().set(self.service.select_conclusion_s(self.id))).grid(row=0,column=6,padx=5, pady=5,sticky='e')
        Button(Lebleframe, text='Карта исходных данных\n на военнослужащего', command= lambda: MilitaryPrintView().set(self.service.select_conclusion_m(self.id))).grid(row=0,column=5,padx=5, pady=5,sticky='e')
        Button(Lebleframe, text='Карта текущей медицинской информации', command= lambda: MedicalPrintView().set(self.service.select_information(self.id))).grid(row=1,column=5,sticky='e')
        Button(Lebleframe, text='Карта медицинских данных при убытии', command= lambda: DeparturePrintView().set(self.service.select_medical_departure(self.id))).grid(row=2,column=5,sticky='e')
        Button(Lebleframe, text='Форма справки о военнослужащем,\n проходившем лечение в медо СпН', command= lambda:SpravkaMView().set(self.service.conclusion_m(self.id))).grid(row=1,column=6,pady=3,padx=2,sticky='e')
        Button(Lebleframe, text='Форма справки о гражданском лице,\n проходившем лечение в медо СпН', command= lambda:SpravkaSView().set(self.service.conclusion_s(self.id))).grid(row=2,column=6,pady=3,sticky='e')
