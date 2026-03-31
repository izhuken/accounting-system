from PySide6.QtCore import Qt
from PySide6.QtWidgets import QPushButton

from shared.colors import Colors


class CommonButton(QPushButton):
    def __init__(self, text: str) -> None:
        super().__init__(text)

        self.setCursor(Qt.PointingHandCursor)
        self.setMinimumHeight(60)
        self.adjustSize()

        self.setStyleSheet(
            """
        CommonButton {
            border-radius: 5px;
            padding-left: 20px;
            padding-right: 20px;
            border: none;
            min-height: 60px;

            font-size: 16px;
            font-weight: 500;
                                    
            color: %s;
            background-color: %s;
        }

        CommonButton:disabled {
            color: %s;
            background-color: %s;
        }
        """
            % (
                Colors.WHITE.value,
                Colors.BLUE_DARK.value,
                Colors.TEXT_DISABLED.value,
                Colors.GRAY_DISABLED.value,
            )
        )
