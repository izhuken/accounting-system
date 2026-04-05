from PySide6.QtCore import Qt
from PySide6.QtWidgets import QPushButton

from shared.colors import Colors


class CommonButton(QPushButton):
    def __init__(self, text: str) -> None:
        super().__init__(text)

        self.setCursor(Qt.PointingHandCursor)
        self.adjustSize()

        self.setStyleSheet(
            f"""
            CommonButton {{
                border-radius: 5px;
                border: none;
                padding: 20px 14px;
                
                font-size: 16px;
                font-family: "Inter";
                font-weight: 500;
                                        
                color: {Colors.WHITE.value};
                background-color: {Colors.BLUE_DARK.value};
            }}

            CommonButton:disabled {{
                color: {Colors.TEXT_DISABLED.value};
                background-color: {Colors.GRAY_DISABLED.value};
            }}
            """
        )
