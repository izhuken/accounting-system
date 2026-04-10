import warnings

from flet import Page, run

from presentation.admin import InitPage, LoginPage
from shared.colors import Colors
from shared.lib.router import Router


async def main(page: Page):
    warnings.filterwarnings("ignore", category=DeprecationWarning)

    page.title = "Учет материалов"
    page.window.icon = "icons/favicon.ico"
    page.padding = 0
    page.bgcolor = Colors.BACKGROUND
    page.expand = 1

    app_router = Router()

    app_router.set_routes(
        {
            "/init": InitPage,
            "/login": LoginPage,
        }
    )

    app_router.page = page
    page.on_route_change = app_router.route_change
    page.add(app_router.body)
    app_router.go("/init")


run(main, name="Учет материалов", assets_dir="src/presentation/assets")
