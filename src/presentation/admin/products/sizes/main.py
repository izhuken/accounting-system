from typing import Any

from flet import Ref

from core.service.app import SizeService
from presentation.admin.products.components import SizeActionsView, SizeCreateModal
from presentation.admin.products.components.tabs import ProductTabs
from shared.components.breadcrumb.config import BreadcrumbsConfig
from shared.components.common_page import CommonPage
from shared.components.table.core import Table
from shared.components.table.dto import TableAccessor, TableData, TableRefreshEvent
from shared.lib.router import Router


class SizeListPage(CommonPage):
    title: str = "Размеры"
    topic_name: str = "size_list_page__refetch"

    def __init__(self, router: Router):
        self.__table_ref = Ref[Table]()

        super().__init__(
            title=self.title,
            router=router,
            content=[
                ProductTabs(router),
                Table(
                    [
                        TableAccessor("Размер", "code", width=90),
                        TableAccessor("Рост", "height", expand=True),
                        TableAccessor(
                            "Действия", "actions", width=90, view=SizeActionsView
                        ),
                    ],
                    topic_name=self.topic_name,
                    on_add=self.__open_create_form,
                    ref=self.__table_ref,
                ),
            ],
            breadcrumbs=[
                BreadcrumbsConfig("Главная"),
                BreadcrumbsConfig("Товары", "/products"),
                BreadcrumbsConfig("Размеры", "/products/sizes"),
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
        entity_service = SizeService()
        paginated_response = await entity_service.all(records=20, page=page)
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
        self.page.show_dialog(SizeCreateModal())
