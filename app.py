from tkinter import *
from View.MainFrame import MainFrame

class AppSettings():
    
    def __init__(self):

        self.win = Tk()
        MainFrame(self.win)
        self.win.geometry("950x650")
        self.win.title('Медицинский учет раненых больных и пораженных поступающих в медо СпН')

        photo = PhotoImage(file='Content/photo/med.png')
        self.win.iconphoto(False, photo)

    def start(self):
        self.win.mainloop()


if __name__ == '__main__':
    app = AppSettings()
    app.start()
