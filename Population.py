import random
from numpy.random import choice

from Breeder import Breeder
from Cat import Cat


class Population:
    def __init__(self):
        self.females = []
        self.males = []

    def add_cat_from_data(self, data):
        cat = Cat(name='test', **data)
        self.add_cat(cat)

    def add_cat(self, cat):
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

    def breed_population(self):
        next_population = Population()
        for female in self.females:
            fathers = choice([0, 1, 2], 1, p=[0.20, 0.30, 0.50])
            if fathers == 1:
                breeder = Breeder(female, random.choice(self.males))
                for i in range(random.randint(3, 5)):
                    next_population.add_cat(breeder.breed())
            elif fathers == 2:
                breeder = Breeder(female, random.choice(self.males), random.choice(self.males))
                for i in range(random.randint(3, 5)):
                    next_population.add_cat(breeder.breed())
        return next_population