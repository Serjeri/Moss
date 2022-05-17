from tkinter import *
from .Components.TabsComponent import TabsComponent
from .Components.ScrollableTreeViewComponent import ScrollableTreeViewComponent
from Service.Service import Service
from View.Components.TabPackBase import TabPackBase
from View.Components.DialogBase import DialogBase
from View.ButtunPrintView import ButtonPrintView
from .Contents.HealthContent import HealthContent
from .Models.MedicalPrintModel import MedicalPrintModel
from .Models.MedicineInfoModel import MedicineInfoModel
from .Contents.MedicineContent import MedicineContent
from .Contents.DischargeContent import DischargeContent
from .Models.DeparturePrintModel import DeparturePrintModel


class UserView():
    
    def __init__(self, tab_one, service: Service, medicineInfo :MedicineContent, 
                    healthInfo : HealthContent, dischargeInfo: DischargeContent) :

        self.medicineInfo = medicineInfo
        self.healthInfo = healthInfo
        self.dischargeInfo = dischargeInfo

        self.service = service

        headers_m = ['№ п/п','ФИО','Предварительный Диагноз','Воинское звание','Воинская часть','Дата поступления','Дата убытия','Исход (состояние)']
                
        header =['Данные о пациентах','Тест']
        tabsComponent = TabsComponent(tab_one,'Данные о больных',header)
        
        self.treeView_m = ScrollableTreeViewComponent(tabsComponent.frameContent[0], headers_m, service.select_m, service.delete)

        self.treeView_m.grid.bind('<Double-1>', self.OnDoubleClick)
        self.treeView_m.grid.column(headers_m[0], anchor = 'center', minwidth=50, width=50, stretch=NO)
        self.treeView_m.grid.column(headers_m[5], anchor = 'center', minwidth=100, width=107, stretch=NO)
        self.treeView_m.grid.column(headers_m[6], anchor = 'center', minwidth=75, width=75, stretch=NO)

    def OnDoubleClick(self, event):

        self.treeView_m.grid.identify_row(event.y)
        values = self.treeView_m.grid.item(self.treeView_m.grid.focus(), option="values")

        dialogBase = DialogBase('Заполнение карты больного', "1025x700")

        self.buttonPrint = ButtonPrintView(values[0], self.service)

        social = TabPackBase(dialogBase.win, self.medicineInfo, title='IV. Медицинские данные', fill=BOTH,side=None, expand = True, padx=20, pady=10)
        social.render(social.LabelFrame)

        social = TabPackBase(dialogBase.win, self.healthInfo, title='V. Текущая медицинская информация', fill=BOTH, side=LEFT, expand = True, padx=20, pady=10)
        social.render(social.LabelFrame)

        social = TabPackBase(dialogBase.win, self.dischargeInfo, title='VI. Данные при выписке', fill=BOTH, side=TOP, expand = True, padx=20, pady=10)
        social.render(social.LabelFrame)

        buttonPrint = TabPackBase(dialogBase.win, self.buttonPrint, title='Отчетные формы на печать', fill=BOTH, side=LEFT, expand = True, padx=20, pady=10)
        buttonPrint.render(buttonPrint.LabelFrame)

        Button(dialogBase.win, text='отправить', height=2, width = 10, font=('calibri', 12, 'normal'),
        command= lambda: self.service.update(values[0],self.healthInfo,self.medicineInfo,self.dischargeInfo)).pack(side=BOTTOM, padx=20, pady=10)


        idTab = values[0]
        test = self.service.select_information(idTab)
        self.healthInfo.set(MedicalPrintModel(test.condition,test.date,test.time,test.where))

        medInfo = self.service.select_Medical_data(idTab)
        self.medicineInfo.set(MedicineInfoModel(medInfo.date_of_injury,medInfo.time_of_injury,medInfo.date_of_receipt,
            medInfo.time_of_arrival,medInfo.circumstances,medInfo.type_of_injury,medInfo.classification_code,medInfo.preliminary_diagnosis,
            medInfo.diagnosis,medInfo.severity_lesion,medInfo.medical,medInfo.wher))

        medicalDeparture = self.service.select_medical_departure(idTab)
        self.dischargeInfo.set(DeparturePrintModel(medicalDeparture.exodus,medicalDeparture.date_of_departure,
        medicalDeparture.time_of_departure,medicalDeparture.diagnosis_on_departure,medicalDeparture.classification_code,
        medicalDeparture.medical_care,medicalDeparture.transport))
