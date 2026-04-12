from core.domain.entities import Contractor
from core.domain.value_objects.contractor.contractor_address import ContractorAddress
from core.service.app.contractor_service import ContractorService
from shared.components.common_input import CommonInput
from shared.components.form import CommonCreateModal


class ContractorCreateModal(CommonCreateModal):
    modal_title = "Новый подрядчик"
    topic_name = "contractor_list_page__refetch"
    entity = Contractor
    entity_service = ContractorService

    def __init__(self):
        super().__init__(
            {
                "name": CommonInput(label="Имя подрядчика"),
                "phone": CommonInput(label="Телефон"),
                "email": CommonInput(label="E-mail"),
                "city": CommonInput(label="Город"),
                "street": CommonInput(label="Улица"),
                "house": CommonInput(label="Дом"),
                "building": CommonInput(label="Строение"),
            }
        )

    def create_entity(self, payload: dict) -> Contractor:
        return Contractor.create(
            name=payload.get("name"),
            phone=payload.get("phone"),
            email=payload.get("email"),
            address=ContractorAddress(
                city=payload.get("city"),
                street=payload.get("street"),
                house=payload.get("house"),
                building=payload.get("building"),
            ),
        )
