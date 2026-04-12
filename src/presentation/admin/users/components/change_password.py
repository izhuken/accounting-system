from core.domain.entities import User
from core.service.app import UserService
from shared.components.common_input import CommonInput
from shared.components.form import CommonUpdateModal


class PasswordUpdateModal(CommonUpdateModal):
    modal_title: str = "Обновление пароля"
    topic_name: str = "user_list_page__refetch"
    entity: User = User
    entity_service = UserService

    def __init__(self, payload: dict):
        super().__init__(
            payload,
            {
                "password": CommonInput(label="Пароль"),
            },
        )

    def update_entity(self, payload: dict, entity: User) -> User:
        entity.update_password(payload.get("password"))
        return entity
