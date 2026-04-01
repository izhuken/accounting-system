import sys

from PySide6.QtWidgets import QApplication, QPushButton, QVBoxLayout, QWidget

from shared.lib.toast import Toast


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(400, 400)
        layout = QVBoxLayout(self)
        layout.addWidget(QPushButton("top Toast", self, clicked=self.show_top))
        layout.addWidget(QPushButton("center Toast", self, clicked=self.show_center))
        layout.addWidget(QPushButton("bottom Toast", self, clicked=self.show_bottom))

    def show_top(self):
        Toast("Pyside6 Toast", parent=self).top().show()

    def show_center(self):
        Toast("Pyside6 Toast", parent=self).center().show()

    def show_bottom(self):
        Toast(parent=self).message("someone asdlkfjas hkldfja hslkdjhfa lk").timeout(
            1111
        ).bottom().info().show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = Window()
    w.show()
    sys.exit(app.exec())
