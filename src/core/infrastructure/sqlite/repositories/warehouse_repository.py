from core.domain.repositories.interfaces import IWarehouseRepository
from core.infrastructure.sqlite.database import Base
from core.infrastructure.sqlite.models import WarehouseModel
from core.infrastructure.sqlite.repositories.base_repository import BaseRepository


class WarehouseRepository(BaseRepository, IWarehouseRepository):
    model: Base = WarehouseModel
