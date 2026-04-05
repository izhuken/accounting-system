from datetime import datetime
from uuid import UUID, uuid4

from sqlalchemy import DateTime, Enum, func
from sqlalchemy.orm import Mapped, mapped_column

from core.domain.entities.user import User
from core.domain.value_objects.user import UserId, UserPassword, UserStatus
from core.infrastructure.sqlite.database import Base
from core.infrastructure.sqlite.fields import EncryptedString


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

    def to_entity(self) -> User:
        return User(
            id=UserId(self.id),
            username=self.username,
            password=UserPassword(self.password, is_hash=True),
            status=self.status,
            created_at=self.created_at,
            updated_at=self.updated_at,
        )

    @staticmethod
    def from_entity(entity: User) -> UserModel:
        return UserModel(
            id=entity.id.value,
            username=entity.username.value,
            password=entity.password.value,
            status=entity.status,
            created_at=entity.created_at,
            updated_at=entity.updated_at,
        )
