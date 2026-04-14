from core.domain.repositories.interfaces import IMaterialRepository
from core.infrastructure.sqlite.database import Base
from core.infrastructure.sqlite.models import MaterialModel
from core.infrastructure.sqlite.repositories.base_repository import BaseRepository


class MaterialRepository(BaseRepository, IMaterialRepository):
    model: Base = MaterialModel
    additional_fields = ["metric"]
