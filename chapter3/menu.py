from Models.beverage import BeveragIeAbstract
from Models.decorator import CondimentDecorator


#### BEVERAGES ####
class Espresso(BeveragIeAbstract):
    DESCRIPTION = "Your favourite Espresso"

    def cost(self) -> float:
        return  1.99


class HouseBlend(BeveragIeAbstract):
    DESCRIPTION = "House Blend Coffee"

    def cost(self) -> float:
        return 0.89


#### Condiments ####

class Mocha(CondimentDecorator):
    def __init__(self, beverage):
        self.beverage = beverage

    def get_description(self):
        return self.beverage.get_description() + ' Mocha'

    def cost(self):
        return self.beverage.cost() + 0.2