from datetime import datetime
from typing import Optional
from uuid import UUID, uuid4

from sqlalchemy import DateTime, ForeignKey, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from core.domain.entities import Product
from core.domain.value_objects.product import ProductId
from core.infrastructure.sqlite.database import Base
from core.infrastructure.sqlite.fields import EncryptedString


class ProductModel(Base):
    __tablename__ = "products"

    id: Mapped[UUID] = mapped_column(primary_key=True, default=uuid4, unique=True)
    name: Mapped[str] = mapped_column(EncryptedString, nullable=False, unique=True)

    # foreign keys
    size_id: Mapped[UUID] = mapped_column(
        ForeignKey("sizes.code", ondelete="RESTRICT"), nullable=True
    )
    color_id: Mapped[UUID] = mapped_column(
        ForeignKey("colors.id", ondelete="RESTRICT"), nullable=True
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now()
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now(), onupdate=func.now()
    )

    size: Mapped[Optional["SizeModel"]] = relationship(backref="products")
    color: Mapped[Optional["ColorModel"]] = relationship(backref="products")

    def to_entity(self) -> Product:
        return Product(
            id=ProductId(self.id),
            name=self.name,
            size=self.size.to_entity() if self.size else None,
            color=self.color.to_entity() if self.color else None,
            created_at=self.created_at,
            updated_at=self.updated_at,
        )

    @staticmethod
    def from_entity(entity: Product) -> ProductModel:
        return ProductModel(
            id=entity.id.value,
            name=entity.name.value,
            size_id=entity.size.code.value if entity.size else None,
            color_id=entity.color.id.value if entity.color else None,
            created_at=entity.created_at,
            updated_at=entity.updated_at,
        )
