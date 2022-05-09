from Models.beverage import BeveragIeAbstract
from abc import abstractmethod

class CondimentDecorator(BeveragIeAbstract):

    @abstractmethod
    def get_description(self):
        pass
