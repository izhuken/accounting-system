from typing import Callable

from flet import (
    BorderRadius,
    Container,
    ControlState,
    FontWeight,
    Icon,
    Icons,
    MainAxisAlignment,
    Ref,
    Row,
    Text,
    TextButton,
    border,
)

from shared.colors import Colors

from .dto import TableData


class TableFooter(Container):
    def __init__(
        self,
        payload: TableData,
        on_next: Callable | None = None,
        on_previous: Callable | None = None,
        ref=None,
    ):
        self.payload = payload
        self._color_statement = {
            ControlState.DEFAULT: Colors.WHITE,
            ControlState.DISABLED: Colors.GRAY_DISABLED,
        }
        self._pages_count_ref = Ref[Text]()
        self._next_button_ref = Ref[TextButton]()
        self._previous_button_ref = Ref[TextButton]()

        super().__init__(
            Row(
                [
                    TextButton(
                        content=Row(
                            [
                                Icon(
                                    Icons.KEYBOARD_ARROW_LEFT_OUTLINED,
                                    size=16,
                                    color=self._color_statement,
                                ),
                                Text(
                                    "Назад",
                                    color=self._color_statement,
                                    weight=FontWeight.W_600,
                                ),
                            ],
                            spacing=2,
                            alignment=MainAxisAlignment.CENTER,
                        ),
                        disabled=not self.payload.has_previous,
                        on_click=on_previous,
                        ref=self._previous_button_ref,
                    ),
                    Text(
                        f"Страница {self.payload.page} из {self.payload.total_pages or 1}",
                        weight=FontWeight.W_600,
                        color=Colors.WHITE,
                        ref=self._pages_count_ref,
                    ),
                    TextButton(
                        content=Row(
                            [
                                Text(
                                    "Вперед",
                                    color=self._color_statement,
                                    weight=FontWeight.W_600,
                                ),
                                Icon(
                                    Icons.KEYBOARD_ARROW_RIGHT_OUTLINED,
                                    size=16,
                                    color=self._color_statement,
                                ),
                            ],
                            alignment=MainAxisAlignment.CENTER,
                            spacing=2,
                        ),
                        disabled=not self.payload.has_next,
                        on_click=on_next,
                        ref=self._next_button_ref,
                    ),
                ],
                height=42,
            ),
            height=50,
            border=border.only(
                left=border.BorderSide(1, Colors.BLACK),
                right=border.BorderSide(1, Colors.BLACK),
                bottom=border.BorderSide(1, Colors.BLACK),
            ),
            border_radius=BorderRadius(0, 0, 5, 5),
            bgcolor=Colors.BLUE_OCEAN,
            ref=ref,
        )

    def refresh(self, new_data: TableData):
        self.payload = new_data
        self._pages_count_ref.current.value = (
            f"Страница {new_data.page} из {new_data.total_pages or 1}"
        )
        self._next_button_ref.current.disabled = not new_data.has_next
        self._previous_button_ref.current.disabled = not new_data.has_previous
        self._next_button_ref.current.update()
        self._previous_button_ref.current.update()
        self._pages_count_ref.current.update()
