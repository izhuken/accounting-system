from PySide6.QtCore import QObject
from PySide6.QtWidgets import QStackedWidget, QWidget


class Router(QObject):
    def __init__(self, stack: QStackedWidget):
        super().__init__(stack)
        self.stack = stack
        self.screens = {}

    def register_screen(self, name: str, widget: QWidget):
        self.screens[name] = widget
        self.stack.addWidget(widget)

        if hasattr(widget, "navigate"):
            widget.navigate.connect(self.route)

    def route(self, screen_name: str):
        if screen_name in self.screens:
            self.stack.setCurrentWidget(self.screens[screen_name])
        else:
            print(f"Screen '{screen_name}' не зарегистрирован!")
