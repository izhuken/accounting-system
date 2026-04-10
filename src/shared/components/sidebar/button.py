from PySide6.QtCore import Qt
from PySide6.QtGui import QIcon, QSize
from PySide6.QtWidgets import QPushButton

from shared.colors import Colors


class SidebarButton(QPushButton):
    def __init__(self, text: str, icon: str) -> None:
        super().__init__(text)

        self.setCursor(Qt.PointingHandCursor)
        self.adjustSize()
        self.setIcon(QIcon(icon))
        self.setIconSize(QSize(14, 14))

        self.setStyleSheet(
            f"""
            SidebarButton {{
                border: none;
                border-radius: 5px;
                padding: 14px;

                font-size: 14px;
                font-family: "Inter";
                font-weight: 500;

                color: {Colors.WHITE.value};
                background-color: {Colors.BLUE_DARK.value};
            }}
            """
        )
