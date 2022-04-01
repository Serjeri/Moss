from tkinter import END, Tk, Entry, Button

 
class MapMedicalPrintView:
    
    def table_health_information(self, id: int, fun):
        print(id)
        win = Tk()
        win.title("Карта текущей медицинской информации")
        win.resizable(False, False)

        lst = [('Текущее состояние',fun(id)),
                ('Дата перевода',fun(id)),
                ('Время перевода',fun(id)),
                ('Куда переведен(а)',fun(id))]

        # найти общее количество строк и
        # столбцов в списке
        total_rows = len(lst)
        total_columns = len(lst[0])

        for i in range(total_rows):
            for j in range(total_columns):
                 
                self.e = Entry(win, width=50, fg='blue',
                               font=('Arial',13,'bold'))
                 
                self.e.grid(row=i, column=j)
                self.e.insert(END, lst[i][j])
        Button(win, text='Распичатать').grid(row=31, column=0, padx=10, sticky='se', pady=10)
