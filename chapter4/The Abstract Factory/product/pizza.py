from abc import ABC, abstractmethod


class Pizza(ABC):
    TOPPINGS = []
    NAME = None
    DOUGH = None
    SAUCE = None
    CHEESE = None


    @abstractmethod
    def prepare(self):
        pass


    def bake(self):
        print('Bake for 25 minutes')

    def cut(self):
        print('cutting the pizza into diagonal slices')

    def box(self):
        print('Place the pizza into official PizzaStore box')


