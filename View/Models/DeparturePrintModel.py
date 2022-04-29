from dataclasses import dataclass


@dataclass
class DeparturePrintModel:

    exodus: str = " "
    date_of_departure: str = " "
    time_of_departure: str = " "
    diagnosis_on_departure: str = " "
    classification_code: str = " "
    medical_care: str = " "
    transport: str = " "
