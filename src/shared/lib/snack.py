from flet import Image, Page, Row, SnackBar, Text

from shared.colors import Colors
from shared.lib.asset import assets


class SnackBarType:
    INFO = "info"
    SUCCESS = "success"
    ERROR = "error"


def snack(
    page: Page,
    message: str,
    _type: SnackBarType = SnackBarType.SUCCESS,
):
    icons = {
        SnackBarType.INFO: assets("icons/info.svg"),
        SnackBarType.SUCCESS: assets("icons/success.svg"),
        SnackBarType.ERROR: assets("icons/error.svg"),
    }
    colors = {
        SnackBarType.INFO: Colors.BLUE_LIGHT,
        SnackBarType.SUCCESS: Colors.GREEN_LIGHT,
        SnackBarType.ERROR: Colors.RED_LIGHT,
    }

    if not page:
        return

    page.show_dialog(
        SnackBar(
            Row([Image(icons[_type]), Text(message, color=Colors.TEXT_DARK)]),
            bgcolor=colors[_type],
        )
    )
    page.update()
