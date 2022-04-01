from tkinter import *
from DataAccess.Database import Database
from View.Contents.RegistrationContent import RegistrationContent
from View.Contents.UtilitiesContent import UtilitiesContent
from View.Contents.SocialContent import SocialContent
from View.Contents.MedicineContent import MedicineContent
from View.Contents.DischargeContent import DischargeContent
from View.Contents.HealthContent import HealthContent
from Helper.errors import Errors


class Service():

    db = None

    def __init__ (self, db: Database):
        self.db = db
        
    def select_MKB(self):
        return self.db.select_MKB()

    def insert (self,registration: RegistrationContent,social:SocialContent,utilities:UtilitiesContent,medicine:MedicineContent,health: HealthContent, discharge: DischargeContent):
        try:
            self.db.insert_regist(registration,social,utilities,medicine,health,discharge)

            Errors.message()
        except Exception as e:
            print(e)
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
            print(e)
            Errors.message_errors()

    def update(self,id:int, health: HealthContent, medicine: MedicineContent, discharge: DischargeContent):# 
        try:
            self.db.update_health(id, health)
            self.db.update_medicine(id, medicine)
            self.db.update_discharge(id,discharge)
            Errors.message()
        except Exception as e:
            print(e)
            Errors.message_errors()

    def select_information(self, id: int):
        return self.db.map_information(id)

    def select_medical_departure(self):
        pass

    def select_conclusion_m(self):
        pass

    def select_conclusion_s(self):
        pass