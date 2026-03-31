from PySide6.QtGui import QColor, QPalette
from PySide6.QtWidgets import QApplication, QMainWindow, QStackedWidget

from core.service.router import Router
from presentation.admin import InitPage
from shared.colors import Colors


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Учет материалов")

        self.showMaximized()

        stack = QStackedWidget()
        router = Router(stack)

        init_page = InitPage()
        router.register_screen("init", init_page)

        self.setCentralWidget(stack)


def main():
    app = QApplication()

    app.setStyle("Fusion")
    palette = QPalette()
    palette.setColor(QPalette.ColorRole.Window, QColor(Colors.BACKGROUND.value))
    palette.setColor(QPalette.ColorRole.Base, QColor(Colors.BACKGROUND.value))
    app.setPalette(palette)

    window = MainWindow()
    window.show()

    app.exec()


if __name__ == "__main__":
    main()
