from tkinter import *
from tkinter import messagebox

root = Tk()
root.title('Викторина')
root.geometry('600x600')
root["bg"] = "#6C48D7"

# Кнопка START (que_zero) тут, запускающая que_one
def que_zero():
    btnStart = Button(root, text='Start', command=lambda: que_one(btnStart))
    btnStart.grid(row=0)

def que_one(btnStart):
    btnStart.destroy()

    question = Label(root, text='Тут будет вопрос', font='20', fg='#000000', bg='#FFD673')
    question_2 = Label(root, text='Введи ответ цифрой: ', font='15', fg='#000000')
    answer = Entry(bg='#C0C0C0')

    btn = Button(root, text='Ответить', command=lambda: game1(que_two))
    btn.grid(row = 0)
    btn.place(relx=.5, rely=.8, anchor="c", height=60, width=500, bordermode=OUTSIDE)
    question_3 = Label(root, text='1. Тут будет ответ', font='15', bg='#FF4040', fg='#FFFFFF')
    question_4 = Label(root, text='2. Тут будет ответ', font='15', bg='#FF4040', fg='#FFFFFF')
    question_5 = Label(root, text='3. Тут будет ответ', font='15', bg='#FF4040', fg='#FFFFFF')
    question_6 = Label(root, text='Правильных ответов: 0', font='5', bg='#FFD700')

    question_6.place(relx=.2, rely=.9, anchor="c", height=25, width=200, bordermode=OUTSIDE,)

    question.grid(row = 0)
    question.place(relx=.5, rely=.1, anchor="c", height=50, width=500, bordermode=OUTSIDE)
    question_2.place(relx=.5, rely=.6, anchor="c", height=60, width=500, bordermode=OUTSIDE)

    answer.grid(row = 1)
    answer.place(relx=.5, rely=.7, anchor="c", height=30, width=500, bordermode=OUTSIDE)

    question_3.grid(row = 1)
    question_3.place(relx=.5, rely=.2, anchor="c", height=50, width=500, bordermode=OUTSIDE)

    question_4.grid(row = 1)
    question_4.place(relx=.5, rely=.3, anchor="c", height=50, width=500, bordermode=OUTSIDE)

    question_5.grid(row = 1)
    question_5.place(relx=.5, rely=.4, anchor="c", height=50, width=500, bordermode=OUTSIDE)

    def game1(que_two):
        if answer.get().lower() == '1':
            correctCount = correctCount + 1
            que_two()
        else:
            incorrectCount = incorrectCount +1
            que_two()


if __name__ == '__main__':
    que_zero()
    root.mainloop()