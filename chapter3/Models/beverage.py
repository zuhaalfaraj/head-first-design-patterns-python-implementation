from abc import ABC, abstractmethod


class BeveragIeAbstract(ABC):
    DESCRIPTION = None

    @classmethod
    def get_description(cls) -> str:
        return cls.DESCRIPTION

    @abstractmethod
    def cost(self) -> float:
        pass

