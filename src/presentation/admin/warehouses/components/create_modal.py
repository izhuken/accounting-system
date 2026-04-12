from core.domain.entities import Warehouse
from core.domain.value_objects.warehouse import WarehouseAddress
from core.service.app import WarehouseService
from shared.components.common_input import CommonInput
from shared.components.form import CommonCreateModal


class WarehouseCreateModal(CommonCreateModal):
    modal_title = "Новый склад"
    topic_name = "warehouse_list_page__refetch"
    entity = Warehouse
    entity_service = WarehouseService

    def __init__(self):
        super().__init__(
            {
                "name": CommonInput(label="Наименование"),
                "city": CommonInput(label="Город"),
                "street": CommonInput(label="Улица"),
                "house": CommonInput(label="Дом"),
                "building": CommonInput(label="Строение"),
            }
        )

    def create_entity(self, payload: dict) -> Warehouse:
        return Warehouse.create(
            name=payload.get("name"),
            address=WarehouseAddress(
                city=payload.get("city"),
                street=payload.get("street"),
                house=payload.get("house"),
                building=payload.get("building"),
            ),
        )
