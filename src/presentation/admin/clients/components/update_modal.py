from core.domain.entities import Client
from core.domain.value_objects.client import ClientAddress
from core.service.app import ClientService
from shared.components.common_input import CommonInput
from shared.components.form import CommonUpdateModal


class ClientUpdateModal(CommonUpdateModal):
    modal_title: str = "Редактирование клиента"
    topic_name: str = "client_list_page__refetch"
    entity = Client
    entity_service = ClientService

    def __init__(self, payload: dict):
        super().__init__(
            payload,
            {
                "name": CommonInput(label="Имя клиента"),
                "phone": CommonInput(label="Телефон"),
                "email": CommonInput(label="E-mail"),
                "city": CommonInput(label="Город"),
                "street": CommonInput(label="Улица"),
                "house": CommonInput(label="Дом"),
                "building": CommonInput(label="Строение"),
            },
        )

    def update_entity(self, payload: dict, entity: Client) -> Client:
        entity.update_name(payload.get("name"))
        entity.update_phone(payload.get("phone"))
        entity.update_email(payload.get("email"))
        entity.update_address(
            ClientAddress(
                city=payload.get("city"),
                street=payload.get("street"),
                house=payload.get("house"),
                building=payload.get("building"),
            )
        )
        return entity
