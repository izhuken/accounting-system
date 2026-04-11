from flet import Alignment, Column, FontWeight, Ref, Text, TextField

from core.service.app import UserService
from core.service.exc import AuthenticationException
from shared.colors import Colors
from shared.components import CommonButton
from shared.lib import Router, SnackBarType, snack


class LoginForm(Column):
    def __init__(self, router: Router):
        self.router = router
        self.__password_ref = Ref[TextField]()

        super().__init__(
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
                    ref=self.__password_ref,
                    width=480,
                ),
                CommonButton("Войти", self.__authenticate),
            ],
            width=480,
            height=250,
            alignment=Alignment.CENTER,
            expand=False,
        )

    async def __authenticate(self) -> None:
        service = UserService()

        try:
            await service.authenticate(self.__password_ref.current.value)
            snack(self.page, "Успешно! Вы вошли в систему")
            self.router.go("/orders")
        except AuthenticationException as e:
            return snack(self.page, e.message, SnackBarType.ERROR)
        except ValueError as e:
            return snack(self.page, str(e), SnackBarType.ERROR)
