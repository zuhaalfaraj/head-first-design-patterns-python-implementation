import abc

class FlyBehavior(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def fly(self):
        raise NotImplementedError


class QuackBehavior(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def quack(self):
        raise NotImplementedError