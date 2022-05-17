from tkinter import *
from datetime import datetime,timedelta
from turtle import update
from xmlrpc.client import boolean
from DataAccess.Database import Database
from View.Contents.RegistrationContent import RegistrationContent
from View.Contents.UtilitiesContent import UtilitiesContent
from View.Contents.SocialContent import SocialContent
from View.Contents.MedicineContent import MedicineContent
from View.Contents.DischargeContent import DischargeContent
from View.Contents.HealthContent import HealthContent
from Helper.errors import Errors
from View.Models.MedicalPrintModel import MedicalPrintModel
from View.Models.CivilPrintModel import CivilPrintModel
from View.Models.MilitaryPrintModel import MilitaryPrintModel
from View.Models.DeparturePrintModel import DeparturePrintModel
from View.Models.SpravkaMModel import SpravkaMModel
from View.Models.SpravkaSModel import SpravkaSModel
from View.Models.MedicineInfoModel import MedicineInfoModel



class Service():

    db = None

    def __init__ (self, db: Database):
        self.db = db
        
    def select_MKB(self):
        return self.db.select_MKB()

    def insert (self,registration: RegistrationContent,social:SocialContent,utilities:UtilitiesContent,
    medicine:MedicineContent,health: HealthContent, discharge: DischargeContent):
        try:
            self.db.insert_regist(registration,social,utilities,medicine,health,discharge)

            Errors.message()
        except Exception as e:
            Errors.message_errors()

    def select_s(self):
       return self.db.select_s()

    def select_m(self,lastname = None):
        try:
            if lastname is None:
                return self.db.select_m()
            else:
                return self.db.select_m(lastname)

        except Exception as e:
            Errors.message_errors()

    def update(self, id:int, health: HealthContent, medicine: MedicineContent, discharge: DischargeContent):
        try:
            self.db.update_health(id, health)
            self.db.update_medicine(id, medicine)
            self.db.update_discharge(id,discharge)
            Errors.message()
        except Exception as e:
            Errors.message_errors()

    def select_information(self, id: int) -> MedicalPrintModel:
        data = self.db.map_information(id)

        if data is None:
            return MedicalPrintModel()

        return MedicalPrintModel(data[1], data[2], data[3], data[4])

    def select_medical_departure(self, id:int)->DeparturePrintModel:
        data = self.db.medical_departure(id)

        if data is None:
            return DeparturePrintModel()

        return DeparturePrintModel(data[7],data[1], data[2], data[3], data[4],data[5], data[6])

    def select_conclusion_m(self, id: int) -> MilitaryPrintModel:
        data = self.db.select_map_m(id)
        if data is None:
            return MilitaryPrintModel()
        
        return MilitaryPrintModel(data[0], data[1], data[2], data[3],data[4], data[5], data[6], data[7],data[8], data[9], data[10], data[11],
        data[12], data[13], data[14], data[15],data[16], data[17], data[18], data[19],data[20], data[21], data[22], data[23],data[24], 
        data[25], data[26], data[27],data[28],data[29],data[30],data[31])

    def select_conclusion_s(self, id:int) -> CivilPrintModel:
        data = self.db.select_map_s(id)
        if data is None:
            return CivilPrintModel()
        
        return CivilPrintModel(data[0], data[1], data[2], data[3],data[4], data[5], data[6], data[7],data[8], data[9], data[10], data[11],
        data[12], data[13], data[14], data[15],data[16], data[17], data[18], data[19],data[20], data[21], data[22],data[23],data[24], 
        data[25], data[26], data[27],data[28])

    def conclusion_m(self,id:int) -> SpravkaMModel:
        data = self.db.conclusion_m(id)
        if data is None:
            return SpravkaMModel()
        return SpravkaMModel(data[0], data[1], data[2], data[3],data[4], data[5], data[6], data[7],data[8], data[9])

    def conclusion_s(self,id:int) -> SpravkaSModel:
        data = self.db.conclusion_s(id)
        if data is None:
            return SpravkaSModel()
        return SpravkaSModel(data[0], data[1], data[2], data[3],data[4], data[5], data[6], data[7],data[8])

    def delete(self, id : int):
        try:
            if Errors.confirmation_of_removal() == 'yes':
                self.db.delete(id)
        except Exception as e:
            Errors.message_errors()


    def select_Medical_data(self, id : int) -> MedicineInfoModel :
        data = self.db.select_Medical_data(id)

        if data is None:
            return MedicineInfoModel
        return MedicineInfoModel(data[1], data[2], data[3], data[4],data[5], data[6], 
        data[7], data[8],data[9],data[10], data[11], data[12])

    def donation(self):
        dateTimeOne = datetime.now() - timedelta(days=1)
        datenow = datetime.now()
        dateOne = self._privet_donation(dateTimeOne)
        dateTime = self._privet_donation(datenow)# возврошяет 2 значеия
        donaDateTime = self.db.donation_datatame(dateTime[0],dateTime[1])
        mo = self.db.donation_mo(dateTime[0],dateTime[1])
        vng = self.db.donation_vng(dateTime[0],dateTime[1])
        others = self.db.donation_others(dateTime[0],dateTime[1])
        сivilians = self.db.donation_сivilians(dateTime[0],dateTime[1])
        status = self.db.don_status(dateOne[0],dateOne[1])
        transport = self.db.transport(dateOne[0],dateOne[1])
        statusDed = self.db.status_ded(dateOne[0],dateOne[1])

        sampleDictDon = {
            'count': donaDateTime[0],
            'mo': self._converter_list_to_dict(mo), 
            'vng': self._converter_list_to_dict(vng),
            'others':self._converter_list_to_dict(others),
            'day': self.db.donation_datatame(dateOne[0],dateOne[1]),
            'status': self._converter_list_to_dict(status),
            'transport':self._converter_list_to_dict(transport),
            'statusDed':self._converter_list_to_dict(statusDed)
            }
        return sampleDictDon

    def _converter_list_to_dict(self, list)-> dict:
        dict_sample = {'ранение': '-', 'заболевание': '-', 'травма':'-', 'термическое': '-', 
        'поражение химическое': '-', 'поражение радиационное': '-', 'комбинированное поражение': '-','летальный исход':'-',
        'самостоятельно':'-'}

        if len(list) == 0:
            return dict_sample

        for val in list:
            dict_sample[val[0]] = val[1]

        return dict_sample

    def _privet_donation(self, time):
        timeNow = (time.hour * 60) + time.minute
        if timeNow > 1200 and timeNow < 1440:
            start = datetime(time.year,time.month,time.day,20,00)
            end = start + timedelta(days=1)

        if timeNow > 1440 and timeNow < 1499 or timeNow > 60 and timeNow < 1200 :
            end = datetime(time.year,time.month,time.day,20,00)
            start = end - timedelta(days=1)
        
        timeEnd = end.strftime('%d.%m.%Y %H:%M')
        timeStart = start.strftime('%d.%m.%Y %H:%M')
        return (timeStart, timeEnd)