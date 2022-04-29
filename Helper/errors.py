from tkinter.messagebox import *
import tkinter.messagebox as mb


class Errors():

    @staticmethod
    def message():
        showinfo("Информация", 'Данные успешно отправлены')

    @staticmethod
    def message_errors():
        showerror("Ошибка", "Приложение обнаружило неизвестную ошибку обратитесь к администратору")

    @staticmethod
    def confirmation_of_removal():
        dele = mb.askquestion("Потвердите удаление", "Удалить запись ?")
        if dele == 'yes':
            return 'yes'
