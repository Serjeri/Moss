from tkinter import LabelFrame


class TabPackBase():

    def __init__ (self, frame , content, **kwargs):
        
        self.LabelFrame = LabelFrame(frame, text=kwargs['title'])
        self.LabelFrame.pack(fill=kwargs['fill'],side=kwargs['side'] ,expand=kwargs['expand'],
        padx=kwargs['padx'], pady=kwargs['pady'])

        self.content = content

    def render(self,Lebleframe):
        self.content.render(Lebleframe)
        