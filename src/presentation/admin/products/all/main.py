from presentation.admin.products.components import ProductTabs
from shared.components.breadcrumb import BreadcrumbsConfig
from shared.components.common_page import CommonPage
from shared.lib.router import Router


class ProductListPage(CommonPage):
    def __init__(self, router: Router):
        super().__init__(
            "Товары",
            router,
            content=[
                ProductTabs(router),
            ],
            breadcrumbs=[
                BreadcrumbsConfig("Главная"),
                BreadcrumbsConfig("Товары", "/products"),
            ],
        )
