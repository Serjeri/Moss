from prettytable import *
from tkinter import *


class ReportView:
    def __init__(self, dateTime):
    
        win=Tk()
        title = "Eжесуточного срочного донесения"
        win.title(title)
        win.resizable(False, False)
        t = Text(win,width=53, height=43)
        t.winfo_geometry()
        table = PrettyTable()
        
        table.add_column("Категория потерь",['Поступило всего:','в том числе:',
        "Военнослужащих МО РФ","раненых огнестрельным оружием:","раненых другими видами оружия:",
        "обожженных:", "обмороженных:","Всего больных:","В том числе инфекционных:","Военнослужащих ВНГ",
        "раненых огнестрельным оружием:","раненых другими видами оружия:","обожженных:","обмороженных:",
        "Всего больных:","В том числе инфекционных:","Военнослужащих других ведомств","раненых огнестрельным оружием:",
        "раненых другими видами оружия:","обожженных:","обмороженных:","Всего больных:","В том числе инфекционных:",
        "Гражданских лиц:"])
        table.add_column("Число (чел.)",[dateTime['count'],'',"",'-',dateTime['mo']['ранение'],dateTime['mo']['термическое'],dateTime['mo']['термическое']
        ,dateTime['mo']['заболевание'],'-',"",'-',dateTime['vng']['ранение'],dateTime['vng']['термическое'],dateTime['vng']['термическое'],dateTime['vng']['заболевание'],'-',"",
        '-',dateTime['others']['ранение'],dateTime['others']['термическое'],dateTime['others']['термическое'],dateTime['others']['заболевание'],'-','-'])
        
        sick = PrettyTable()
        sick.add_column("Показатели",["Состояло на 20.00 предыдущих суток","Поступило всего:","Состоит всего:",
                        "В том числе","раненых","больных","Выбыло всего:","В том числе","возвращено в часть",
                        "эвакуировано","умерло"])

        sick.add_column("Число (чел.)",[dateTime['day'][0],dateTime['day'][0],dateTime['day'][0],' ',dateTime['status']['ранение'],
        dateTime['status']['заболевание'],dateTime['transport']['самостоятельно'],' ',0,0,dateTime['statusDed']['летальный исход']])
        t.insert(INSERT,table)
        t.insert(INSERT,sick)
        t.config(state=DISABLED)
        t.pack()
