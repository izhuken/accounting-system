from core.domain.entities import Contractor
from core.domain.value_objects.contractor.contractor_address import ContractorAddress
from core.service.app import ContractorService
from shared.components.common_input import CommonInput
from shared.components.form import CommonUpdateModal


class ContractorUpdateModal(CommonUpdateModal):
    modal_title: str = "Редактирование исполнителя"
    topic_name: str = "contractor_list_page__refetch"
    entity = Contractor
    entity_service = ContractorService

    def __init__(self, payload: dict):
        super().__init__(
            payload,
            {
                "name": CommonInput(label="Имя подрядчика"),
                "phone": CommonInput(label="Телефон"),
                "email": CommonInput(label="E-mail"),
                "city": CommonInput(label="Город"),
                "street": CommonInput(label="Улица"),
                "house": CommonInput(label="Дом"),
                "building": CommonInput(label="Строение"),
            },
        )

    def update_entity(self, payload: dict, entity: Contractor) -> Contractor:
        entity.update_name(payload.get("name"))
        entity.update_phone(payload.get("phone"))
        entity.update_email(payload.get("email"))
        entity.update_address(
            ContractorAddress(
                city=payload.get("city"),
                street=payload.get("street"),
                house=payload.get("house"),
                building=payload.get("building"),
            )
        )
        return entity
