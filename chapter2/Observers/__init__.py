import abc

class Observer(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def update(self, temp, humidity, pressure):
        raise NotImplementedError

class DisplayElement:
    @abc.abstractmethod
    def display(self):
        raise NotImplementedError
