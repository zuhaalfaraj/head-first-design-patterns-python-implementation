import abc

class Subject(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def register_observer(self, observer):
        raise NotImplementedError

    @abc.abstractmethod
    def remove_observer(self, observer):
        raise NotImplementedError

    @abc.abstractmethod
    def notify_observers(self):
        raise NotImplementedError