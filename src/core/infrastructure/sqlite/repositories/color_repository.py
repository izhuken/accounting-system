from core.domain.repositories.interfaces import IColorRepository
from core.infrastructure.sqlite.database import Base
from core.infrastructure.sqlite.models import ColorModel
from core.infrastructure.sqlite.repositories.base_repository import BaseRepository


class ColorRepository(BaseRepository, IColorRepository):
    model: Base = ColorModel
