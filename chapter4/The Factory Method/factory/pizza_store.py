from abc import ABC, abstractmethod


class PizzaStore(ABC):

    @abstractmethod
    def create_pizza(self,type):
        pass

    def order_pizza(self, type):
        pizza = self.create_pizza(type)

        pizza.prepare()
        pizza.bake()
        pizza.box()
        pizza.cut()