from abc import ABC, abstractmethod
from factory.ingredient_factory import *
from product.concrete import *

class PizzaStore(ABC):

    @abstractmethod
    def create_pizza(self, type):
        pass

    def order_pizza(self, type):
        pizza = self.create_pizza(type)

        pizza.prepare()
        pizza.bake()
        pizza.box()
        pizza.cut()


class NYPizzaStore(PizzaStore):
    def create_pizza(self, type):
        pizza = None
        ingredientFactory = NYPizzaIngredientFactory()
        if type == "cheese":
            pizza = CheesePizza(ingredientFactory)

        return pizza



class ChicagoPizzaStore(PizzaStore):
    def create_pizza(self, type):
        pizza = None
        ingredientFactory = ChicagoPizzaIngredientFactory()
        if type == "cheese":
            pizza = CheesePizza(ingredientFactory)

        return pizza


