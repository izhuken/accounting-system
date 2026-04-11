from flet import Ref

from core.service.app import UserService
from presentation.admin.users.components import ActionsView
from shared.components.breadcrumb import BreadcrumbsConfig
from shared.components.common_page import CommonPage
from shared.components.table import Table, TableAccessor, TableData
from shared.lib.router import Router


class UserListPage(CommonPage):
    def __init__(self, router: Router):
        self.__table_ref = Ref[Table]()

        super().__init__(
            title="Пользователи",
            router=router,
            content=[
                Table(
                    [
                        TableAccessor("Имя пользователя", "username", expand=True),
                        TableAccessor(
                            "Действия", "actions", width=180, view=ActionsView
                        ),
                    ],
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

    async def __fetch_data(self):
        user_service = UserService()
        paginated_response = await user_service.all()
        self.__table_ref.current.refresh(
            TableData(
                data=[entity.to_dict() for entity in paginated_response.data],
                has_next=paginated_response.has_next,
                has_previous=paginated_response.has_previous,
                page=paginated_response.page,
                total_pages=paginated_response.count,
            )
        )
