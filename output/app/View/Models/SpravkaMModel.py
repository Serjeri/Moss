from dataclasses import dataclass


@dataclass
class SpravkaMModel:

    id: str 
    lastname : str =" "
    name : str =" "
    patronymic: str =" "
    diagnosis: str =" "
    military_rank: str = " "
    military_unit: str = " "
    date_of_receipt : str = " "
    date_of_departure : str = " "
    exodus : str = " "
