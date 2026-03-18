from datetime import datetime

from core.domain.entities.entity import Entity
from core.domain.value_objects.contractor import (
    ContractorAddress,
    ContractorEmail,
    ContractorId,
    ContractorName,
    ContractorPhone,
)


class Contractor(Entity):
    def __init__(
        self,
        id: ContractorId,
        name: ContractorName,
        phone: ContractorPhone,
        email: ContractorEmail,
        address: ContractorAddress,
        created_at: datetime = datetime.now(),
        updated_at: datetime = datetime.now(),
    ):
        self._id = id
        self._name = name
        self._phone = phone
        self._email = email
        self._address = address
        self._created_at = created_at
        self._updated_at = updated_at

    @property
    def id(self) -> ContractorId:
        return self._id

    @property
    def name(self) -> ContractorName:
        return self._name

    def phone(self) -> ContractorPhone:
        return self._phone

    def email(self) -> ContractorEmail:
        return self._email

    def address(self) -> ContractorAddress:
        return self._address

    @property
    def created_at(self) -> datetime:
        return self._created_at

    @property
    def updated_at(self) -> datetime:
        return self._updated_at

    def update_name(self, name: ContractorName) -> None:
        self._name = name
        self._updated_at = datetime.now()

    def update_phone(self, phone: ContractorPhone) -> None:
        self._phone = phone
        self._updated_at = datetime.now()

    def update_email(self, email: ContractorEmail) -> None:
        self._email = email
        self._updated_at = datetime.now()

    def update_address(self, address: ContractorAddress) -> None:
        self._address = address
        self._updated_at = datetime.now()

    @staticmethod
    def create(
        name: ContractorName,
        phone: ContractorPhone,
        email: ContractorEmail,
        address: ContractorAddress,
    ) -> Contractor:
        return Contractor(
            id=ContractorId.generate(),
            name=name,
            phone=phone,
            email=email,
            address=address,
        )
