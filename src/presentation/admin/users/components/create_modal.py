from core.domain.entities import User
from core.service.app import UserService
from shared.components.common_input import CommonInput
from shared.components.form import CommonCreateModal


class UserCreateModal(CommonCreateModal):
    modal_title: str = "Новый пользователь"
    topic_name: str = "user_list_page__refetch"
    entity: User = User
    entity_service = UserService

    def __init__(self):
        super().__init__(
            {
                "username": CommonInput(label="Имя пользователя"),
                "password": CommonInput(label="Пароль"),
            }
        )
