from tkinter import Button
from View.CivilPrintView import CivilPrintView
from View.MilitaryPrintView import MilitaryPrintView
from View.MapMedicalPrintView import MapMedicalPrintView
from View.MapDeparturePrintView import MapDeparturePrintView
from View.MapPrintSView import MapPrintSView
from View.MapSpravkaMView import MapSpravkaMView
from Service.Service import Service


class ButtunPrintView():

    def __init__(self, id: int, service: Service):
        self.id = id
        self.service = service

    def render(self, Lebleframe):

        self.tableCivic = CivilPrintView()
        self.TableMilitary = MilitaryPrintView()

        Button(Lebleframe, text='Карта исходных данных\n на гражданское лицо', command= lambda: self.tableCivic.table_civic()).grid(row=0,column=6,padx=5, pady=5,sticky='e')
        Button(Lebleframe, text='Карта исходных данных\n на военнослужащего', command= lambda: self.TableMilitary.table_military()).grid(row=0,column=5,padx=5, pady=5,sticky='e')
        Button(Lebleframe, text='Карта текущей медицинской информации', command= lambda: MapMedicalPrintView().table_health_information(self.id, self.service.select_information)).grid(row=1,column=5,sticky='e')
        Button(Lebleframe, text='Карта медицинских данных при убытии', command= lambda: MapDeparturePrintView().table_medical_departure()).grid(row=2,column=5,sticky='e')
        Button(Lebleframe, text='Форма справки о военнослужащем,\n проходившем лечение в медо СпН', command= lambda:MapSpravkaMView().table_Military()).grid(row=1,column=6,pady=3,padx=2,sticky='e')
        Button(Lebleframe, text='Форма справки о гражданском лице,\n проходившем лечение в медо СпН', command= lambda:MapPrintSView().table_held_in_medo()).grid(row=2,column=6,pady=3,sticky='e')
