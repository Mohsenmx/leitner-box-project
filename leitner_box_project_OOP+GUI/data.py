from card import *
from datetime import *

class DataBase:
    def __init__(self):
        self.box = []
        self.archive = []
        self.read_archive_cards()
        self.read_all_cards()
        
    def insert_new_card(self, card):
        self.box.append(card)
        self.save_cards()

    def save_cards(self):
        try:
            with open("D:/Dev/Python/myworks/leitner_box_project_OOP+GUI/data and setting/cards.csv", "w") as writer:
                for card in self.box:
                    newQuestion = card.question.replace(",", "-")
                    newAnswer = card.answer.replace(",", "-")
                    writer.write(f"{newQuestion},{newAnswer},{card.day},{card.review}\n")
            writer.close()
        except:
            print("something went wrong in cards.csv!!")

    def read_all_cards(self):
        try:
            with open("D:/Dev/Python/myworks/leitner_box_project_OOP+GUI/data and setting/cards.csv") as reader:
                for line in reader:
                    datas = line.split(",")

                    question = datas[0].replace("-", ",")
                    answer = datas[1].replace("-", ",")
                    day = int(datas[2])
                    review = int(datas[3])

                    c = Card(question, answer)
                    c.day = day
                    c.review = review
                    self.box.append(c)
            reader.close()
        except:
            print("something went wrong in cards.csv!!")

    def save_archive_cards(self):
        try:
            with open("D:/Dev/Python/myworks/leitner_box_project_OOP+GUI/data and setting/archive.csv", "w") as writer:
                for card in self.archive:
                    newQuestion = card.question.replace(",", "-")
                    newAnswer = card.answer.replace(",", "-")
                    newAnswer1 = newAnswer.replace("\n", "")
                    writer.write(f"{newQuestion},{newAnswer1}\n")
            writer.close()
        except:
            print("something went wrong in archive.csv!!")

    def read_archive_cards(self):
        try:
            with open("D:/Dev/Python/myworks/leitner_box_project_OOP+GUI/data and setting/archive.csv") as reader:
                for line in reader:
                    datas = line.split(",")

                    question = datas[0].replace("-", ",")
                    answer = datas[1].replace("-", ",")
                                    
                    c = Card(question, answer)
                    self.archive.append(c)
            reader.close()
        except:
            print("something went wrong in archive.csv!!")

    def save_date(self, currentDate):
        try:
            with open("D:/Dev/Python/myworks/leitner_box_project_OOP+GUI/data and setting/config.ini", "w") as writer:
                writer.write(f"{currentDate.year},{currentDate.month},{currentDate.day}\n")
            writer.close()
        except:
            print("something went wrong in config.ini!!")

    def read_last_date(self):
        try:
            with open("D:/Dev/Python/myworks/leitner_box_project_OOP+GUI/data and setting/config.ini") as reader:
                for line in reader:
                    datas = line.split(",")

                    lastDate = datetime(int(datas[0]), int(datas[1]), int(datas[2]))
                    return lastDate
            reader.close()
        except:
            print("something went wrong in config.ini!!")