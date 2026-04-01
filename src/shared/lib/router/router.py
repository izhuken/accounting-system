from PySide6.QtCore import QObject
from PySide6.QtWidgets import QStackedWidget, QWidget


class Router(QObject):
    def __init__(self, stack: QStackedWidget) -> None:
        super().__init__()
        self.stack = stack
        self.screens = {}

    def register_screen(self, name: str, widget: QWidget) -> None:
        self.screens[name] = widget
        self.stack.addWidget(widget)
        if hasattr(widget, "navigate"):
            widget.navigate.connect(self.route)

    def route(self, route_str: str) -> None:
        parts = route_str.split("/")
        screen_name = parts[0]
        params = {}

        # Если есть :id
        if len(parts) > 1:
            params["id"] = parts[1]

        if screen_name in self.screens:
            widget = self.screens[screen_name]
            # Если экран поддерживает set_params, передаем параметры
            if hasattr(widget, "set_params"):
                widget.set_params(**params)
            self.stack.setCurrentWidget(widget)
        else:
            print(f"Screen '{screen_name}' не зарегистрирован!")
