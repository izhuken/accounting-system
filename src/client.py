from PySide6.QtCore import QObject, Signal
from PySide6.QtWidgets import (
    QApplication,
    QPushButton,
    QStackedWidget,
    QVBoxLayout,
    QWidget,
)

# --- Экраны ---


class Screen1(QWidget):
    # Сигнал для перехода на другой экран
    navigate = Signal(str)

    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        button = QPushButton("Перейти на Screen 2")
        button.clicked.connect(lambda: self.navigate.emit("screen2"))
        layout.addWidget(button)
        self.setLayout(layout)


class Screen2(QWidget):
    navigate = Signal(str)

    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        button1 = QPushButton("Назад на Screen 1")
        button1.clicked.connect(lambda: self.navigate.emit("screen1"))
        button2 = QPushButton("Перейти на Screen 3")
        button2.clicked.connect(lambda: self.navigate.emit("screen3"))
        layout.addWidget(button1)
        layout.addWidget(button2)
        self.setLayout(layout)


class Screen3(QWidget):
    navigate = Signal(str)

    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        button = QPushButton("Назад на Screen 1")
        button.clicked.connect(lambda: self.navigate.emit("screen1"))
        layout.addWidget(button)
        self.setLayout(layout)


# --- Контроллер навигации ---


class Router(QObject):
    def __init__(self, stack: QStackedWidget):
        super().__init__()
        self.stack = stack
        self.screens = {}

    def register_screen(self, name: str, widget: QWidget):
        self.screens[name] = widget
        self.stack.addWidget(widget)
        # Подключаем сигнал navigate, если он есть
        if hasattr(widget, "navigate"):
            widget.navigate.connect(self.route)

    def route(self, screen_name: str):
        if screen_name in self.screens:
            self.stack.setCurrentWidget(self.screens[screen_name])
        else:
            print(f"Screen '{screen_name}' не зарегистрирован!")


# --- Основное приложение ---

app = QApplication([])

stack = QStackedWidget()
router = Router(stack)

# Создаем и регистрируем экраны
screen1 = Screen1()
screen2 = Screen2()
screen3 = Screen3()

router.register_screen("screen1", screen1)
router.register_screen("screen2", screen2)
router.register_screen("screen3", screen3)

# Показываем первый экран
stack.setCurrentWidget(screen1)
stack.show()

app.exec()
