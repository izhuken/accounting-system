from flet import Column, Container, Divider, Image, Row, padding

from shared.colors import Colors
from shared.components.navbar.footer import NavFooter
from shared.components.spacer import Spacer
from shared.lib.asset import assets
from shared.lib.router import Router

from .button import NavButton


class NavBar(Container):
    def __init__(self, router: Router):
        self.router = router

        super().__init__(
            Column(
                controls=[
                    Container(
                        Row(
                            [
                                Image(
                                    assets("icons/logo.svg"),
                                    height=30,
                                )
                            ],
                        ),
                        padding=padding.only(top=20, left=100),
                    ),
                    Divider(color=Colors.WHITE, thickness=1),
                    Container(
                        Column(
                            controls=[
                                NavButton(
                                    "Заказы",
                                    "icons/orders.svg",
                                    "/orders",
                                    self.router,
                                ),
                                NavButton(
                                    "Накладные",
                                    "icons/invoices.svg",
                                    "/invoices",
                                    self.router,
                                ),
                                Spacer(),
                                NavButton(
                                    "Товары",
                                    "icons/products.svg",
                                    "/products",
                                    self.router,
                                ),
                                NavButton(
                                    "Материалы",
                                    "icons/materials.svg",
                                    "/materials",
                                    self.router,
                                ),
                                NavButton(
                                    "Склады",
                                    "icons/warehouses.svg",
                                    "/warehouses",
                                    self.router,
                                ),
                                NavButton(
                                    "Клиенты",
                                    "icons/clients.svg",
                                    "/clients",
                                    self.router,
                                ),
                                NavButton(
                                    "Подрядчики",
                                    "icons/contractors.svg",
                                    "/contractors",
                                    self.router,
                                ),
                                NavButton(
                                    "Пользователи",
                                    "icons/users.svg",
                                    "/users",
                                    self.router,
                                ),
                            ],
                        ),
                        expand=True,
                        padding=padding.only(left=10, right=10),
                    ),
                    NavFooter(),
                ],
            ),
            adaptive=True,
            bgcolor=Colors.BLUE_DARK,
            width=270,
        )
