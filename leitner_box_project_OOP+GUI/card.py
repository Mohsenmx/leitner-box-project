class Card:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer
        self.day = 0
        self.review = 1

    def get_information(self):
        Question = "question: {}".format(self.question)
        Answer = "answer: {}".format(self.answer)
        return Question, Answer