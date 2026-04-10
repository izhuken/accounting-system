from alembic.util import CommandError
from flet import Column, Container, ProgressBar, Text, alignment

from core.domain.repositories.exc import SaveException
from core.service.command.init_command import InitCommand
from shared.colors import Colors
from shared.lib import Router, snack


class InitPage(Container):
    def __init__(self, router: Router) -> None:
        self.router = router

        super().__init__(
            Column(
                [
                    Text("Проводим настройку приложения...", color=Colors.TEXT_DARK),
                    ProgressBar(
                        width=400,
                        color=Colors.BLUE_DARK,
                        bgcolor=Colors.BACKGROUND,
                    ),
                ],
                height=200,
                width=400,
                expand=False,
            ),
            expand=True,
            alignment=alignment.Alignment.CENTER,
        )

    def did_mount(self):
        self.page.run_task(self.__init_db)

    async def __init_db(self):
        command = InitCommand()
        try:
            await command.execute()
            snack(self.page, "Успешно!")
            return self.router.go("/login")
        except CommandError, SaveException:
            return snack(self.page, "Ошибка при настройке приложения!")
