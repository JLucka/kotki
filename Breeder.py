from random import random, randint

from Cat import Cat


class Breeder:
    def __init__(self, female, male, second_male = None):
        self.female = female
        self.male = male
        self.second_male = second_male

    def choose_parent(self):
        if self.second_male:
            parent = randint(0,1)
            if parent == 0:
                return self.male
            else:
                return self.second_male
        else:
            return self.male

    def breed(self):
        father = self.choose_parent()
        kitten_gender = randint(0,1)
        kitten_params = {}
        for i in self.female.genes:
            male_random = randint(0,1)
            female_random = randint(0,1)
            kitten_params[i] = [self.female.genes[i][female_random], father.genes[i][male_random]]
        return Cat(gender=kitten_gender, name='Maciek', **kitten_params)
