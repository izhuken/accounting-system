class Entity:
    def __dict__(self) -> dict:
        return self.to_dict()

    def to_dict(self) -> dict:
        raise NotImplementedError
