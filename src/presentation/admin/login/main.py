from flet import (
    Column,
    Container,
    FontWeight,
    Ref,
    Text,
    TextField,
    alignment,
)

from core.service.router import Router
from shared.colors import Colors
from shared.components import CommonButton


class LoginPage(Container):
    def __init__(self, router: Router):
        self.router = router
        # self._service = UserService()
        self.password_field_ref = Ref[TextField]()

        super().__init__(
            Column(
                [
                    Text(
                        "Вход",
                        color=Colors.TEXT_DARK,
                        size=32,
                        weight=FontWeight.W_600,
                    ),
                    Text(
                        "Войдите в систему, чтобы приступить к работе",
                        color=Colors.TEXT_DARK,
                        weight=FontWeight.W_400,
                        size=16,
                    ),
                    TextField(
                        password=True,
                        label="Пароль",
                        color=Colors.TEXT_DARK,
                        ref=self.password_field_ref,
                        width=480,
                    ),
                    CommonButton("Войти", self.authenticate),
                ],
                width=480,
                height=250,
                alignment=alignment.Alignment.CENTER,
                expand=False,
            ),
            alignment=alignment.Alignment.CENTER,
            expand=True,
        )

    def authenticate(self):
        pass
