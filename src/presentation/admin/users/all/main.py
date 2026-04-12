from typing import Any

from flet import Ref

from core.service.app import UserService
from presentation.admin.users.components import ActionsView, UserCreateModal
from shared.components.breadcrumb import BreadcrumbsConfig
from shared.components.common_page import CommonPage
from shared.components.table import Table, TableAccessor, TableData, TableRefreshEvent
from shared.lib.router import Router


class UserListPage(CommonPage):
    title: str = "Пользователи"
    topic_name: str = "user_list_page__refetch"

    def __init__(self, router: Router):
        self.__table_ref = Ref[Table]()

        super().__init__(
            title=self.title,
            router=router,
            content=[
                Table(
                    [
                        TableAccessor("Имя пользователя", "username", expand=True),
                        TableAccessor(
                            "Действия", "actions", width=180, view=ActionsView
                        ),
                    ],
                    topic_name=self.topic_name,
                    on_add=self.__open_create_form,
                    ref=self.__table_ref,
                )
            ],
            breadcrumbs=[
                BreadcrumbsConfig("Главная"),
                BreadcrumbsConfig("Пользователи", "/users"),
            ],
        )

    def did_mount(self):
        self.page.run_task(self.__fetch_data)
        self.page.pubsub.subscribe_topic(self.topic_name, self.__handle_message)

    def will_unmount(self):
        self.page.pubsub.unsubscribe_topic(self.topic_name)

    async def __handle_message(self, topic: str, data: Any):
        if isinstance(data, TableRefreshEvent):
            return await self.__fetch_data(data.next_page)

        return await self.__fetch_data()

    async def __fetch_data(self, page: int = 0):
        user_service = UserService()
        paginated_response = await user_service.all(records=20, page=page)
        self.__table_ref.current.refresh(
            TableData(
                data=[entity.to_dict() for entity in paginated_response.data],
                has_next=paginated_response.has_next,
                has_previous=paginated_response.has_previous,
                page=paginated_response.page,
                total_pages=paginated_response.pages,
            )
        )

    def __open_create_form(self):
        user_create_modal = UserCreateModal()
        self.page.show_dialog(user_create_modal)
