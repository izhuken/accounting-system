from core.domain.entities import Client
from core.domain.value_objects.client import ClientAddress
from core.service.app import ClientService
from shared.components.common_input import CommonInput
from shared.components.form import CommonCreateModal


class ClientCreateModal(CommonCreateModal):
    modal_title = "Новый клиент"
    topic_name = "client_list_page__refetch"
    entity = Client
    entity_service = ClientService

    def __init__(self):
        super().__init__(
            {
                "name": CommonInput(label="Имя клиента"),
                "phone": CommonInput(label="Телефон"),
                "email": CommonInput(label="E-mail"),
                "city": CommonInput(label="Город"),
                "street": CommonInput(label="Улица"),
                "house": CommonInput(label="Дом"),
                "building": CommonInput(label="Строение"),
            }
        )

    def create_entity(self, payload: dict) -> Client:
        return Client.create(
            name=payload.get("name"),
            phone=payload.get("phone"),
            email=payload.get("email"),
            address=ClientAddress(
                city=payload.get("city"),
                street=payload.get("street"),
                house=payload.get("house"),
                building=payload.get("building"),
            ),
        )
