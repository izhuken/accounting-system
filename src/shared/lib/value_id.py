from uuid import UUID

from core.domain.value_objects.common.id_object import (
    UIntValueObjectId,
    UUIDValueObjectId,
)


def value_id(_id: int | UUID) -> UUIDValueObjectId | UIntValueObjectId:
    if isinstance(_id, UUID):
        return UUIDValueObjectId.create(_id)

    return UIntValueObjectId.create(_id)
