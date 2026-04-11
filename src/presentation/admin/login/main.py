from flet import (
    Container,
    alignment,
)

from core.config import Config
from core.service.app import UserService
from shared.lib.router import Router

from .components.login_form import LoginForm


class LoginPage(Container):
    def __init__(self, router: Router):
        self.router = router
        self.auth_service = UserService()
        super().__init__(
            LoginForm(self.router),
            alignment=alignment.Alignment.CENTER,
            expand=True,
        )

    def did_mount(self):
        if Config.is_dev:
            self.router.go("/orders")
