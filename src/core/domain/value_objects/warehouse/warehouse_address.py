from dataclasses import dataclass


@dataclass(frozen=True)
class StockAddress:
    city: str
    street: str
    house: str
    building: str | None

    def __str__(self) -> str:
        return (
            f"г. {self.city}, ул. {self.street}, д. {self.house}" + ""
            if not self.building
            else f"/{self.building}"
        )

    def __eq__(self, obj: object) -> bool:
        if isinstance(obj, type(self)):
            return (
                self.city == obj.city
                and self.street == obj.street
                and self.house == obj.house
                and self.building == obj.building
            )

        return False
