from importlib.util import set_loader
from ssl import ALERT_DESCRIPTION_BAD_CERTIFICATE_HASH_VALUE
from tkinter import *

class StatisticsForm:
    def __init__(self, box):
        self.box = box
        self.window = Tk()

        self.window.geometry("150x100")
        self.window.title("Statistics")
        self.window.resizable(False, False)

        s = self.box.get_statistics()

        lblstatistics = Label(self.window, text= s)
        lblstatistics.grid(row= 0, column= 0, padx= 20, pady= 20)

        self.window.mainloop()