from data import *
from datetime import *

class Box:
    def __init__(self):
        self.dataBase = DataBase()
        self.currentDate = datetime.today()
        self.lastDate = self.dataBase.read_last_date()
        if self.lastDate == None:#this line for the first launch of app which we don not have last date
            self.lastDate = datetime.today()
        self.dataBase.save_date(self.currentDate)
        self.move_cards()

    def add_new_card(self, card):
        self.dataBase.insert_new_card(card)
    
    def move_cards(self):
        difference = self.difference_between_current_last_date()
        if difference != 0 :
            if len(self.dataBase.box) != 0 :
                for card in self.dataBase.box:
                    if card.day == card.review :
                        continue
                    else:
                        for i in range(difference):
                            card.day += 1
                            if card.day == card.review :
                                break
                self.dataBase.save_cards()

    def move_after_review(self, cards, responses):
        for i in range(len(cards)):
            if cards[i].review == 16 :
                if responses[i] == 1 :
                    self.dataBase.archive.append(cards[i])
                    self.dataBase.box.remove(cards[i])
                elif responses[i] == -1 :
                    cards[i].review = 1
                    cards[i].day = 0
            else:
                if responses[i] == 1 :
                    cards[i].review *= 2
                    cards[i].day = 0
                elif responses[i] == -1 :
                    cards[i].review = 1
                    cards[i].day = 0
        self.dataBase.save_cards()
        self.dataBase.save_archive_cards()

    def review(self):
        reviewList = []
        for card in self.dataBase.box:
            if card.day == card.review :
                reviewList.append(card)
        return reviewList

    def get_user_response(self, cards, response):
        self.move_after_review(cards, response)

    def difference_between_current_last_date(self):
        difference = (self.currentDate - self.lastDate).days
        return difference

    def get_all_boxcards_information(self):
        message = "Box Cards".center(20, "*")+"\n"
        for card in self.dataBase.box:
            q, a = card.get_information()
            message +="{} , {} \n".format(q, a)
        return message
    
    def get_archive_cards_information(self):
        message ="Archive Cards".center(20, "*")+"\n" 
        for card in self.dataBase.archive:
            q, a = card.get_information()
            message +="{} , {} \n".format(q, a)
        return message

    def get_statistics(self):
        message = f"cards in box: {len(self.dataBase.box)}\n" + f"cards in archive: {len(self.dataBase.archive)}"
        return message