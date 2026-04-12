import warnings

from flet import Page, run

from presentation.admin import (
    ClientListPage,
    ContactorListPage,
    InitPage,
    InvoiceListPage,
    LoginPage,
    MaterialListPage,
    MetricListPage,
    OrderListPage,
    ProductListPage,
    UserListPage,
    WarehouseListPage,
)
from shared.colors import Colors
from shared.lib.router import Router


async def main(page: Page):
    warnings.filterwarnings("ignore", category=DeprecationWarning)

    page.title = "Учет материалов"
    page.window.icon = "icons/favicon.ico"
    page.padding = 0
    page.bgcolor = Colors.BACKGROUND
    page.expand = 1
    page.window.maximized = True

    app_router = Router()

    app_router.set_routes(
        {
            "/init": InitPage,
            "/login": LoginPage,
            # orders section
            "/orders": OrderListPage,
            # invoices section
            "/invoices": InvoiceListPage,
            # products section
            "/products": ProductListPage,
            # materials section
            "/materials": MaterialListPage,
            "/materials/metrics": MetricListPage,
            # warehouses section
            "/warehouses": WarehouseListPage,
            # clients section
            "/clients": ClientListPage,
            # contractors section
            "/contractors": ContactorListPage,
            # users section
            "/users": UserListPage,
        }
    )

    app_router.page = page
    page.on_route_change = app_router.route_change
    page.add(app_router.body)
    app_router.go("/init")


run(main, name="Учет материалов", assets_dir="src/presentation/assets")
