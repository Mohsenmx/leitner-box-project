from tkinter import *
from tkinter import messagebox

# create the root window
window = Tk()
window.geometry("500x500")
window.title('Review Cards')
window.resizable(False, False)


# create a list box
langs = ["card1", "card2", "card3"]

var = Variable(value=langs)

listbox = Listbox(
    window,
    listvariable=var,
    height= len(langs),
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

window.mainloop()