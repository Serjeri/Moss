from dataclasses import dataclass


@dataclass
class MedicalPrintModel:

    condition: str = " "
    date: str = " "
    time: str = " "
    where: str = " "