from PySide6.QtCore import QPropertyAnimation, Qt, QTimer
from PySide6.QtGui import QGuiApplication, QPainter, QPaintEvent
from PySide6.QtWidgets import (
    QHBoxLayout,
    QLabel,
    QSizePolicy,
    QWidget,
)

from shared.colors import Colors


class Toast(QWidget):
    def __init__(
        self,
        parent=None,
        message="",
        timeout=1500,
    ):
        super().__init__(parent)
        self.parent = parent
        self.timer = QTimer()
        self.timer.singleShot(timeout, self.close)
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.Tool | Qt.WindowStaysOnTopHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        self.layout = QHBoxLayout()

        self.layout.setObjectName("Layout")
        self.setLayout(self.layout)
        self.animation = None
        self.__init_ui(message)
        self.__create_animation(timeout)
        self.bottom()
        self.adjustSize()

    @property
    def layout_height(self):
        return self.layout.minimumSize().height()

    @property
    def layout_width(self):
        return self.layout.minimumSize().width()

    def message(self, message: str) -> Toast:
        self.message_label.setText(message)
        return self

    def timeout(self, timeout: int) -> Toast:
        self.timer.stop()
        self.timer.singleShot(timeout, self.close)
        self.__create_animation(timeout)
        return self

    def info(self) -> Toast:
        self.setStyleSheet(f"""
            #LabelMessage {{
                color: {Colors.TEXT_DARK.value};
                text-align: center;
            }}
            QWidget {{
                background-color: {Colors.BLUE_LIGHT.value};
                opacity: 1;
                padding: 10px;
                border-radius: 10px;
            }}
        """)
        return self

    def center(self) -> Toast:
        if self.parent:
            toast_x = self.parent.x() + int(
                (self.parent.width() - self.layout_width) / 2
            )
            toast_y = self.parent.y() + int(
                (self.parent.height() - self.layout_height) / 2 + 40
            )
            self.move(toast_x, toast_y)
        else:
            screen = QGuiApplication.primaryScreen().size()
            size = self.geometry()
            self.move(
                int((screen.width() - size.width()) / 2),
                int((screen.height() - size.height()) / 2) + 40,
            )
        return self

    def bottom(self) -> Toast:
        if self.parent:
            toast_x = self.parent.x() + int(
                (self.parent.width() - self.layout_width) / 2
            )
            toast_y = self.parent.y() + int((self.parent.height() - self.layout_height))
            self.move(toast_x, toast_y)
        else:
            screen = QGuiApplication.primaryScreen().size()
            size = self.geometry()
            self.move(
                int((screen.width() - size.width()) / 2),
                int((screen.height() - size.height())),
            )
        return self

    def top(self) -> Toast:
        if self.parent:
            toast_x = self.parent.x() + int(
                (self.parent.width() - self.layout_width) / 2
            )
            toast_y = self.parent.y() + 40
            self.move(toast_x, toast_y)
        else:
            screen = QGuiApplication.primaryScreen().size()
            size = self.geometry()
            self.move(int((screen.width() - size.width()) / 2), 40)
        return self

    def __init_ui(self, message):
        self.message_label = QLabel()
        if self.parent:
            self.message_label.setMaximumSize(self.parent.size())
        self.size_policy = QSizePolicy()
        self.size_policy.setHorizontalStretch(0)
        self.size_policy.setVerticalStretch(0)
        self.size_policy.setHeightForWidth(
            self.message_label.sizePolicy().hasHeightForWidth()
        )
        self.message_label.setSizePolicy(self.size_policy)
        self.message_label.setWordWrap(True)
        self.message_label.setText(message)
        self.message_label.setTextFormat(Qt.AutoText)
        self.message_label.setScaledContents(True)
        self.message_label.setObjectName("LabelMessage")
        self.message_label.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.message_label)

    def __create_animation(self, timeout):
        self.animation = QPropertyAnimation(self, b"windowOpacity")
        self.animation.setTargetObject(self)
        self.animation.setStartValue(0)
        self.animation.setKeyValueAt(0.2, 0.7)
        self.animation.setKeyValueAt(0.8, 0.7)
        self.animation.setEndValue(0)
        self.animation.setDuration(timeout)
        self.animation.start()

    def paintEvent(self, a0: QPaintEvent):
        qp = QPainter()
        qp.begin(self)
        qp.setRenderHints(QPainter.Antialiasing, True)
        # qp.setBrush(QBrush(Qt.black))
        rect = self.rect()
        rect.setWidth(rect.width() - 1)
        rect.setHeight(rect.height() - 1)
        qp.end()
