from PySide6.QtCore import Qt, Signal
from PySide6.QtWidgets import QVBoxLayout, QWidget

from .components.login_form import LoginForm

# from shared.lib import Toaster


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

    def init_ui(self):
        self.setWindowTitle("Вход")

    def authenticate(self):
        print("submitted")
