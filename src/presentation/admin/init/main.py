from PySide6.QtCore import Qt, QThread, Signal
from PySide6.QtWidgets import QLabel, QProgressBar, QVBoxLayout, QWidget

from core.service.command import InitThreadCommand
from shared.colors import Colors

# from shared.lib import Toaster


class InitPage(QWidget):
    navigate = Signal(str)

    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignCenter)
        layout.setSpacing(10)

        title = QLabel("Проводим настройку приложения...")
        title.setStyleSheet(
            """
            QLabel {
                font-size: 16px;
                font-weight: 400;
                color: %s;
            } 
        """
            % Colors.TEXT_DARK.value
        )
        layout.addWidget(title)

        progress_bar = QProgressBar()
        progress_bar.setRange(0, 0)
        progress_bar.setFixedSize(400, 10)
        progress_bar.setStyleSheet(
            f"""
        QProgressBar {{
            border: 1px solid {Colors.GRAY_DISABLED.value};
            border-radius: 5px;
        }}
                                   
        QProgressBar::chunk {{
            background-color: {Colors.BLUE_DARK.value};
            width: 10px;
            margin: 0px;
        }}
        """
        )

        layout.addWidget(progress_bar, alignment=Qt.AlignCenter)
        self.setLayout(layout)

        self.init_db()

    def init_db(self) -> None:
        self.thread = QThread()
        self.worker = InitThreadCommand()

        self.worker.moveToThread(self.thread)

        self.thread.started.connect(self.worker.execute)
        self.worker.finished.connect(self.thread.quit)
        self.worker.finished.connect(self.worker.deleteLater)
        self.thread.finished.connect(self.thread.deleteLater)
        self.worker.finished.connect(self.quit)
        self.thread.start()

    def quit(self) -> None:
        self.navigate.emit("login")
