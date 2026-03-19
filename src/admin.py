from warnings import filterwarnings

from flet import Page, run

from core.service.router import Router
from presentation.admin import LoginPage
from shared.colors import Colors


async def main(page: Page):
    filterwarnings("ignore", category=DeprecationWarning)

    app_router = Router()

    page.title = "Учет материалов"
    page.padding = 0
    page.expand = 1
    page.bgcolor = Colors.BACKGROUND

    app_router.set_routes({"/login": LoginPage})

    app_router.page = page
    page.on_route_change = app_router.route_change
    page.add(app_router.body)
    app_router.go("/login")


run(main, name="Учет материалов", assets_dir="assets")
