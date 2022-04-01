from tkinter import Tk


class DialogBase():

    def __init__(self, title: str, geometry: str, shouldResize: bool = False, useGeometry: bool = True):
    
        self.win = Tk()

        if useGeometry:
           self.win.geometry(geometry)

        self.win.title(title)
        self.win.resizable(shouldResize, shouldResize)