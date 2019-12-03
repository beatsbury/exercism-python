import random


class Robot:
    def __init__(self):
        self.name = self.new_name()

    def new_name(self):
        alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        letter1 = self.get_letter()
        letter2 = self.get_letter()
        number1 = self.get_number()
        number2 = self.get_number()
        number3 = self.get_number()
        new_name = letter1 + letter2 + number1 + number2 + number3
        return new_name

    def get_letter(self):
        alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        return alphabet[random.randint(0, 25)]

    def get_number(self):
        return str(random.randint(0, 9))

    def reset(self):
        random_seed = random.random()
        random.seed(random_seed)
        self.name = self.new_name()
