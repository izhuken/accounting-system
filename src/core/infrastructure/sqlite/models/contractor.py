from datetime import datetime
from uuid import UUID, uuid4

from sqlalchemy import DateTime, func
from sqlalchemy.orm import Mapped, mapped_column

from core.domain.entities.contractor import Contractor
from core.domain.value_objects.contractor import (
    ContractorAddress,
    ContractorId,
)
from core.infrastructure.sqlite.database import Base
from core.infrastructure.sqlite.fields import EncryptedString


class ContractorModel(Base):
    __tablename__ = "contractors"

    id: Mapped[UUID] = mapped_column(primary_key=True, default=uuid4, unique=True)
    name: Mapped[str] = mapped_column(EncryptedString, nullable=False)
    email: Mapped[str] = mapped_column(EncryptedString, nullable=True, default=None)
    phone: Mapped[str] = mapped_column(EncryptedString, nullable=True, default=None)

    # address
    city: Mapped[str] = mapped_column(EncryptedString, nullable=False)
    street: Mapped[str] = mapped_column(EncryptedString, nullable=True, default=None)
    house: Mapped[str] = mapped_column(EncryptedString, nullable=True, default=None)
    building: Mapped[str] = mapped_column(EncryptedString, nullable=True, default=None)

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now()
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now(), onupdate=func.now()
    )

    def to_entity(self) -> Contractor:
        return Contractor(
            id=ContractorId(self.id),
            name=self.name,
            phone=self.phone,
            email=self.email,
            address=ContractorAddress(
                city=self.city,
                street=self.street,
                house=self.house,
                building=self.building,
            ),
            created_at=self.created_at,
            updated_at=self.updated_at,
        )

    @staticmethod
    def from_entity(entity: Contractor) -> ContractorModel:
        return ContractorModel(
            id=entity.id.value,
            name=entity.name.value,
            phone=entity.phone.value,
            email=entity.email.value,
            city=entity.address.city,
            street=entity.address.street,
            house=entity.address.house,
            building=entity.address.building,
            created_at=entity.created_at,
            updated_at=entity.updated_at,
        )
