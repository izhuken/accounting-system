from datetime import datetime
from uuid import UUID, uuid4

from sqlalchemy import DateTime, Enum, func
from sqlalchemy.orm import Mapped, mapped_column

from core.domain.value_objects.user import UserStatus
from core.infrastructure.sqlite.database import Base
from core.infrastructure.sqlite.fields.encrypted_string import EncryptedString


class UserModel(Base):
    __tablename__ = "user"

    id: Mapped[UUID] = mapped_column(primary_key=True, default=uuid4, unique=True)

    username: Mapped[str] = mapped_column(EncryptedString, nullable=False, unique=True)
    password: Mapped[str] = mapped_column(nullable=False)
    status: Mapped[UserStatus] = mapped_column(
        Enum(UserStatus), nullable=False, default=UserStatus.INACTIVE
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now()
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now(), onupdate=func.now()
    )
