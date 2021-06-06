import abc

from Behavior.fly_behaviors import FlyWithWings, FlyNoWay
from Behavior.quack_behaviors import Quack


class Duck (metaclass=abc.ABCMeta):
    def __init__(self,quack_behavior = None,fly_behavior= None ):
        self.quack_behavior = quack_behavior
        self.fly_behavior = fly_behavior

    def set_fly_behavior(self, fly_behavior):
        self.fly_behavior = fly_behavior

    def set_quack_behavior(self, quack_behavior):
        self.quack_behavior = quack_behavior

    def perform_fly(self):
        if self.fly_behavior is not None:
            self.fly_behavior.fly()
        else:
            raise NotImplementedError

    def perform_quack(self):
        if self.quack_behavior is not None:
            self.quack_behavior.quack()
        else:
            raise NotImplementedError


    def swim(self):
        print("All ducks float, even decoys!")

    @abc.abstractmethod
    def display(self):

        raise NotImplementedError



class MallardDuck(Duck):
    def display(self):
        print("I'm a real Mallard duck")

    def __init__(self):
        self.quack_behavior = Quack()
        self.fly_behavior = FlyWithWings()
        super().__init__(self.quack_behavior, self.fly_behavior)



class ModelDuck(Duck):

    def __init__(self):
        self.quack_behavior = Quack()
        self.fly_behavior = FlyNoWay()
        super().__init__(self.quack_behavior,self.fly_behavior)

    def display(self):
        print("I'm a model duck")
