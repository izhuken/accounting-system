from core.domain.repositories.interfaces import IContractorRepository
from core.infrastructure.sqlite.database import Base
from core.infrastructure.sqlite.models import ContractorModel
from core.infrastructure.sqlite.repositories.base_repository import BaseRepository


class ContractorRepository(BaseRepository, IContractorRepository):
    model: Base = ContractorModel
