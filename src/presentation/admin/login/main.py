from PySide6.QtCore import Qt, QTimer, Signal
from PySide6.QtWidgets import QVBoxLayout, QWidget

from core.config import Config
from core.service.app.user_service import UserService
from core.service.exc.authentication import AuthenticationException
from shared.lib.shack import Snackbar
from shared.lib.shack.snack import SnackbarType

from .components.login_form import LoginForm


class LoginPage(QWidget):
    navigate = Signal(str)

    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()

        form = LoginForm()
        form.submit.connect(self.authenticate)

        layout.addWidget(form)
        layout.setAlignment(Qt.AlignCenter)

        self.init_ui()
        self.setLayout(layout)

        if Config.is_dev:
            QTimer.singleShot(1000, lambda: self.navigate.emit("orders/list"))

    def init_ui(self) -> None:
        self.setWindowTitle("Вход")

    def authenticate(self, password: str) -> None:
        service = UserService()

        try:
            service.authenticate(password)
            snack = Snackbar(self, "Успешно! Вы вошли в систему", SnackbarType.SUCCESS)
            snack.show_snack()
            self.navigate.emit("orders/list")
        except AuthenticationException as e:
            snack = Snackbar(self, e.message, SnackbarType.ERROR)
            snack.show_snack()
        except ValueError as e:
            snack = Snackbar(self, str(e), SnackbarType.ERROR)
            snack.show_snack()
