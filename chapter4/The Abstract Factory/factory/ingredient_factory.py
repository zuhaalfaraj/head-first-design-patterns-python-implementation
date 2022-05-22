from abc import ABC, abstractmethod
from .plain_ingredient import *


class PizzaIngredientFactory(ABC):

    @abstractmethod
    def createDough(self): pass

    @abstractmethod
    def createSauce(self): pass

    @abstractmethod
    def createCheese(self): pass


class NYPizzaIngredientFactory(PizzaIngredientFactory):
    def createDough(self):
        return ThinCrustDough().determine()

    def createSauce(self):
        return MarinaraSauce().determine()

    def createCheese(self):
        return ReggianoCheese().determine()


class ChicagoPizzaIngredientFactory(PizzaIngredientFactory):
    def createDough(self):
        return ThickCrustDough().determine()

    def createSauce(self):
        return PlumTomatoSauce().determine()

    def createCheese(self):
        return MozzarellaCheese().determine()
