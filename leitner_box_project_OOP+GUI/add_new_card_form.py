from tkinter import *
from tkinter import messagebox
from card import *

class AddNewCardForm:
    def __init__(self, box):
        self.box = box
        self.window = Tk()

        self.window.geometry("230x150")
        self.window.title("Add New Card Form")
        self.window.resizable(False, False)

        self.lblQuestion = Label(self.window, text = "Question: ")
        self.lblQuestion.grid(row = 0, column = 0, padx = 10, pady = 10)
        self.entQuestion = Entry(self.window)
        self.entQuestion.grid(row = 0, column = 1)

        self.lblAnswer = Label(self.window, text = "Answer: ")
        self.lblAnswer.grid(row = 1, column = 0, padx = 10, pady = 10)
        self.entAnswer = Entry(self.window)
        self.entAnswer.grid(row = 1, column = 1)

        self.btnMakeCard = Button(self.window, text = "Make Card", command = self.save_card)
        self.btnMakeCard.grid(row = 2, column = 0,columnspan = 3, pady = 10)
        
        self.window.mainloop()

    def save_card(self):
        question = self.entQuestion.get()
        answer = self.entAnswer.get()

        c = Card(question, answer)
        self.box.add_new_card(c)
        messagebox.showinfo(title = "Success", message = "Card Added Successfully!")
        self.entQuestion.delete(0, "end")
        self.entAnswer.delete(0, "end")
        
        



        