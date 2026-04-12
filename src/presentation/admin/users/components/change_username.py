from core.domain.entities import User
from core.service.app import UserService
from shared.components.common_input import CommonInput
from shared.components.form import CommonUpdateModal


class UsernameUpdateModal(CommonUpdateModal):
    modal_title: str = "Обновление имени"
    topic_name: str = "user_list_page__refetch"
    entity: User = User
    entity_service = UserService

    def __init__(self, payload: dict):
        super().__init__(
            payload,
            {
                "username": CommonInput(label="Имя пользователя"),
            },
        )

    def update_entity(self, payload: dict, entity: User) -> User:
        entity.update_username(payload.get("username"))
        return entity
