from tkinter import *
from tkinter.ttk import Notebook
from .Components.TabGridBase import TabGridBase
from .Contents.RegistrationContent import RegistrationContent
from .Contents.UtilitiesContent import UtilitiesContent
from .Contents.SocialContent import SocialContent
from .Contents.MedicineContent import MedicineContent
from .Contents.DischargeContent import DischargeContent
from .Contents.HealthContent import HealthContent
from .UserView import UserView
from DataAccess.Database import Database
from Service.Service import Service
from .ReportView import ReportView


class MainFrame(Frame):

    def __init__(self, win):

        registrInfo = RegistrationContent()
        socialInfo = SocialContent()
        utilitiesIfon = UtilitiesContent()

        tabs_control = Notebook(win)
        
        tab_one = Frame(tabs_control)
        frameCenter = Frame(tab_one)
        
        opts = { 'ipadx': 10, 'ipady': 10, 'fill': BOTH }
        frameCenter.pack(side=TOP, **opts)
        tab_one.pack(side=LEFT,**opts)

        self.tab_two = Frame(tabs_control)
        self.tab_four = Frame(tabs_control)
        self.tab_five = Frame(tabs_control)
        self.tab_sex = Frame(tabs_control)

        tabs_control.add(tab_one, text='Структура исходной информации')
        tabs_control.pack(fill=BOTH)
        
        registr = TabGridBase(frameCenter, registrInfo, title='Регистрация', row=0, column=0, padx=5, pady=10, sticky="w")
        registr.render(registr.LabelFrame)

        utilities = TabGridBase(frameCenter,utilitiesIfon,title='II Служебные данные (на военнослужащих)',row=0, column=1, padx=5, sticky='n', pady=10)
        utilities.render(utilities.LabelFrame)

        social = TabGridBase(frameCenter, socialInfo, title='III Социальные данные (на гражданских лиц)',row=0, column=2, padx=5, pady=10, sticky='n')
        social.render(social.LabelFrame)
        
        dbInfo = Database()
        service1 = Service(dbInfo)
 
        medicineInfo = MedicineContent(service1.select_MKB())
        healthInfo = HealthContent()
        dischargeInfo = DischargeContent()

        UserView(win,service1,medicineInfo,healthInfo,dischargeInfo)

        Button(frameCenter, text='Отправить' ,command=lambda:service1.insert(registrInfo,socialInfo,utilitiesIfon,
        medicineInfo,healthInfo,dischargeInfo)).grid(row=0,column=2,padx=5, sticky='es',pady=10)
        Button(frameCenter, text='Ежесуточное срочное донесение',command=lambda: ReportView(service1.donation())).grid(row=0,column=3,padx=5, sticky='ew',pady=10)
