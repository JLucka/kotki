from random import random


from Cat import Cat


class Breeder:
    def __init__(self, female, male, second_male = None):
        self.female = female
        self.male = male
        self.second_male = second_male

    def choose_parent(self):
        if self.second_male:
            parent = round(random())
            if parent == 0:
                return self.male
            else:
                return self.second_male
        else:
            return self.male

    def breed(self):
        father = self.choose_parent()
        kitten_gender = round(random())
        kitten_params = {}
        for i in self.female.genes:
            male_random = round(random())
            female_random = round(random())
            kitten_params[i] = [self.female.genes[i][female_random], father.genes[i][male_random]]
        return Cat(gender=kitten_gender, name='Maciek', **kitten_params)
