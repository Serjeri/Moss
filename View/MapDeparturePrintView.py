from tkinter import END, Tk, Entry, Button
 
 
class MapDeparturePrintView:
     
    def table_medical_departure(self):
    
        win = Tk()
        win.title("Карта медицинских данных при убытии")
        win.resizable(False, False)

        for i in range(total_rows):
            for j in range(total_columns):
                 
                self.e = Entry(win, width=50, fg='blue',
                               font=('Arial',13,'bold'))
                 
                self.e.grid(row=i, column=j)
                self.e.insert(END, lst[i][j])
        Button(win, text='Распичатать').grid(row=31, column=0, padx=10, sticky='se', pady=10)

lst = [('Исход',' '),
    ('Дата убытия',' '),
    ('Время убытия',' '),
    ('Диагноз при убытии',' '),
    ('Код по классификатору при убытии', ' '),
    ('Оказанная медицинская помощь', ' '),
    ('Каким транспортом убыл', ' ')]

# найти общее количество строк и
# столбцов в списке
total_rows = len(lst)
total_columns = len(lst[0])
