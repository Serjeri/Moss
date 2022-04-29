from dataclasses import dataclass


@dataclass
class SpravkaSModel:
    
    id : str
    lastname : str =" "
    name : str =" "
    patronymic: str =" "
    diagnosis: str =" "
    category: str = " "
    date_of_receipt : str = " "
    date_of_departure : str = " "
    exodus : str = " "