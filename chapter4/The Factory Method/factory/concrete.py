from factory.pizza_store import PizzaStore
from product.concrete import *

class NYStylePizzaStore(PizzaStore):
    def create_pizza(self,type):
        if type == "cheese":
            pizza = NYStyleCheesePizza()

        elif type == "pepperoni":
            pizza = NYStylePepperoniPizza()

        elif type == "clam":
            pizza = NYStyleClamPizza()

        elif type == "veggie":
            pizza = NYStyleVeggiePizza()

        return pizza


class ChicagoStylePizzaStore(PizzaStore):
    def create_pizza(self, type):
        if type == "cheese":
            pizza = ChicagoStyleCheesePizza()

        elif type == "pepperoni":
            pizza = ChicagoStylePepperoniPizza()

        elif type == "clam":
            pizza = ChicagoStyleClamPizza()

        elif type == "veggie":
            pizza = ChicagoStyleVeggiePizza()

        return pizza