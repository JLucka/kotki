#!/usr/bin/python
# -*- coding: utf-8 -*-
from Fenotype import Fenotype


class Cat:

    def __init__(self, gender=0, name='Maciek', **params):
        self.gender = gender
        self.name = name
        self.genes = {
            "black": [0, 0],
            "orange": [1, 1],
            "density": [0, 0],
            "dilute": [1, 1],
            'agouti': [1, 1],
            'mackarel': [1, 1],
            'ticked': [0, 1],
            'albino': [0, 0],
            'white': [1, 1],
            'spots': [0, 1],
        }
        for i in params:
            self.genes[i] = params[i]
        # Orange gene is sex-linked, so males only have one
        if gender == 1:
            self.genes['orange'][1] = self.genes['orange'][0]
        self.fenotype = Fenotype()

    def describe(self):
        if self.gender == 1:
            self.genes['orange'][1] = self.genes['orange'][0]
        if self.gender:
            print("Kot jest płci męskiej")
        else:
            print("Kot jest płci żeńskiej")
        self.check_if_albino()

    def check_if_albino(self):
        if min(self.genes['albino']) == 4:
            self.fenotype.albino = "full"
            self.fenotype.base_color = "white"
            print("Kot to całkowity albinos. Ma różowe oczka")
        elif min(self.genes['albino']) == 3:
            self.fenotype.albino = "full"
            self.fenotype.base_color = "white"
            print("Kot to albinos. Ma niebieskie oczka")
        elif min(self.genes['albino']) == 2:
            print("Kot ma znaczenia syjamskie")
            self.fenotype.albino = "siamese"
            self.check_if_white()
        elif min(self.genes['albino']) == 1 and max(self.genes['albino']) == 2:
            self.fenotype.albino = "tonkese"
            print("Kot ma znaczenia tonkijskie")
            self.check_if_white()
        elif min(self.genes['albino']) == 1:
            self.fenotype.albino = "burmese"
            print("Kot ma znaczenia burmskie")
            self.check_if_white()
        else:
            self.check_if_white()

    def check_if_white(self):
        if min(self.genes['white']) == 0:
            self.fenotype.base_color = "white"
            print("Kot jest koloru white")
        else:
            self.check_if_orange()

    def check_if_orange(self):
        if min(self.genes['orange']) == 0 and max(self.genes['orange']) == 0:
            self.check_if_dense('orange')
        elif min(self.genes['orange']) == 0 and max(self.genes['orange']) == 1:
            self.check_black()
            self.check_if_dense('orange')
        else:
            self.check_black()

    def check_if_dense(self, color):
        color_hash = {'orange': 'cream', 'black': 'blue', 'chocolate': 'lilac', 'cinnamon': 'fawn'}
        if min(self.genes['density']) == 0:
            print("Kot jest koloru " + color)
            if self.fenotype.base_color == "":
                self.fenotype.base_color = color
            else:
                self.fenotype.torbie = color
            self.check_agouti()
        else:
            new_color = color_hash[color]
            self.check_if_diluted(new_color)

    def check_if_diluted(self, color):
        color_hash = {'cream': 'apricot', 'blue': 'blue caramel', 'lilac': 'lilac caramel', 'fawn': 'fawn caramel'}
        if min(self.genes['dilute']) == 0:
            color = color_hash[color]
        print("Kot jest koloru " + color)
        if self.fenotype.base_color == "":
            self.fenotype.base_color = color
        else:
            self.fenotype.torbie = color

        self.check_agouti()

    def check_black(self):
        if min(self.genes['black']) == 0:
            self.check_if_dense('black')
        elif min(self.genes['black']) == 1:
            self.check_if_dense('chocolate')
        else:
            self.check_if_dense('cinnamon')

    def check_agouti(self):
        if min(self.genes['agouti']) == 0:
            self.check_for_patterns()
        else:
            self.check_for_white_spots()

    def check_for_patterns(self):
        if min(self.genes['mackarel']) == 0:
            print("Kot ma znaczenia tygrysie")
            self.fenotype.pattern = "tiger"
        else:
            print("Kot ma znaczenia klasyczne")
            self.fenotype.pattern = "classic"
        self.check_if_ticked()

    def check_if_ticked(self):
        if min(self.genes['ticked']) == 0 and max(self.genes['ticked']) == 0:
            print ("Znaczenia kota są rozmyte")
            self.fenotype.pattern = "ticked"
        elif min(self.genes['ticked']) == 0:
            print("Znaczenia kota są lekko rozmyte")
            self.fenotype.pattern = "ticked-" + self.fenotype.pattern
        self.check_for_white_spots()

    def check_for_white_spots(self):
        if min(self.genes['spots']) == 0 and max(self.genes['spots']) != 1:
            print("Kot ma dużo białych łat")
            self.fenotype.spots = 'big'
        elif min(self.genes['spots']) == 0 and max(self.genes['spots']) == 1:
            print("Kot ma trochę białych łat")
            self.fenotype.spots = 'medium'
        elif min(self.genes['spots']) == 1:
            print("Kot nie ma białych łat")
        else:
            print("Kot ma białe skarpetki")
            self.fenotype.spots = 'socks'