from PySide6.QtCore import Qt, Signal
from PySide6.QtWidgets import (
    QFrame,
    QHBoxLayout,
    QHeaderView,
    QLabel,
    QPushButton,
    QScrollArea,
    QSizePolicy,
    QTableWidget,
    QTableWidgetItem,
    QVBoxLayout,
    QWidget,
)


class Sidebar(QWidget):
    def __init__(self):
        super().__init__()
        self.setObjectName("sidebar")
        self.setFixedWidth(240)

        layout = QVBoxLayout(self)
        layout.setContentsMargins(15, 20, 15, 20)

        logo = QLabel("ЯР")
        logo.setObjectName("logo")
        layout.addWidget(logo)

        btn_orders = QPushButton("Заказы")

        btn_items = QPushButton("Товары заказа")

        for b in [btn_orders, btn_items]:
            b.setObjectName("menuButton")
            layout.addWidget(b)

        layout.addStretch()

        layout.addWidget(QLabel("Пользователь 1"))
        self.setStyleSheet("""
            QWidget#sidebar {
                background: #000;
            }
        """)


class PageLayout(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout(self)
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(0)

        self.header = QWidget()
        self.content = QScrollArea()
        self.footer = QWidget()

        self.content.setWidgetResizable(True)
        self.content.setFrameShape(QFrame.NoFrame)

        self.content_widget = QWidget()
        self.content_layout = QVBoxLayout(self.content_widget)
        self.content_layout.setContentsMargins(0, 0, 0, 0)

        self.content.setWidget(self.content_widget)

        layout.addWidget(self.header)
        layout.addWidget(self.content, 1)
        layout.addWidget(self.footer)

        h = QVBoxLayout()

        h.addWidget(QLabel("Главная / Заказы"))

        title = QLabel("Заказы")
        title.setObjectName("pageTitle")
        h.addWidget(title)

        table = QTableWidget(30, 3)
        table.setHorizontalHeaderLabels(["#", "Название", "Действия"])
        table.verticalHeader().hide()

        table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        table.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        for i in range(30):
            table.setItem(i, 0, QTableWidgetItem(str(i + 1)))
            table.setItem(i, 1, QTableWidgetItem(f"Заказ №{i + 1}"))
            table.setCellWidget(i, 2, QPushButton("🗑"))

        self.content_layout.addWidget(table)

        f = QHBoxLayout(self.footer)
        f.addStretch()

        btn = QPushButton("Создать заказ")
        btn.setObjectName("primaryButton")
        f.addWidget(btn)


class OrderListPage(QWidget):
    navigate = Signal(str)

    def __init__(self):
        super().__init__()

        layout = QHBoxLayout()
        layout.setAlignment(Qt.AlignCenter)
        layout.setSpacing(0)

        layout.addWidget(Sidebar())
        layout.addWidget(PageLayout())

        self.setLayout(layout)
