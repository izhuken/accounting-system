from core.domain.repositories.interfaces import IClientRepository
from core.infrastructure.sqlite.database import Base
from core.infrastructure.sqlite.models import ClientModel
from core.infrastructure.sqlite.repositories.base_repository import BaseRepository


class ClientRepository(BaseRepository, IClientRepository):
    model: Base = ClientModel
