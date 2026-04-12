from core.domain.entities import Warehouse
from core.domain.value_objects.warehouse import WarehouseAddress
from core.service.app import WarehouseService
from shared.components.common_input import CommonInput
from shared.components.form import CommonUpdateModal


class WarehouseUpdateModal(CommonUpdateModal):
    modal_title = "Редактирование склада"
    topic_name = "warehouse_list_page__refetch"
    entity = Warehouse
    entity_service = WarehouseService

    def __init__(self, payload: dict):
        super().__init__(
            payload,
            {
                "name": CommonInput(label="Наименование"),
                "city": CommonInput(label="Город"),
                "street": CommonInput(label="Улица"),
                "house": CommonInput(label="Дом"),
                "building": CommonInput(label="Строение"),
            },
        )

    def update_entity(self, payload: dict, entity: Warehouse) -> Warehouse:
        entity.update_name(payload.get("name"))
        entity.update_address(
            WarehouseAddress(
                city=payload.get("city"),
                street=payload.get("street"),
                house=payload.get("house"),
                building=payload.get("building"),
            )
        )
        return entity
