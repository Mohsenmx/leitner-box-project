from tkinter import *
from add_new_card_form import *
from review_form import *
from box_cards_form import *
from archive_cards_form import *
from statistics_form import *

class MainForm:
    def __init__(self, box):
        self.box = box
        self.window = Tk()

        self.window.geometry("230x300")
        self.window.title("Leitner Box")
        self.window.resizable(False, False)

        self.btnAddNewCard = Button(self.window, text= "Add New Card", command= self.show_add_new_card_form)
        self.btnAddNewCard.grid(row= 0, column= 0, padx= 70, pady= 10)

        self.btnReview = Button(self.window, text= "Review", command= self.show_review)
        self.btnReview.grid(row= 1, column= 0, padx= 70, pady= 10)

        self.btnBoxCards = Button(self.window, text= "Box Cards", command= self.show_box_cards_form)
        self.btnBoxCards.grid(row= 2, column=0, padx= 70, pady= 10)

        self.btnArchiveCards = Button(self.window, text= "Archive Cards", command= self.show_archive_cards_form)
        self.btnArchiveCards.grid(row= 3, column= 0, padx= 70, pady= 10)

        self.btnStatistics = Button(self.window, text= "Statistics", command= self.show_statistics_form)
        self.btnStatistics.grid(row= 4, column= 0, padx= 70, pady= 10)

        self.btnClose = Button(self.window, text= "Exit", command= self.close_form)
        self.btnClose.grid(row= 5, column= 0, padx= 70, pady= 10)

        self.window.mainloop()
    
    def show_add_new_card_form(self):
        AddNewCardForm(self.box)

    def show_review(self):
        ReviewForm(self.box)

    def show_box_cards_form(self):
        BoxCardsForm(self.box)

    def show_statistics_form(self):
        StatisticsForm(self.box)
        
    def show_archive_cards_form(self):
        ArchiveCardsForm(self.box)

    def close_form(self):
        self.window.destroy()