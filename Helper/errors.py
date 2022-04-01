from tkinter.messagebox import *

class Errors():

    @staticmethod
    def message():
        showinfo("Информация", 'Данные успешно отправлены')

    @staticmethod
    def message_errors():
        showerror("Ошибка", "Приложение обнаружило неизвестную ошибку")
