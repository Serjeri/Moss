from dataclasses import dataclass


@dataclass
class MedicineInfoModel:

    date_of_injury : str =" "
    time_of_injury: str =" "
    date_of_receipt: str =" "
    time_of_arrival: str =" "
    circumstances: str =" "
    type_of_injury: str =" "
    classification_code: str =" "
    preliminary_diagnosis: str = " "
    diagnosis: str =" "
    severity_lesion: str =" "
    medical: str =" "
    wher: str =" "






