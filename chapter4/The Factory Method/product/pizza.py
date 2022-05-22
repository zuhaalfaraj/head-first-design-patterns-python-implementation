from abc import ABC, abstractmethod


class Pizza(ABC):
    TOPPINGS = []
    NAME = None
    DOUGH = None
    SAUCE = None


    @classmethod
    def prepare(cls):
        print('Preparing {}'.format(cls.NAME))
        print('Tossing {}'.format(cls.DOUGH))
        print('Adding {}'.format(cls.SAUCE))
        print('Adding toppings: ')
        for i,top in enumerate(cls.TOPPINGS):
            print('{}. {}'.format(i,top))


    def bake(self):
        print('Bake for 25 minutes')

    def cut(self):
        print('cutting the pizza into diagonal slices')

    def box(self):
        print('Place the pizza into official PizzaStore box')