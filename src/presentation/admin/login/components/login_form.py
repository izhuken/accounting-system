from PySide6.QtCore import Qt, Signal
from PySide6.QtWidgets import QLabel, QVBoxLayout, QWidget

from shared.colors import Colors
from shared.components import CommonButton
from shared.components.common_input import CommonInput, InputType


class LoginForm(QWidget):
    submit = Signal()

    def __init__(self) -> None:
        super().__init__()

        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignCenter)
        layout.setSpacing(10)

        title = QLabel("Вход")
        title.setObjectName("title")
        subtitle = QLabel("Войдите в систему, чтолбы приступить к работе")

        self.password_input = CommonInput(
            placeholder="Введите пароль", _type=InputType.PASSWORD
        )

        self.submit_button = CommonButton("Submit")
        self.submit_button.clicked.connect(self.__submit)

        layout.addWidget(title)
        layout.addWidget(subtitle)
        layout.addWidget(self.password_input)
        layout.addWidget(self.submit_button)

        self.init_ui()
        self.setLayout(layout)

    def init_ui(self) -> None:
        self.setWindowTitle("Вход")
        self.setStyleSheet(f"""
            QWidget {{
                max-width: 400px;
            }}
                           
            QLabel {{
                color: {Colors.TEXT_DARK.value};
                font-family: "Inter";
                font-size: 16px;
            }}

            QLabel#title {{
                font-weight: 500;
                font-size: 32px;
            }}
        """)

    def __submit(self) -> None:
        self.submit.emit()
