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
        name: str,
        phone: str,
        email: str,
        address: ContractorAddress,
        created_at: datetime = datetime.now(),
        updated_at: datetime = datetime.now(),
    ):
        self._id = id
        self._name = ContractorName(name)
        self._phone = ContractorPhone(phone)
        self._email = ContractorEmail(email)
        self._address = address
        self._created_at = created_at
        self._updated_at = updated_at

    @property
    def id(self) -> ContractorId:
        return self._id

    @property
    def name(self) -> ContractorName:
        return self._name

    @property
    def phone(self) -> ContractorPhone:
        return self._phone

    @property
    def email(self) -> ContractorEmail:
        return self._email

    @property
    def address(self) -> ContractorAddress:
        return self._address

    @property
    def created_at(self) -> datetime:
        return self._created_at

    @property
    def updated_at(self) -> datetime:
        return self._updated_at

    def update_name(self, name: str) -> None:
        self._name = ContractorName(name)
        self._updated_at = datetime.now()

    def update_phone(self, phone: str) -> None:
        self._phone = ContractorPhone(phone)
        self._updated_at = datetime.now()

    def update_email(self, email: str) -> None:
        self._email = ContractorEmail(email)
        self._updated_at = datetime.now()

    def update_address(self, address: ContractorAddress) -> None:
        self._address = address
        self._updated_at = datetime.now()

    def to_dict(self) -> dict:
        return {
            "id": self.id.value,
            "name": self.name.value,
            "phone": self.phone.value,
            "email": self.email.value,
            "city": self.address.city,
            "street": self.address.street,
            "house": self.address.house,
            "building": self.address.building,
            "full_address": str(self.address),
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat(),
        }

    @staticmethod
    def create(
        name: str, phone: str, email: str, address: ContractorAddress
    ) -> Contractor:
        return Contractor(
            id=ContractorId.generate(),
            name=name,
            phone=phone,
            email=email,
            address=address,
        )
