from core.domain.repositories.interfaces import IProductRepository
from core.infrastructure.sqlite.models import ProductModel
from core.infrastructure.sqlite.repositories.base_repository import BaseRepository


class ProductRepository(BaseRepository, IProductRepository):
    model: ProductModel = ProductModel
    additional_fields = ["size", "color"]
