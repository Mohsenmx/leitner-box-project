from tkinter import *
from tkinter import messagebox

class ReviewForm:
    def __init__(self, box):
        self.box = box

        reviewCards = self.box.review()
        if len(reviewCards) == 0 :
            messagebox.showinfo(title = "No Review" , message = "No Review Today!")
        else:
            self.window = Tk()
            
            self.window.title("Review Cards")
        
            cards = ["card1", "card2", "card3"]

            var = Variable(value=cards)

            listbox = Listbox(
                self.window,
                listvariable=var,
                height= len(cards),
                selectmode=EXTENDED
            )

            listbox.pack(expand=True, fill=BOTH)


            def items_selected(event):
                # get all selected indices
                selected_indices = listbox.curselection()
                # get selected items
                selected_langs = ",".join([listbox.get(i) for i in selected_indices])
                msg = f'{selected_langs}'
                messagebox.showinfo(title="", message=msg)


            listbox.bind('<<ListboxSelect>>', items_selected)

            #self.reviewedCards = []
            #self.responses = []
            #self.q, self.a = selected_cards.get_information()
            #self.lblQuestion = Label(self.window, text = self.q)
            #self.lblQuestion.grid(row = 0, column = 0, padx= 20, pady= 10)

            #self.btnShowAnswer = Button(self.window, text = "Show Answer", command = self.show_answer)
            #self.btnShowAnswer.grid(row = 1, column = 0, padx= 20, pady=10)

            #self.reviewedCards.append(card)
            #self.box.get_user_response(self.reviewedCards, self.responses)
            self.window.mainloop()

    def show_answer(self):
        self.lblAnswer = Label(self.window, text = self.a)
        self.lblAnswer.grid(row = 2, column = 0, padx= 20, pady= 10)
        
        self.btnYes = Button(self.window, text = "Yes Answer's Right!", command= self.responses.append(1))
        self.btnYes.grid(row = 3, column = 0, padx= 20, pady= 10)

        self.btnNo = Button(self.window, text = "No Answer's Wrong!", command= self.responses.append(-1))
        self.btnNo.grid(row = 4, column = 0, padx= 20, pady= 10)