from tkinter import *

class ArchiveCardsForm:
    def __init__(self, box):
        self.box = box
        self.window = Tk()

        self.window.geometry("400x700")
        self.window.title("Archive Cards")
        self.window.resizable(False, False)

        archiveCards = self.box.get_archive_cards_information()

        lblarchiveCards = Label(self.window, text= archiveCards)
        lblarchiveCards.grid(row= 0, column= 0)

        self.window.mainloop()