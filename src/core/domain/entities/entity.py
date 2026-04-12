from abc import ABC, abstractmethod


class Entity(ABC):
    def __dict__(self) -> dict:
        return self.to_dict()

    @abstractmethod
    def to_dict(self) -> dict:
        raise NotImplementedError

    @staticmethod
    def create(*args, **kwargs) -> Entity:
        raise NotImplementedError
