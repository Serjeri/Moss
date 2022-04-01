from tkinter import END, Tk, Entry, Button
 
 
class MapPrintSView:
     
    def table_held_in_medo(self):
    
        win = Tk()
        win.title("Экранная форма справки о гражданском лице, проходившем лечение в медо СпН")
        win.resizable(False, False)

        for i in range(total_rows):
            for j in range(total_columns):
                 
                self.e = Entry(win, width=50, fg='blue',
                               font=('Arial',13,'bold'))
                 
                self.e.grid(row=i, column=j)
                self.e.insert(END, lst[i][j])
        Button(win, text='Распичатать').grid(row=31, column=0, padx=10, sticky='se', pady=10)

lst = [('№ п/п',''),
    ('Фамилия',' '),
    ('Имя',' '),
    ('Отчество',' '),
    ('Диагноз',' '),
    ('Категория гражданского лица', ' '),
    ('Дата по-ступле-ния', ' '),
    ('Дата убытия', ' '),
    ('Исход (состоя-ние)', ' ')]

# найти общее количество строк и
# столбцов в списке
total_rows = len(lst)
total_columns = len(lst[0])
