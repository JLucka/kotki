class Cat:

    def __init__(self, gender=0, name='Maciek', **params):
        self.gender = gender
        self.name = name
        self.genes = {
            "black": [0, 0],
            "orange": [1, 1],
            "density": [0, 0],
            "dilute": [1, 1],
            'agouti': [0, 0],
            'mackarel': [1, 1],
            'ticked': [1, 1],
            'ember': [0, 0],
            'albino': [0, 0],
            'white': [1, 1],
            'spots': [1, 1],
        }
        for i in params:
            self.genes[i] = params[i]
        # Orange gene is sex-linked, so males only have one
        if gender == 1:
            self.genes['orange'][1] = 1

    def print(self):
        print (self.name)
        print (self.gender)
        print (self.genes)

    def describe(self):
        if min(self.genes['albino']) == 4:
            print("Kot to całkowity albinos. Ma różowe oczka")
        elif min(self.genes['albino']) == 3:
            print("Kot to albinos. Ma niebieskie oczka")
        elif min(self.genes['albino']) == 2:
            print("Kot ma znaczenia syjamskie")
        elif min(self.genes['albino']) == 1 and max(self.genes['albino']) == 2:
            print("Kot ma znaczenia tonkijskie")
        elif min(self.genes['albino']) == 1:
            print("Kot ma znaczenia burmskie")
        else:
            print("Kot nie ma dodatkowych znaczeń")




