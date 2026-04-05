from PySide6.QtGui import QColor, QPalette
from PySide6.QtWidgets import QApplication, QMainWindow, QStackedWidget

import presentation.resources.admin_rc  # noqa:F401
from presentation.admin import InitPage, LoginPage
from shared.colors import Colors
from shared.lib.font import load_fonts
from shared.lib.router import Router


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Учет материалов")

        self.stack = QStackedWidget()
        self.router = Router(self.stack)

        init_page = InitPage()
        login_page = LoginPage()

        self.router.register_screen("init", init_page)
        self.router.register_screen("login", login_page)

        self.setCentralWidget(self.stack)
        self.showMaximized()

        self.router.route("init")


def main():
    app = QApplication()

    app.setStyle("Fusion")
    load_fonts(app)
    palette = QPalette()
    palette.setColor(QPalette.ColorRole.Window, QColor(Colors.BACKGROUND.value))
    palette.setColor(QPalette.ColorRole.Base, QColor(Colors.BACKGROUND.value))
    app.setPalette(palette)

    window = MainWindow()
    window.show()
    app.exec()


if __name__ == "__main__":
    main()
