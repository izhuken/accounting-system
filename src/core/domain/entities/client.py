from datetime import datetime

from core.domain.value_objects.client import (
    ClientAddress,
    ClientEmail,
    ClientId,
    ClientName,
    ClientPhone,
)


class Client:
    def __init__(
        self,
        id: ClientId,
        name: ClientName,
        phone: ClientPhone,
        email: ClientEmail,
        address: ClientAddress,
        created_ad: datetime = datetime.now(),
        updated_at: datetime = datetime.now(),
    ):
        self._id = id
        self._name = name
        self._phone = phone
        self._email = email
        self._address = address
        self._created_ad = created_ad
        self._updated_at = updated_at

    @property
    def id(self) -> ClientId:
        return self._id

    @property
    def name(self) -> ClientName:
        return self._name

    def phone(self) -> ClientPhone:
        return self._phone

    def email(self) -> ClientEmail:
        return self._email

    def address(self) -> ClientAddress:
        return self._address

    @property
    def created_at(self) -> datetime:
        return self._created_ad

    @property
    def updated_at(self) -> datetime:
        return self._updated_at

    def update_name(self, name: ClientName) -> None:
        self._name = name
        self._updated_at = datetime.now()

    def update_phone(self, phone: ClientPhone) -> None:
        self._phone = phone
        self._updated_at = datetime.now()

    def update_email(self, email: ClientEmail) -> None:
        self._email = email
        self._updated_at = datetime.now()

    def update_address(self, address: ClientAddress) -> None:
        self._address = address
        self._updated_at = datetime.now()

    @staticmethod
    def create(
        name: ClientName, phone: ClientPhone, email: ClientEmail, address: ClientAddress
    ) -> Client:
        return Client(
            id=ClientId.generate(),
            name=name,
            phone=phone,
            email=email,
            address=address,
        )
