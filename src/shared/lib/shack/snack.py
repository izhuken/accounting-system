from enum import Enum

from PySide6.QtCore import (
    QEasingCurve,
    QPoint,
    QPropertyAnimation,
    Qt,
    QTimer,
)
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import (
    QGraphicsOpacityEffect,
    QHBoxLayout,
    QLabel,
    QPushButton,
    QSizePolicy,
    QWidget,
)

from shared.colors import Colors


class SnackbarType(Enum):
    INFO = "info"
    SUCCESS = "success"
    ERROR = "error"


class Snackbar(QWidget):
    def __init__(
        self,
        parent: QWidget,
        text: str,
        _type: SnackbarType = SnackbarType.INFO,
        duration: int = 1500,
    ):
        super().__init__(parent)

        self.duration = duration
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setAttribute(Qt.WA_TransparentForMouseEvents, False)

        self.setObjectName("Snackbar")

        layout = QHBoxLayout(self)
        layout.setContentsMargins(14, 10, 10, 10)
        layout.setSpacing(8)

        match _type:
            case SnackbarType.INFO:
                icon = QIcon(":/icons/info.svg")
                self.background_color = Colors.BLUE_LIGHT.value
            case SnackbarType.SUCCESS:
                icon = QIcon(":/icons/success.svg")
                self.background_color = Colors.GREEN_LIGHT.value
            case SnackbarType.ERROR:
                icon = QIcon(":/icons/error.svg")
                self.background_color = Colors.RED_LIGHT.value

        icon_label = QLabel()
        icon_label.setPixmap(icon.pixmap(18, 18))
        layout.addWidget(icon_label)

        self.label = QLabel(text)
        self.label.setObjectName("SnackbarLabel")
        self.label.setSizePolicy(
            QSizePolicy.Maximum,
            QSizePolicy.Preferred,
        )
        layout.addWidget(self.label)

        layout.addStretch()

        self.close_button = QPushButton("✕")
        self.close_button.setCursor(Qt.PointingHandCursor)
        self.close_button.setFixedSize(20, 20)
        self.close_button.clicked.connect(self.hide_snack)
        layout.addWidget(self.close_button)

        self.setStyleSheet(
            f"""
            QWidget#Snackbar {{
                background: {self.background_color};
                color: {Colors.TEXT_DARK.value};
                border-radius: 8px;
            }}

            QLabel#SnackbarLabel {{
                color: {Colors.TEXT_DARK.value};
                font-size: 14px;
                font-family: "Inter";
            }}

            QPushButton {{
                border: none;
                background: transparent;
                color: {Colors.TEXT_DARK.value};
                font-weight: bold;
            }}

            QPushButton:hover {{
                color: {Colors.TEXT_DARK.value};
            }}
            """
        )

        self.adjustSize()

        self.opacity = QGraphicsOpacityEffect(self)
        self.setGraphicsEffect(self.opacity)

    def _bottom_position(self) -> QPoint:
        parent = self.parentWidget()
        x = (parent.width() - self.width()) // 2
        y = parent.height() - self.height() - 20
        return QPoint(x, y)

    def show_snack(self):
        parent = self.parentWidget()
        self.adjustSize()

        end_position = self._bottom_position()
        start_pos = QPoint(end_position.x(), parent.height() + self.height())

        self.move(start_pos)
        self.show()
        self.raise_()

        self.anim = QPropertyAnimation(self, b"pos")
        self.anim.setDuration(250)
        self.anim.setStartValue(start_pos)
        self.anim.setEndValue(end_position)
        self.anim.setEasingCurve(QEasingCurve.OutCubic)
        self.anim.start()

        # автоматическое сокрытие
        QTimer.singleShot(self.duration, self.hide_snack)

    def hide_snack(self):
        parent = self.parentWidget()

        end_position = QPoint(self.x(), parent.height() + self.height())

        self.anim = QPropertyAnimation(self, b"pos")
        self.anim.setDuration(250)
        self.anim.setStartValue(self.pos())
        self.anim.setEndValue(end_position)
        self.anim.setEasingCurve(QEasingCurve.InCubic)
        self.anim.finished.connect(self.deleteLater)
        self.anim.start()
