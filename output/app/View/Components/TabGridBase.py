from tkinter import LabelFrame


class TabGridBase():

    def __init__ (self, frame , content, **kwargs):
        
        self.LabelFrame = LabelFrame(frame, text=kwargs['title'])
        self.LabelFrame.grid(row=kwargs['row'],column=kwargs['column'],
        padx=kwargs['padx'], pady=kwargs['pady'], sticky=kwargs['sticky'])

        self.content = content

    def render(self,Lebleframe):
        self.content.render(Lebleframe)