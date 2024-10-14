from tkinter import *

class BoxCardsForm:
    def __init__(self, box):
        self.box = box
        self.window = Tk()

        self.window.geometry("400x700")
        self.window.title("Box Cards")
        self.window.resizable(False, False)

        boxCards = self.box.get_all_boxcards_information()

        lblboxCards = Label(self.window, text= boxCards)
        lblboxCards.grid(row= 0, column= 0)

        self.window.mainloop()