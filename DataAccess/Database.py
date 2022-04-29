import sqlite3
from tkinter import END
from View.Contents.RegistrationContent import RegistrationContent
from View.Contents.UtilitiesContent import UtilitiesContent
from View.Contents.SocialContent import SocialContent
from View.Contents.MedicineContent import MedicineContent
from View.Contents.DischargeContent import DischargeContent
from View.Contents.HealthContent import HealthContent
 

class Database():

    def __init__(self):
        self.db = sqlite3.connect('dbMoss.db')
        self.cursor = self.db.cursor()
        self.db.commit()

    def insert_regist(self, register: RegistrationContent, social: SocialContent, utilities: UtilitiesContent, 
                        medicine: MedicineContent, health: HealthContent, discharge: DischargeContent):
        with self.db:
            self.cursor.execute("BEGIN TRANSACTION")

            self.cursor.execute('''INSERT INTO Social_data( Marital_status,
                Category,Place_of_residence,Position,Specialty) VALUES (?,?,?,?,?)''',(social.Marital_status.get(),social.Category.get(),
            social.Place_of_residence.get(),social.Position.get(),social.Specialty.get(),))

            social_id = self.cursor.lastrowid

            social.Marital_status.delete(0,END),social.Category.set(" "),social.Place_of_residence.delete(0,END),
            social.Position.delete(0,END),social.Specialty.delete(0,END)

            self.cursor.execute('''INSERT INTO Service_data(departmental_affiliation, Composition, 
                military_rank, personal_number, position, vus, military_unit) VALUES (?,?,?,?,?,?,?)''',(utilities.departmental_affiliation.get(),
                utilities.composition.get(),utilities.military_rank.get(),utilities.personal_number.get(),
                utilities.position.get(),utilities.vus.get(),utilities.military_unit.get(),))

            utilities_id = self.cursor.lastrowid

            utilities.departmental_affiliation.set(" "),utilities.composition.set(" "),utilities.military_rank.set(" "),
            utilities.personal_number.delete(0,END),utilities.position.delete(0,END),utilities.vus.delete(0,END),utilities.military_unit.delete(0,END)

            self.cursor.execute('''INSERT INTO Medical_data(
                date_of_injury,time_of_injury,date_of_receipt,time_of_arrival,circumstances,type_of_injury,
                classification_code,preliminary_diagnosis,diagnosis,severity_lesion,medical,wher
                    ) VALUES (?,?,?,?,?,?,?,?,?,?,?,?)''',('','','','','','','','','','','',''))
            medicine_id = self.cursor.lastrowid

            self.cursor.execute('''INSERT INTO health_information(
                Current_status,Transfer_date,Translation_time,Where_transferred
                     ) VALUES (?,?,?,?)''',('','','',''))

            health_id = self.cursor.lastrowid

            self.cursor.execute('''INSERT INTO Discharge_data(
                exodus,date_of_departure,time_of_departure,diagnosis_on_departure,
                classification_code,medical_care,transport) VALUES (?,?,?,?,?,?,?)''',('','','','','','',''))

            discharge_id = self.cursor.lastrowid

            self.cursor.execute( '''INSERT INTO information(lastname,name,patronymic,date_of_birth,
                gender,category,blood_type,rh_factor,information,exposure_dose,Chronic_diseases,Identity_document,
                series,number,Social_data,Service_data,Medical_data,health_information,Discharge_data,forma) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''',(register.lastname.get(),
                register.name.get(),register.patronymic.get(),register.date_of_birth.get(),register.gender.get(),register.category.get(),
                register.blood_type.get(),register.rh_factor.get(),register.information.get(),register.exposure_dose.get(),
                register.Chronic_diseases.get(),register.Identity_document.get(),register.series.get(),register.number.get(),
                social_id,utilities_id,medicine_id,health_id,discharge_id,register.var.get(),))

            register.lastname.delete(0,END),register.name.delete(0,END),register.patronymic.delete(0,END),
            register.date_of_birth.delete(0,END),register.gender.set(''),register.category.set(''),
            register.blood_type.set(''),register.rh_factor.set(''),register.information.delete(0,END),
            register.exposure_dose.delete(0,END),register.Chronic_diseases.delete(0,END),register.Identity_document.delete(0,END),
            register.series.delete(0,END),register.number.delete(0,END)

            self.cursor.execute("COMMIT TRANSACTION")

    def select_m(self, lastname: str = None):
        with self.db: 
            lsname = ''' SELECT  information.id, lastname ||' ' ||name||' '||patronymic,
                        Medical_data.preliminary_diagnosis,Service_data.Military_rank, Service_data.military_unit,
                        Medical_data.date_of_receipt,Discharge_data.Date_of_departure,Discharge_data.exodus FROM information
                                LEFT JOIN Service_data ON Service_data.id = information.Service_data
                                LEFT JOIN Medical_data ON Medical_data.id = information.Medical_data
                                LEFT JOIN Discharge_data ON Discharge_data.id = information.Discharge_data '''
            q = ()
            Q1 = '''WHERE lastname LIKE (?)'''

            if lastname is not None:
                lsname += Q1 
                q = (lastname,)
            return self.cursor.execute(lsname,q)

    def select_s(self): 
        with self.db: 
            return self.cursor.execute( ''' SELECT information.id, lastname ||' ' ||name||' '|| patronymic,
                        Medical_data.preliminary_diagnosis,Medical_data.date_of_receipt,Discharge_data.Date_of_departure,
                        Discharge_data.exodus FROM information 
                                LEFT JOIN Service_data ON Service_data.id = information.Service_data
                                LEFT JOIN Medical_data ON Medical_data.id = information.Medical_data
                                LEFT JOIN Discharge_data ON Discharge_data.id = information.Discharge_data ''' )

    def select_map_m(self,id: int):
        with self.db:
            idTab = self.cursor.execute(""" SELECT information.lastname, information.name, information.patronymic,
                    information.date_of_birth,information.gender,information.category,information.blood_type,
                    information.rh_factor,information.information,information.exposure_dose,information.Chronic_diseases,
                    information.Identity_document,information.series,information.number,
                    Service_data.Departmental_affiliation,Service_data.Composition,Service_data.Military_rank,
                    Service_data.Personal_number, Service_data.Position,Service_data.vus,Service_data.military_unit,
                    Medical_data.date_of_injury, Medical_data.time_of_injury,Medical_data.date_of_receipt,
                    Medical_data.time_of_arrival,Medical_data.circumstances,Medical_data.type_of_injury,
                    Medical_data.classification_code,Medical_data.diagnosis,Medical_data.severity_lesion,
                    Medical_data.medical,Medical_data.wher
                    FROM information
                    LEFT JOIN Service_data ON Service_data.id = information.Service_data
                    LEFT JOIN Medical_data ON Medical_data.id = information.Medical_data 
                    WHERE information.id = ? """,(id,))
            return idTab.fetchone()

    def select_map_s(self, id: int):
        with self.db:
            idTab = self.cursor.execute(""" SELECT information.lastname, information.name, information.patronymic,
                    information.date_of_birth,information.gender,information.category,information.blood_type,
                    information.rh_factor,information.information,information.exposure_dose,
                    information.Chronic_diseases,information.Identity_document,information.series,information.number,
                    Social_data.Marital_status,Social_data.Place_of_residence,Social_data.Position,Social_data.Specialty,
                    Medical_data.date_of_injury, Medical_data.time_of_injury,Medical_data.date_of_receipt,
                    Medical_data.time_of_arrival,Medical_data.circumstances,Medical_data.type_of_injury,
                    Medical_data.classification_code,Medical_data.diagnosis,Medical_data.severity_lesion,
                    Medical_data.medical,Medical_data.wher
                    FROM information
                    LEFT JOIN Social_data ON Social_data.id = information.Social_data
                    LEFT JOIN Medical_data ON Medical_data.id = information.Medical_data 
                    WHERE information.id = ? """,(id,))
                        
            return idTab.fetchone()

    def map_information(self,id: int):
        with self.db:
            idTab = """ SELECT health_information FROM information WHERE id = ? """
            idKey = self.cursor.execute(idTab,(id,))
            idForenKey = idKey.fetchone()
            health = self.cursor.execute(""" SELECT * FROM health_information WHERE id = ? """,(idForenKey[0],))

            return health.fetchone()
            
    def medical_departure(self, id: int):
        with self.db:
            idTab = """ SELECT Discharge_data FROM information WHERE id = ? """
            idKey = self.cursor.execute(idTab,(id,))
            idForenKey = idKey.fetchone()
            dischargeId = self.cursor.execute(""" SELECT * FROM Discharge_data WHERE id = ? """,(idForenKey[0],))
            return dischargeId.fetchone()

    def conclusion_m(self, id: int):
        with self.db:
            idTab = self.cursor.execute(""" SELECT information.id, information.lastname, information.name, information.patronymic, 
                                        Medical_data.diagnosis,Service_data.Military_rank,
                                        Service_data.military_unit,Medical_data.date_of_receipt,
                                        Discharge_data.date_of_departure,Discharge_data.exodus
                                        FROM information
                                        LEFT JOIN Medical_data ON Medical_data.id = information.Medical_data
                                        LEFT JOIN Service_data ON Service_data.id = information.Service_data
                                        LEFT JOIN Discharge_data ON Discharge_data.id = information.Discharge_data 
                                        WHERE information.id = ? """,(id,))
            return idTab.fetchone()

    def conclusion_s(self, id :int):
        with self.db:
            idTab = self.cursor.execute(""" SELECT information.id,information.lastname, information.name, information.patronymic, 
                                        Medical_data.diagnosis,Social_data.Category,Medical_data.date_of_receipt,
                                        Discharge_data.date_of_departure,Discharge_data.exodus
                                        FROM information
                                        LEFT JOIN Medical_data ON Medical_data.id = information.Medical_data
                                        LEFT JOIN Social_data ON Social_data.id = information.Social_data
                                        LEFT JOIN Discharge_data ON Discharge_data.id = information.Discharge_data 
                                        WHERE information.id = ? """,(id,))
            return idTab.fetchone()
            
    def select_MKB(self):
        lst = []
        with self.db:
            self.cursor.execute(""" SELECT Code,name FROM mkb """)
            for row in self.cursor.fetchall():
                lst.extend(row)
        return lst

    def update_health(self, id: int, health: HealthContent):
        with self.db:
            idTab = """ SELECT health_information FROM information WHERE id = ? """
            idKey = self.cursor.execute(idTab,(id,))
            idForenKey = idKey.fetchone()
            self.cursor.execute( """ UPDATE health_information SET Current_status = ?, Transfer_date = ?, Translation_time = ?,
            Where_transferred = ? WHERE id = ? """,(health.current_status.get(),health.transfer_date.get(),
            health.translation_time.get(),health.where_transferred.get(),idForenKey[0],))

    def update_medicine(self,id: int, medicine: MedicineContent):
        with self.db:
            idTab = """ SELECT Medical_data FROM information WHERE id = ? """
            idKey = self.cursor.execute(idTab,(id,))
            idForenKey = idKey.fetchone()
            self.cursor.execute( """ UPDATE Medical_data SET date_of_injury = ?,time_of_injury = ?,date_of_receipt = ?,time_of_arrival = ?,
                                circumstances = ?,type_of_injury = ?,classification_code = ?,preliminary_diagnosis = ?,diagnosis = ?,
                                severity_lesion = ?,medical = ?,wher = ? WHERE id = ? """,(medicine.date_of_injury.get(),medicine.time_of_injury.get(),
                                medicine.date_of_receipt.get(),medicine.time_of_arrival.get(),medicine.circumstances.get(),medicine.type_of_injury.get(),
                                medicine.classification_code.get(),medicine.preliminary_diagnosis.get(),medicine.diagnosis.get(),medicine.severity_lesion.get(),
                                medicine.medical.get(),medicine.wher.get(),idForenKey[0],))
    
    def update_discharge(self,id: int, discharge: DischargeContent):
        with self.db:
            idTab = """ SELECT Discharge_data FROM information WHERE id = ?"""
            idKey = self.cursor.execute(idTab,(id,))
            idForenKey = idKey.fetchone()
            self.cursor.execute( """ UPDATE Discharge_data SET exodus = ?,date_of_departure = ?,time_of_departure = ?,diagnosis_on_departure = ?,
                classification_code = ?,medical_care = ?,transport = ? WHERE id = ? """,(discharge.exodus.get(),discharge.date_of_departure.get(),
                discharge.time_of_departure.get(),discharge.diagnosis_on_departure.get(),discharge.classification_code.get(),
                discharge.medical_care.get(),discharge.transport.get(),idForenKey[0],))

    def delete(self, id: int):
        with self.db:
            idTab = """ SELECT Discharge_data,health_information,Medical_data,
            Social_data,Service_data,information.id FROM information WHERE id = ? """

            idKeys = self.cursor.execute(idTab,(id,)).fetchone()

            self.cursor.execute(""" DELETE FROM Discharge_data WHERE id = ? """,(idKeys[0],))
            self.cursor.execute(""" DELETE FROM health_information WHERE id = ? """,(idKeys[1],))
            self.cursor.execute(""" DELETE FROM Medical_data WHERE id = ? """,(idKeys[2],))
            self.cursor.execute(""" DELETE FROM Social_data WHERE id = ? """,(idKeys[3],))
            self.cursor.execute(""" DELETE FROM Service_data WHERE id = ? """,(idKeys[4],))
            self.cursor.execute(""" DELETE FROM information WHERE id = ? """,(idKeys[5],))
    
    def select_Medical_data(self, id: int):
        with self.db:
            idTab = """ SELECT Medical_data FROM information WHERE id = ? """
            idKey = self.cursor.execute(idTab,(id,)).fetchone()
            health = self.cursor.execute(""" SELECT * FROM Medical_data WHERE id = ? """,(idKey[0],))
            return health.fetchone()
            
# SELECT COUNT(*) AS count FROM information - Поступило всего за сутки 20:
# -Военнослужащих МО
# раненых огнестрельным оружием
# раненых другими видами оружия
# обожженных
# обмороженных
# Всего больных
# В том числе инфекционных
