import os
from box import *
from card import *
from main_form import *

menu =("Add new card",
       "Review",
       "Statistics",
       "Show archive cards",
       "Show box cards",
       "Exit"
)

def clear_screen(inp):
    if inp == 1 :
        input("press enter to continue")
    if os.name == "nt":
        os.system("cls")

def show_menu():
    i = 1
    for item in menu:
        message ="{}- {}".format(i, item)
        i += 1
        print(message)
    userChoice = int(input("Please enter your choice: "))
    return userChoice

def main():
    clear_screen(0)
    box = Box()
    while True:
        userChoice = show_menu()

        if userChoice == 1:
            question, answer = input("Please enter question: "), input("Please enter answer: ")
            c = Card(question, answer)
            box.add_new_card(c)
            print("Card added successfully!")

        elif userChoice == 2:
            clear_screen(0)
            reviewCards = box.review()
            if len(reviewCards) == 0 :
                print("no review today")
            else:
                reviewdCards = []
                responses = []
                for card in reviewCards:
                    q, a = card.get_information()
                    print(q)
                    input("Press enter to show answer")
                    print(a)
                    response = int(input("Enter 1 if you have guessed correctly or 2 if you have not: "))
                    if response == 1:
                        responses.append(1)
                    elif response == 2:
                        responses.append(-1)
                    reviewdCards.append(card)
                box.get_user_response(reviewCards, responses)

        elif userChoice == 3:
            print(box.get_statistics())

        elif userChoice == 4:
            print(box.get_archive_cards_information())

        elif userChoice == 5:
            print(box.get_all_boxcards_information())

        elif userChoice == 6:
            break

        clear_screen(1)

#main()

box = Box()
f = MainForm(box)

