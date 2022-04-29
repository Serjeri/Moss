from tkinter import *
from .Components.TabsComponent import TabsComponent
from .Components.ScrollableTreeViewComponent import ScrollableTreeViewComponent
from Service.Service import Service
from View.Components.TabPackBase import TabPackBase
from View.Components.DialogBase import DialogBase
from View.ButtunPrintView import ButtunPrintView



class UserView():
    
    def __init__(self, tab_one, service: Service, medicineInfo, healthInfo, dischargeInfo) :

        self.medicineInfo = medicineInfo
        self.healthInfo = healthInfo
        self.dischargeInfo = dischargeInfo

        self.service = service

        headers_m = ['№ п/п','ФИО','Предварительный Диагноз','Воинское звание','Воинская часть','Дата поступления','Дата убытия','Исход (состояние)']
        headers_s = ['№ п/п','ФИО','Предварительный Диагноз','Дата поступления','Дата убытия','Исход (состояние)']
                
        header =['Данные о военных','Данные о гражданских']
        tabsComponent = TabsComponent(tab_one,'Данные о больных',header)
        
        self.treeView_m = ScrollableTreeViewComponent(tabsComponent.frameContent[0], headers_m, service.select_m)

        self.treeView_m.grid.bind('<Double-1>', self.OnDoubleClick)
        self.treeView_m.grid.column(headers_m[0], anchor = 'center', minwidth=50, width=50, stretch=NO)
        self.treeView_m.grid.column(headers_m[5], anchor = 'center', minwidth=100, width=107, stretch=NO)
        self.treeView_m.grid.column(headers_m[6], anchor = 'center', minwidth=75, width=75, stretch=NO)

        self.treeView_s = ScrollableTreeViewComponent(tabsComponent.frameContent[1], headers_s, service.select_s)
        self.treeView_s.grid.bind('<Double-1>', self.OnDoubleClick)
        self.treeView_s.grid.column(headers_s[0], anchor = 'center', minwidth=50, width=50, stretch=NO)
        self.treeView_s.grid.column(headers_s[3], anchor = 'center', minwidth=100, width=107, stretch=NO)
        self.treeView_s.grid.column(headers_s[4], anchor = 'center', minwidth=75, width=75, stretch=NO)

    def OnDoubleClick(self, event):

        self.treeView_m.grid.identify_row(event.y)
        values = self.treeView_m.grid.item(self.treeView_m.grid.focus(), option="values")

        dialogBase = DialogBase('Заполнение карты больного',"1025x700")

        self.buttunPrint = ButtunPrintView(values[0], self.service)

        social = TabPackBase(dialogBase.win, self.medicineInfo, title='IV. Медицинские данные', fill=BOTH,side=None, expand = True, padx=20, pady=10)
        social.render(social.LabelFrame)

        social = TabPackBase(dialogBase.win, self.healthInfo, title='V. Текущая медицинская информация', fill=BOTH, side=LEFT, expand = True, padx=20, pady=10)
        social.render(social.LabelFrame)

        social = TabPackBase(dialogBase.win, self.dischargeInfo, title='VI. Данные при выписке', fill=BOTH, side=TOP, expand = True, padx=20, pady=10)
        social.render(social.LabelFrame)

        buttonPrint = TabPackBase(dialogBase.win, self.buttunPrint, title='Отчетные формы на печать', fill=BOTH, side=LEFT, expand = True, padx=20, pady=10)
        buttonPrint.render(buttonPrint.LabelFrame)

        Button(dialogBase.win, text='отправить', height=2, width = 10, font=('calibri', 12, 'normal'),
        command= lambda: self.service.update(values[0],self.healthInfo,self.medicineInfo,self.dischargeInfo)).pack(side=BOTTOM, padx=20, pady=10)
