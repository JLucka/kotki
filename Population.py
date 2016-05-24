import random

from Cat import Cat


class Population:
    def __init__(self):
        self.females = []
        self.males = []

    def add_cat_from_data(self, data):
        cat = Cat(name='test', **data)
        if cat.gender == 0:
            self.females.append(cat)
        else:
            self.males.append(cat)
        cat.describe()

    def get_male_cat(self):
        self.males.remove(random.choice(list(self.males)))

    def get_female_cat(self):
        self.males.remove(random.choice(list(self.males)))

    def to_json(self):
        females =[c.serialize() for c in self.females]
        males =[c.serialize() for c in self.males]
        return females + males