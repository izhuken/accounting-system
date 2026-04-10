from PySide6.QtWidgets import (
    QHBoxLayout,
    QLabel,
    QVBoxLayout,
    QWidget,
)

from shared.components.sidebar.button import SidebarButton


class Sidebar(QWidget):
    def __init__(self):
        super().__init__()
        self.setObjectName("sidebar")
        self.setFixedWidth(240)

        layout = QVBoxLayout(self)
        layout.setContentsMargins(15, 20, 15, 20)
        layout.addStretch()

        # logo container
        logo_container = QWidget()
        logo_container.setObjectName("logoContainer")
        logo = QLabel("ЯР")
        logo.setObjectName("logo")
        logo_container.addWidget(logo)
        layout.addWidget(logo_container)

        # navigation buttons container
        nav_buttons_container = QWidget()
        nav_buttons_layout = QVBoxLayout()
        nav_buttons_container.setLayout(nav_buttons_layout)
        nav_buttons_container.setObjectName("navButtonsContainer")

        orders_button = SidebarButton("Заказы")
        invoice_button = SidebarButton("Накладные")
        products_button = SidebarButton("Товары")
        materials_button = SidebarButton("Материалы")
        warehouses_button = SidebarButton("Склады")
        clients_button = SidebarButton("Клиенты")
        contractors_button = SidebarButton("Подрядчики")
        users_button = SidebarButton("Пользователи")

        nav_buttons_layout.addWidget(orders_button, ":/icons/orders.svg")
        nav_buttons_layout.addWidget(invoice_button, ":/icons/invoices.svg")
        nav_buttons_layout.addWidget(products_button, ":/icons/products.svg")
        nav_buttons_layout.addWidget(materials_button, ":/icons/materials.svg")
        nav_buttons_layout.addWidget(warehouses_button, ":/icons/warehouses.svg")
        nav_buttons_layout.addWidget(clients_button, ":/icons/clients.svg")
        nav_buttons_layout.addWidget(contractors_button, ":/icons/contractors.svg")
        nav_buttons_layout.addWidget(users_button, ":/icons/users.svg")

        layout.addWidget(nav_buttons_container)

        # footer container
        footer_buttons_container = QWidget()
        footer_buttons_layout = QHBoxLayout()
        footer_buttons_container.setLayout(nav_buttons_layout)
        footer_buttons_container.setObjectName("navButtonsContainer")

        username_label = QLabel("Пользователь 1")

        footer_buttons_layout.addWidget(username_label)
