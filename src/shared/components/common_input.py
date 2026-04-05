from PySide6.QtCore import Qt
from PySide6.QtWidgets import QLineEdit

from shared.colors import Colors


class InputType:
    TEXT = "text"
    PASSWORD = "password"


class CommonInput(QLineEdit):
    def __init__(
        self,
        name: str | None = None,
        placeholder: str | None = None,
        _type: InputType = InputType.TEXT,
    ) -> None:
        super().__init__()

        self.setCursor(Qt.PointingHandCursor)
        self.adjustSize()

        if name:
            self.setObjectName(name)

        if placeholder:
            self.setPlaceholderText(placeholder)

        if _type == InputType.TEXT:
            self.setEchoMode(QLineEdit.Normal)

        if _type == InputType.PASSWORD:
            self.setEchoMode(QLineEdit.Password)

        self.setStyleSheet(
            f"""
            CommonInput {{
                border-radius: 5px;

                padding: 10px 14px;

                border: 1px solid {Colors.BLUE_ACCENT.value};

                font-size: 16px;
                font-family: "Inter";
                font-weight: 400;
                                        
                color: {Colors.TEXT_DARK.value};
            }}

            """
        )
