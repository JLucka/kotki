from random import random, randint
from numpy.random import choice

from Breeder import Breeder
from Cat import Cat

class CatCreator:
    def __init__(self):
        self.cat = Cat()

    def get_random_cat(self, gender=None):
        self.cat.gender = gender or randint(0,1)
        self.cat.genes["black"] = [randint(0,2), randint(0,2)]
        self.cat.genes["orange"] = [randint(0,1), randint(0,1)]
        self.cat.genes["density"] = [randint(0,1), randint(0,1)]
        self.cat.genes["dilute"] = [randint(0,1), randint(0,1)]
        self.cat.genes["agouti"] = [randint(0,1), randint(0,1)]
        self.cat.genes["mackarel"] = [randint(0,1), randint(0,1)]
        self.cat.genes["ticked"] = [randint(0,1), randint(0,1)]
        self.cat.genes["albino"] = [choice([0, 1, 2, 3, 4], 1, p=[0.70, 0.10, 0.10, 0.05, 0.05]),
                                    choice([0, 1, 2, 3, 4], 1, p=[0.70, 0.10, 0.10, 0.05, 0.05])]
        self.cat.genes["white"] = [choice([0, 1], 1, p=[0.15, 0.85]), choice([0, 1], 1, p=[0.15, 0.85])]
        self.cat.genes["spots"] = [randint(0,2), randint(0,2)]

        return self.cat


    def get_patterned_cat(self):
        self.cat.gender = randint(0,1)
        self.cat.genes["black"] = [randint(0,2), randint(0,2)]
        self.cat.genes["orange"] = [randint(0,1), randint(0,1)]
        self.cat.genes["density"] = [randint(0,1), randint(0,1)]
        self.cat.genes["dilute"] = [randint(0,1), randint(0,1)]
        self.cat.genes["agouti"] = [0, 0]
        self.cat.genes["mackarel"] = [randint(0,1), randint(0,1)]
        self.cat.genes["ticked"] = [randint(0,1), randint(0,1)]
        self.cat.genes["albino"] = [0, 0]
        self.cat.genes["white"] = [1, 1]
        self.cat.genes["spots"] = [randint(0,2), randint(0,2)]
        return self.cat

