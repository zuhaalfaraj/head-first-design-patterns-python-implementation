from . import *


class ThickCrustDough(Dough):
    def determine(self):
        print('ThickCrustDough')


class ThinCrustDough(Dough):
    def determine(self):
        print('ThinCrustDough')


class PlumTomatoSauce(Sauce):
    def determine(self):
        print('PlumTomatoSauce')


class MarinaraSauce(Sauce):
    def determine(self):
        print('MarinaraSauce')


class MozzarellaCheese(Cheese):
    def determine(self):
        print('MozzarellaCheese')


class ReggianoCheese(Cheese):
    def determine(self):
        print('ReggianoCheese')

